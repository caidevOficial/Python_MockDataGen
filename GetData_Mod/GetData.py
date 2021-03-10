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

from faker import Faker as fk
import random


def mySwitch(fakeType: str, fake: fk):
    """[summary]

    Args:
        fakeType (str): [description]
        fake (fk): [description]

    Returns:
        [type]: [description]
    """
    fakeAttr = 'name'

    try:
        fakeFunc = getattr(fake, fakeType)
    except:
        return getattr(fake, fakeAttr)

    return fakeFunc


def getAmountOfRegisters(TABLE_DATA_Fields: dict, tableName: str):
    """[summary]

    Args:
        TABLE_DATA_Fields (dict): [description]
        tableName (str): [description]
    """

    amountOfRegisters = 1000

    try:
        listMetadata = TABLE_DATA_Fields[tableName]["MetaData"]
        for index in range(0, len(listMetadata)):
            if("RegisterQtty" in listMetadata[index]):
                amountOfRegisters = listMetadata[index]["RegisterQtty"]
                break
    except:
        print(
            f'Error in obtaining the amount of registers. The default value was set to {amountOfRegisters}.')

    return amountOfRegisters


def getRandomPkOrFk(listOfPk: dict, sourceTable: str, sourceField: str):
    """[summary]

    Args:
        listOfPk (dict): [description]
        sourceTable (str): [description]
        sourceField (str): [description]
    """

    try:
        listOfValues = listOfPk[sourceTable][sourceField]
        randomPk = random.choice(listOfValues)
    except:
        randomPk = []
        print(
            f'Error getting the list of pk from the table {sourceTable}. An empty list will be returned')

    return randomPk


def createRecords(TABLE_FIELDS: list, tableName: str, amountOfRegisters: int, jsonVariable: dict):
    """[summary]

    Args:
        TABLE_FIELDS (list): [description]
        tableName (str): [description]
        amountOfRegisters (int): [description]
        jsonVariable (dict): [description]
    """

    tableRecords = ""
    actualRecord = []
    listOfValues = []
    pksOfThisTable = []
    jsonOfThisTable = {}
    fake = fk()

    print(
        f'Creating registers for the table {tableName}, this action may taking a while...')

    for number in range(0, amountOfRegisters):
        try:
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
                        values = list(jsonOfThisTable[tableName][columnName])
                        values.append(uniqueID)
                        jsonOfThisTable[tableName][columnName] = values

                elif ('faketype' in element.keys()):
                    fakeType = element["faketype"]
                    actualRecord.append(mySwitch(fakeType, fake)())

                elif ('isfk' in element.keys()):
                    sourceTable = element["sourceTable"]
                    sourceField = element["sourceField"]

                    randomPK = getRandomPkOrFk(
                        jsonVariable, sourceTable, sourceField)
                    actualRecord.append(str(randomPK))

            tableRecords += ",".join(map(str, actualRecord)) + "\n"
            actualRecord.clear()
            jsonVariable.update(jsonOfThisTable)
        except:
            print(
                f'Error getting the list of values of the "Data" field of {tableName}')

    return tableRecords, jsonVariable
