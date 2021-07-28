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

import datetime
import os

import FileHandle_Mod.FileHandle as FH
import SearchIfExist_Mod.Search as SF
from CreateRegisters_Mod.DataCreation import CreateRegisterForCSV as CSV
from CreateRegisters_Mod.DataCreation import CreateRegisterForSQL as SQL
from FileHandle_Mod.FileHandle import SingleMessage as PMS
from Statistics_Mod.Statistics import CountRegisters as CR
from Statistics_Mod.Statistics import FormatAmountRegisters as FAR
from Statistics_Mod.Statistics import TimeFormatted as TF

################################ SETUP AREA ################################
configFile = FH.OpenFile('Configurations.json')
dataSetName = configFile['Configurations']['DatasetName']

jsonConfigTables = configFile['Configurations']['DatasetFileToOpen']
jsonFinalName = configFile['Configurations']['NameOfDatasetToSaveInJson']

directoryToSaveCSV = configFile['Configurations']['Directory_To_Save_csvFiles']
directoryToSaveJSON = configFile['Configurations']['Directory_To_Save_jsonFiles']
directoryToSaveSQL = configFile['Configurations']['Directory_To_Save_sqlFiles']
isSQL = configFile['Configurations']['SQL_Format']

currentDir = os.path.dirname(os.path.realpath(__file__))
absDir = jsonConfigTables
scriptName = "DataMock Generator"
version = "v3.1.2"
################################ SETUP AREA ################################

def MockDataGenerator() -> None:
    """[summary]
    Creates Files in csv with the data generated and a Json with the tables and its pk values inside.
    """
    jsonRecord = {}
    try:
        jsonRecord = SF.SearchIfExist(jsonRecord, currentDir, dataSetName, directoryToSaveJSON, jsonFinalName)
        JSON_ALL_TABLES = FH.OpenFile(absDir)

        if(isSQL):
            SQL(JSON_ALL_TABLES, jsonRecord, dataSetName, isSQL)
        else:
            CSV(JSON_ALL_TABLES, jsonRecord, dataSetName, isSQL)

        PMS(f"Creating JSON file for {dataSetName}")
        ################
        totalRecords = CR(jsonRecord)
        amountRegisters = FAR(totalRecords)

        ##############
        FH.WriteJSON(jsonRecord, dataSetName, jsonFinalName)

        PMS("Moving Files...")
        FH.SortFiles(jsonConfigTables, dataSetName, directoryToSaveCSV, directoryToSaveJSON, directoryToSaveSQL,currentDir)
        PMS(f'{scriptName} - {version} Finished Successfully!.')
        PMS(f'Total Records Created: {amountRegisters}')
    except Exception as e:
        PMS("Error: Try to run again.")
        PMS(f"Exception: {e}")

################################# TEST AREA ################################

if __name__ == "__main__":
    start_time = datetime.datetime.now()
    MockDataGenerator()
    elapsed_time = TF(start_time)
    PMS(f"Elapsed Time: {elapsed_time}")
    PMS("Success! All task done. Press a key to close the app")
    end = input()
