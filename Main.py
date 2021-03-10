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

import GetData_Mod.GetData as GD
import FileHandle_Mod.FileHandle as FH
import os

# SETUP
scriptName = "DataMock Generator"
version = "v2.8.1"
filename = "file.json"
dirName = ""
absDir = dirName + filename
currentDir = os.path.dirname(os.path.realpath(__file__))


def dataMockGenerator():
    """[summary]
    Abre un json con la estructura de la tablas, genera la mock y lo guarda en csv, tmb guarda las pk de cada tabla en un json.
    """

    jsonRecord = {}
    dataMockRecord = []
    try:
        TABLE_DATA_FIELDS = FH.openFile(absDir)

        for tableName in TABLE_DATA_FIELDS:
            amountOfRegisters = GD.getAmountOfRegisters(
                TABLE_DATA_FIELDS, tableName)
            dataMockRecord, actualTableDictionary = GD.createRecords(
                TABLE_DATA_FIELDS, tableName, amountOfRegisters, jsonRecord)
            jsonRecord = actualTableDictionary

            FH.writeCSV(dataMockRecord, tableName)
        FH.writeJSON(jsonRecord, 'Pks_Of_Tables')
        FH.sortFiles(filename, currentDir)
        print(f'\n{scriptName} - {version} Finished Successfully!.\n')
    except RuntimeError:
        print("Error: Try to run again.")


# Test
if __name__ == "__main__":
    dataMockGenerator()
