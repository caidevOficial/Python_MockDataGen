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

import Modules.FileHandle_Mod.FileHandle as FH
import Modules.SearchIfExist_Mod.Search as SF
from Modules.CreateRegisters_Mod.DataCreation import CreateRegisterForCSV as CSV
from Modules.CreateRegisters_Mod.DataCreation import CreateRegisterForSQL as SQL
from Modules.FileHandle_Mod.FileHandle import DoubleMessage as PMD
from Modules.FileHandle_Mod.FileHandle import SingleMessage as PMS
from Modules.GetConfigs_Mod.GetConfigsPython import ScriptConfigurator as GCP
from Modules.Statistics_Mod.Statistics import CountRegisters as CR
from Modules.Statistics_Mod.Statistics import FormatAmountRegisters as FAR
from Modules.Statistics_Mod.Statistics import TimeFormatted as TF

################################ SETUP AREA ################################
configurator = GCP(os.path.dirname(os.path.realpath(__file__)))
################################ SETUP AREA ################################

def MockDataGenerator() -> None:
    """[summary]
    Creates Files in csv with the data generated and a Json with the tables and its pk values inside.
    """
    jsonRecord = {}
    try:
        jsonRecord = SF.SearchIfExist(jsonRecord, configurator.getCurrentDir(), configurator.getDatasetName(), configurator.getJSONDirectory(), configurator.getJSONFileName())
        JSON_ALL_TABLES = FH.OpenFile(configurator.getAbsolutePathOfConfigFile())

        if(configurator.isSql()):
            SQL(JSON_ALL_TABLES, jsonRecord, configurator.getDatasetName(), configurator.isSql())
        else:
            CSV(JSON_ALL_TABLES, jsonRecord, configurator.getDatasetName(), configurator.isSql())

        PMS(f"Creating JSON file for {configurator.getDatasetName()}")
        ################
        totalRecords = CR(jsonRecord)
        amountRegisters = FAR(totalRecords)

        ##############
        FH.WriteJSON(jsonRecord, configurator.getDatasetName(), configurator.getJSONFileName())

        PMS("Moving Files...")
        FH.SortFiles(configurator.getNameConfigOfDataset(), configurator.getDatasetName(), configurator.getCSVDirectory(), configurator.getJSONDirectory(), configurator.getSQLDirectory(),configurator.getCurrentDir())
        PMD(f'{configurator.getScriptName()} - {configurator.getScriptVersion()}','Finished Successfully!.')
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
