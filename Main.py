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

from time import time
import GetData_Mod.GetData as GD
import FileHandle_Mod.FileHandle as FH
import SearchIfExist_Mod as SF
from FileHandle_Mod.FileHandle import printMessageS as PMS, printMessageD as PMD
import os

################################ SETUP AREA ################################
configFile = FH.openFile('Configurations.json')
dataSetName = configFile['Configurations']['DatasetName']

jsonConfigTables = configFile['Configurations']['DatasetFileToOpen']
jsonFinalName = configFile['Configurations']['NameOfDatasetToSaveInJson']

directoryToSaveCSV = configFile['Configurations']['Directory_To_Save_csvFiles']
directoryToSaveJSON = configFile['Configurations']['Directory_To_Save_jsonFile']

currentDir = os.path.dirname(os.path.realpath(__file__))
absDir = jsonConfigTables
scriptName = "DataMock Generator"
version = "v3.0.4"
################################ SETUP AREA ################################


def dataMockGenerator() -> None:
    """
    Creates Files in csv with the data generated and a Json with the tables and its pk values inside.
    """
    jsonRecord = {}
    dataMockRecord = []
    try:
        jsonRecord = SF.searchIfExist(jsonRecord, currentDir, dataSetName, directoryToSaveJSON, jsonFinalName)
        TABLE_DATA_FIELDS = FH.openFile(absDir)

        for tableName in TABLE_DATA_FIELDS:
            if (not tableName in jsonRecord.keys()):
                PMS(f"Obtaining the amount of registers for table: {tableName}")
                amountOfRegisters = GD.getQtyRegisters(TABLE_DATA_FIELDS, tableName)
                PMD(f"Registers for {tableName}: {amountOfRegisters}", f"Generating data for {tableName}")
                PMD("This may taking a while, bassed on the","Amount of registers and amount of columns")
                dataMockRecord, actualTableDictionary = GD.createRecords(TABLE_DATA_FIELDS, tableName, amountOfRegisters, jsonRecord)
                jsonRecord = actualTableDictionary

            PMS(f"Creating CSV file for {tableName}")
            FH.writeCSV(dataMockRecord, tableName)

        PMS(f"Creating JSON file for {dataSetName}")
        FH.writeJSON(jsonRecord, 'Pks_Of_Tables')

        PMS("Moving Files...")
        FH.sortFiles(jsonConfigTables, dataSetName, directoryToSaveCSV, directoryToSaveJSON, currentDir)
        PMS(f'\n{scriptName} - {version} Finished Successfully!.\n')
    except Exception as e:
        PMS("Error: Try to run again.")
        PMS(f"Exception: {e}")


################################# TEST AREA ################################
if __name__ == "__main__":
    start_time = time()
    dataMockGenerator()
    elapsed_time = time() - start_time
    elapsed_time = round(elapsed_time, 4)
    PMS(f"Elapsed Time: {elapsed_time} seconds")
    PMS("Success! All task done. Press a key to close the app")
    ent = input()
