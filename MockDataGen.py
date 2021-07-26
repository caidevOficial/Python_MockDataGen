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

import os
from time import time

import FileHandle_Mod.FileHandle as FH
import SearchIfExist_Mod.Search as SF
from FileHandle_Mod.FileHandle import DoubleMessage as PMD
from FileHandle_Mod.FileHandle import SingleMessage as PMS
from GetData_Mod import GetData as GD

################################ SETUP AREA ################################
configFile = FH.OpenFile('Configurations.json')
dataSetName = configFile['Configurations']['DatasetName']

jsonConfigTables = configFile['Configurations']['DatasetFileToOpen']
jsonFinalName = configFile['Configurations']['NameOfDatasetToSaveInJson']

directoryToSaveCSV = configFile['Configurations']['Directory_To_Save_csvFiles']
directoryToSaveJSON = configFile['Configurations']['Directory_To_Save_jsonFile']

currentDir = os.path.dirname(os.path.realpath(__file__))
absDir = jsonConfigTables
scriptName = "DataMock Generator"
version = "v3.0.44"
################################ SETUP AREA ################################


def MockDataGenerator() -> None:
    """[summary]
    Creates Files in csv with the data generated and a Json with the tables and its pk values inside.
    """
    jsonRecord = {}
    dataMockRecord = []
    try:
        jsonRecord = SF.SearchIfExist(jsonRecord, currentDir, dataSetName, directoryToSaveJSON, jsonFinalName)
        TABLE_DATA_FIELDS = FH.OpenFile(absDir)

        for tableName in TABLE_DATA_FIELDS:
            if (not tableName in jsonRecord.keys()):
                PMS(
                    f"Obtaining the amount of registers for table: {tableName}")
                amountOfRegisters = GD.GetAmountOfRegisters(TABLE_DATA_FIELDS, tableName)
                PMD(f"Registers for {tableName}: {amountOfRegisters}",
                    f"Generating data for {tableName}")
                PMD("This may taking a while, bassed on the",
                    "Amount of registers and amount of columns")
                dataMockRecord, actualTableDictionary = GD.CreateRecords(TABLE_DATA_FIELDS, tableName, amountOfRegisters, jsonRecord)
                jsonRecord = actualTableDictionary

            PMS(f"Creating CSV file for {tableName}")
            FH.WriteCSV(dataMockRecord, dataSetName, tableName)

        PMS(f"Creating JSON file for {dataSetName}")
        FH.WriteJSON(jsonRecord, dataSetName, jsonFinalName)

        PMS("Moving Files...")
        FH.SortFiles(jsonConfigTables, dataSetName, directoryToSaveCSV, directoryToSaveJSON, currentDir)
        PMS(f'{scriptName} - {version} Finished Successfully!.')
    except Exception as e:
        PMS("Error: Try to run again.")
        PMS(f"Exception: {e}")


################################# TEST AREA ################################
if __name__ == "__main__":
    start_time = time()
    MockDataGenerator()
    elapsed_time = time() - start_time
    elapsed_time = round(elapsed_time, 4)
    PMS(f"Elapsed Time: {elapsed_time} seconds")
    PMS("Success! All task done. Press a key to close the app")
    end = input()
