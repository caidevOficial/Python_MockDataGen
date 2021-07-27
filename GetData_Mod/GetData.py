# MIT License
#
# Copyright (C) 2021 <FacuFalcone - CaidevOficial>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from ntpath import join
import random

from faker import Faker as fk
import faker
from FileHandle_Mod.FileHandle import DoubleMessage as PMD
from FileHandle_Mod.FileHandle import SingleMessage as PMS


def GetRandomValueFaker(fakeType: str, fake: fk, listOfParameters: list):
    """
    Simulates a switch, only used for Faker class.
    Args:
        fakeType (str): String with the name of the method from Faker Class.
        fake (fk): The Faker Class.
    Returns:
        function: one of the methods of Faker Class.
    """
    fakeAttr = 'name'

    try:
        randomvalue = None
        fakeFunc = getattr(fake, fakeType)

        for i in range(len(listOfParameters)):
            if(len(listOfParameters) > 0):
                if(str(type(listOfParameters[i])) == "<class 'str'>" and listOfParameters[i].startswith('tuple')):
                    tupleArray = listOfParameters[i].replace(
                        'tuple(', '').replace(')', '').split(',')
                    listOfParameters[i] = tuple(tupleArray)
        if(len(listOfParameters) == 1):
            randomvalue = fakeFunc(listOfParameters[0])
        elif(len(listOfParameters) == 2):
            randomvalue = fakeFunc(listOfParameters[0], listOfParameters[1])
        elif(len(listOfParameters) == 3):
            randomvalue = fakeFunc(
                listOfParameters[0], listOfParameters[1], listOfParameters[2])
        elif(len(listOfParameters) == 4):
            randomvalue = fakeFunc(
                listOfParameters[0], listOfParameters[1], listOfParameters[2], listOfParameters[3])
        elif(len(listOfParameters) == 5):
            randomvalue = fakeFunc(
                listOfParameters[0], listOfParameters[1], listOfParameters[2], listOfParameters[3], listOfParameters[4])
        else:
            randomvalue = fakeFunc()
    except Exception as e:
        PMS(f'Error in the function getRandomValueFaker. Error: {e}')
        return getattr(fake, fakeAttr)
    finally:
        return randomvalue

def GetAmountOfRegisters(JSON_ALL_TABLES: dict, tableName: str) -> int:
    """
    Obtains the amount of registers from the config json.
    Args:
        JSON_ALL_TABLES (dict): A dictionary with all the tables and its configs.
        tableName (str): The name of the table to search the value.
    Returns:
        int: the amount of registers, otherwise 1000.
    """
    amountOfRegisters = 1000
    try:
        listMetadata = JSON_ALL_TABLES[tableName]["MetaData"]
        for index in range(0, len(listMetadata)):
            if("AmountOfRegisters" in listMetadata[index]):
                amountOfRegisters = listMetadata[index]["AmountOfRegisters"]
                break
    except Exception as e:
        PMD(f'\nError in obtaining the amount of registers.',
            'The default value was set to {amountOfRegisters}')
        PMS(f'Exception: {e}')
    finally:
        return amountOfRegisters

def GetRandomPkOrFk(listOfPk: dict, sourceTable: str, sourceField: str) -> str:
    """
    Obtains a random number from the list of pk of the table 'sourceTable'.
    Args:
        listOfPk (dict): The variable with the structure of the tables with theirs pk inside.
        sourceTable (str): Name of the table to search.
        sourceField (str): Name of the field of the table to search the list of pks.
    Returns:
        [int]: A random number between the list of pks.
    """
    try:
        randomPk = []
        listOfValues = listOfPk[sourceTable][sourceField]
        randomPk = random.choice(listOfValues)
    except:
        PMD(f'Error getting the list of pk from the table {sourceTable}.',
            'An empty list will be returned')
    finally:
        return randomPk

def GetColumnsNames(JSON_ALL_TABLES: dict, tableName:str) -> str:
    """[summary]
    Gets the name of the columns of a table.
    Args:
        JSON_ALL_TABLES (dict): [List of fields of the table to search]
    Returns:
        str: [Returns the name of the columns]
    """
    try:
        columnsListOfDictionary = JSON_ALL_TABLES[tableName]["Data"]
        columnsNames = ""
        if(len(columnsListOfDictionary) > 0):
            for index in range(0, len(columnsListOfDictionary)):
                if(index == 0):
                    columnsNames = columnsListOfDictionary[index]["name"]
                else:
                    columnsNames = columnsNames + "," + columnsListOfDictionary[index]["name"]
        
    except Exception as ww:
        PMS(f'Error in the function GetColumnsNames. Error: {ww}')
    finally:
        return columnsNames

def CreateRecordString(actualRecord:list, pksOfThisTable:list, values:list, jsonVariable:dict, jsonOfThisTable:dict, tableName:str, element:str, fake:faker) -> list:
    """[summary]
    Creates values for the actual record of the table formated as a string. 
    Args:
        actualRecord (list): [Actual record to be filled]
        pksOfThisTable (list): [Dictionary with the pks of the table]
        values (list): [List to be filled with the values of the pks of the table]
        jsonVariable (dict): [The variable with the structure of the tables with theirs pk inside.]
        jsonOfThisTable (dict): [Json with the name and pks of all the tables of the database.]
        tableName (str): [Name of the table to search]
        element (str): [Dictionary of the column of the table]
        fake (faker): [Faker objecto to create random values]
    Returns:
        list: [List of records formated as a string]
    """
    if('ispk' in element.keys()):
        uniqueID = fake.unique.bothify(element["format"], element["letters"])

        actualRecord.append(f'"{uniqueID}"')
        pksOfThisTable.append(uniqueID)
        columnName = element["name"]

        if (not columnName in jsonOfThisTable[tableName]):
            values.append(uniqueID)
            jsonOfThisTable[tableName][columnName] = values
        else:
            values = jsonOfThisTable[tableName][columnName]
            values.append(uniqueID)
            jsonOfThisTable[tableName][columnName] = values

    elif ('faketype' in element.keys()):
        fakeType = element["faketype"]
        listOfParameters = []
        if(fakeType == "bothify"):
            dataCell = fake.botify(element["format"], element["letters"])
            actualRecord.append(f'"{dataCell}"')

        elif ('parameters' in element.keys()):
            listOfParameters = element["parameters"]
            actualRecord.append(f"'{GetRandomValueFaker(fakeType, fake, listOfParameters)}'")

    elif ('isfk' in element.keys()):
        sourceTable = element["sourceTable"]
        sourceField = element["sourceField"]

        randomPK = GetRandomPkOrFk(jsonVariable, sourceTable, sourceField)
        actualRecord.append(f'"{randomPK}"')
    
    return actualRecord

def CreateRecordNormal(actualRecord:list, pksOfThisTable:list, values:list, jsonVariable:dict, jsonOfThisTable:dict, tableName:str, element:str, fake:faker) -> list:
    """[summary]
    Creates values for the actual record of the table.
    Args:
        actualRecord (list): [Actual record to be filled]
        pksOfThisTable (list): [Dictionary with the pks of the table]
        values (list): [List to be filled with the values of the pks of the table]
        jsonVariable (dict): [The variable with the structure of the tables with theirs pk inside.]
        jsonOfThisTable (dict): [Json with the name and pks of all the tables of the database.]
        tableName (str): [Name of the table to search]
        element (str): [Dictionary of the column of the table]
        fake (faker): [Faker objecto to create random values]
    Returns:
        list: [description]
    """
    if (not tableName in jsonOfThisTable):
        jsonOfThisTable[tableName] = {}

    if('ispk' in element.keys()):
        uniqueID = fake.unique.bothify(element["format"], element["letters"])

        actualRecord.append(uniqueID)
        pksOfThisTable.append(uniqueID)
        columnName = element["name"]

        if (not columnName in jsonOfThisTable[tableName]):
            values.append(uniqueID)
            jsonOfThisTable[tableName][columnName] = values
        else:
            values = jsonOfThisTable[tableName][columnName]
            values.append(uniqueID)
            jsonOfThisTable[tableName][columnName] = values

    elif ('faketype' in element.keys()):
        fakeType = element["faketype"]
        listOfParameters = []
        if(fakeType == "bothify"):
            dataCell = fake.botify(element["format"], element["letters"])
            actualRecord.append(str(dataCell))

        elif ('parameters' in element.keys()):
            listOfParameters = element["parameters"]
            actualRecord.append(GetRandomValueFaker(fakeType, fake, listOfParameters))

    elif ('isfk' in element.keys()):
        sourceTable = element["sourceTable"]
        sourceField = element["sourceField"]

        randomPK = GetRandomPkOrFk(jsonVariable, sourceTable, sourceField)
        actualRecord.append(str(randomPK))
    
    return actualRecord

def CreateRecords(JSON_ALL_TABLES: dict, tableName: str, amountOfRegisters: int, jsonVariable: dict, sqlStatement:bool):
    """
    Creates 'amountOfRegisters' registers for the table 'tableName'.
    Args:
        JSON_ALL_TABLES (dict): The variable with the configuration of the tables.
        tableName (str): The name of the actual table to create the registers.
        amountOfRegisters (int): The amount of registers.
        jsonVariable (dict): The variable with the structure of the tables with theirs pk inside.
    Returns:
        string: A string with all the registers of the table.
        dict: A dictionary with the table and its pks values.
    """
    
    nameOfColumns = ""
    tableRecords = ""
    actualRecord = []
    listOfValues = []
    pksOfThisTable = []
    jsonOfThisTable = {}
    fake = fk()

    PMD(f'Creating registers for the table {tableName}',
        'This action may taking a while...')

    try:
        counter = 0
        nameOfColumns = GetColumnsNames(JSON_ALL_TABLES, tableName)
        statement = f"INSERT INTO {tableName} ({nameOfColumns}) VALUES("
        tableRecords+= tableRecords.join(nameOfColumns).join("\n")
        if(sqlStatement):
            register = "Querys"
        else:
            register = "Records"

        for number in range(0, amountOfRegisters):
            listOfValues:list = JSON_ALL_TABLES[tableName]["Data"]

            for element in listOfValues:
                values = []
                if (not tableName in jsonOfThisTable):
                    jsonOfThisTable[tableName] = {}

                if(element["type"] == "STRING" and sqlStatement):
                    actualRecord = CreateRecordString(actualRecord, pksOfThisTable, values, jsonVariable, jsonOfThisTable, tableName, element, fake)
                else:
                    actualRecord = CreateRecordNormal(actualRecord, pksOfThisTable, values, jsonVariable, jsonOfThisTable, tableName, element, fake)
                
            if(sqlStatement):
                tableRecords += f"{statement}" + ",".join(map(str, actualRecord))+");\n"
            else:
                tableRecords += ",".join(map(str, actualRecord))+"\n"
            actualRecord.clear()
            jsonVariable.update(jsonOfThisTable)
            counter += 1

            if counter == 5000:
                
                PMS(f"## {register} Created: {number+1}")
                counter = 0
    except Exception as aa:
        PMS(f'Error getting the list of values of the "Data" field of {tableName}')
        PMS(f'Exception: {aa}')
    finally:
        PMS(f"## Total {register} Created: {number+1}")
        return tableRecords, jsonVariable
