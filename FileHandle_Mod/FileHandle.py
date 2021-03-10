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

import json
import shutil
import os


def openFile(abspath: str):
    """[summary]

    Args:
        abspath (str): [description]
    """
    try:
        print(f'Trying to open {abspath}')
        with open(abspath, 'r+') as schemafile:
            TABLE_FIELDS = json.load(schemafile)
            print("Success: File Opened!")
    except:
        TABLE_FIELDS = {}
        print(
            f'Error opening the file {abspath}, an empty dictionary will be returned.')

    return TABLE_FIELDS


def writeJSON(myDict: dict, tableName: str):
    """[summary]

    Args:
        myDict (dict): [description]
        tableName (str): [description]
    """
    formatJSON = tableName + ".json"

    try:
        print(f'Trying write the file {formatJSON}')
        with open(formatJSON, 'w+') as jsonFile:
            jsonFile.write(json.dumps(myDict, sort_keys=True,
                                      indent=4, separators=(',', ':')))
            jsonFile.close()
            print('Success: Json file created!')
    except:
        print('Error: The json could not be written')


def writeCSV(myList: list, tableName: str):
    """[summary]

    Args:
        myList (list): [description]
        tableName (str): [description]
    """
    formatCSV = tableName + ".csv"

    try:
        print(f'Trying write the file {formatCSV}')
        with open(formatCSV, 'w+') as csvFile:
            csvFile.write(str(myList))
            csvFile.close()
            print('Success: CSV file created!')
    except:
        print('Error: The CSV could not be written')


def sortFiles(exceptedFile: str, currentDir):
    """[summary]

    Args:
        exceptedFile (str): [description]
        currentDir ([type]): [description]
    """
    try:
        print(f'\Trying read files in {currentDir}.')
        for filename in os.listdir(currentDir):
            if filename.endswith('.csv'):
                directory = 'CSV_Files'
                if not os.path.exists(directory):
                    os.makedirs(directory)
                shutil.copy(filename, directory)
                os.remove(filename)
                print(f'Success: {filename} moved to {directory}.')
            elif not filename.startswith(exceptedFile) and filename.endswith('.json'):
                directory = 'JSON_Files'
                if not os.path.exists(directory):
                    os.makedirs(directory)
                shutil.copy(filename, directory)
                os.remove(filename)
                print(f'Success: {filename} moved to {directory}.')
    except:
        print(f'Effor: Reading of {currentDir} has failed.')
