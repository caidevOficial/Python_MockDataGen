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
    Opens the file specified in 'abspath'.
    Args:
        abspath (str): The path with the name of the file to open.

    Returns:
        [dict]: [The json parsed with the configuration of the tables inside.]
    """
    try:
        print(f'\nTrying to open {abspath}')
        with open(abspath, 'r+') as schemafile:
            TABLE_FIELDS = json.load(schemafile)
            print("Success: File Opened!")
    except:
        TABLE_FIELDS = {}
        print(
            f'\nError opening the file {abspath}, an empty dictionary will be returned.')

    return TABLE_FIELDS


def writeJSON(myDict: dict, fileName: str):
    """
    Writes and creates a file with format json.
    Args:
        myDict (dict): A dictionary with the data of the json to create.
        fileName (str): The name of the final File.
    """
    formatJSON = fileName + ".json"

    try:
        print(f'\nTrying write the file {formatJSON}')
        with open(formatJSON, 'w+') as jsonFile:
            jsonFile.write(json.dumps(myDict, sort_keys=True,
                                      indent=4, separators=(',', ':')))
            jsonFile.close()
            print('Success: Json file created!')
    except:
        print('\nError: The json could not be written')


def writeCSV(myList: list, tableName: str):
    """
    Writes and creates a file with format csv.
    Args:
        myList (list): A list with all the registers inside.
        tableName (str): Name of the table with all the registers to make the file.
    """
    formatCSV = tableName + ".csv"

    try:
        print(f'\nTrying write the file {formatCSV}')
        with open(formatCSV, 'w+') as csvFile:
            csvFile.write(str(myList))
            csvFile.close()
            print('Success: CSV file created!')
    except:
        print('\nError: The CSV could not be written')


def sortFiles(exceptedFile: str, currentDir):
    """ 
    Moves the files with format json and csv (except the configuration's json) to two directories, one for all the json and the other for the csv.
    Args:
        exceptedFile (str): File of tables's configuration (json)
        currentDir ([type]): Current directory with the files.
    """
    try:
        print(f'\nTrying read files in {currentDir}.')
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
        print(f'\nError: Reading of {currentDir} has failed.')
