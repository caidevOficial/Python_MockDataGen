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

from FileHandle_Mod.FileHandle import SingleMessage as PMS, DoubleMessage as PMD
from faker import Faker as fk
import random


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


def GetAmountOfRegisters(TABLE_DATA_Fields: dict, tableName: str) -> int:
    """
    Obtains the amount of registers from the config json.
    Args:
        TABLE_DATA_Fields (dict): A dictionary with all the configs of the tables.
        tableName (str): The name of the table to search the value.

    Returns:
        int: the amount of registers, otherwise 1000.
    """
    amountOfRegisters = 1000
    try:
        listMetadata = TABLE_DATA_Fields[tableName]["MetaData"]
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


def CreateRecords(TABLE_FIELDS: list, tableName: str, amountOfRegisters: int, jsonVariable: dict):
    """
    Creates 'amountOfRegisters' registers for the table 'tableName'.
    Args:
        TABLE_FIELDS (list): The variable with the configuration of the tables.
        tableName (str): The name of the actual table to create the registers.
        amountOfRegisters (int): The amount of registers.
        jsonVariable (dict): The variable with the structure of the tables with theirs pk inside.

    Returns:
        string: A string with all the registers of the table.
        dict: A dictionary with the table and its pks values.
    """

    tableRecords = "\n"
    actualRecord = []
    listOfValues = []
    pksOfThisTable = []
    jsonOfThisTable = {}
    fake = fk()

    PMD(f'Creating registers for the table {tableName}',
        'This action may taking a while...')

    try:
        counter = 0
        for number in range(0, amountOfRegisters):
            listOfValues = TABLE_FIELDS[tableName]["Data"]

            for element in listOfValues:
                values = []

                if (not tableName in jsonOfThisTable):
                    jsonOfThisTable[tableName] = {}

                if('ispk' in element.keys()):
                    uniqueID = fake.unique.bothify(
                        element["format"], element["letters"])

                    actualRecord.append(str(uniqueID))
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
                        dataCell = fake.botify(
                            element["format"], element["letters"])
                        actualRecord.append(str(dataCell))

                    elif ('parameters' in element.keys()):
                        listOfParameters = element["parameters"]
                        actualRecord.append(GetRandomValueFaker(fakeType, fake, listOfParameters))

                elif ('isfk' in element.keys()):
                    sourceTable = element["sourceTable"]
                    sourceField = element["sourceField"]

                    randomPK = GetRandomPkOrFk(
                        jsonVariable, sourceTable, sourceField)
                    actualRecord.append(str(randomPK))

            tableRecords += ",".join(map(str, actualRecord))+"\n"
            actualRecord.clear()
            jsonVariable.update(jsonOfThisTable)
            counter += 1

            if counter == 5000:
                PMS(f"## Registers Created: {number+1}")
                counter = 0
    except Exception as e:
        PMS(f'Error getting the list of values of the "Data" field of {tableName}')
        PMS(f'Exception: {e}')
    finally:
        PMS(f"## Total Registers Created: {number+1}")
        return tableRecords, jsonVariable
