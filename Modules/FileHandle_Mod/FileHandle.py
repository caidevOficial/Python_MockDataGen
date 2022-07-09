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

import json
import os
import shutil
from Modules.Message_Mod.Message import Messenger

def OpenFile(abspath: str) -> dict:
    """[summary]
    Opens the file specified in 'abspath'.
    Args:
        abspath (str): The path with the name of the file to open.
    Returns:
        [dict]: [The json parsed with the configuration of the tables inside.]
    """
    msn = Messenger()
    try:
        msn.print_message(f'Trying to open {abspath}')
        with open(abspath, 'r+') as schemafile:
            TABLE_FIELDS = json.load(schemafile)
            print("Success: File Opened!")
    except Exception as e:
        TABLE_FIELDS = {}
        msn.print_message(
            f'Error opening the file {abspath}',
            'An empty dictionary will be returned.',
            f'Exception: {e}'
        )
        
    return TABLE_FIELDS


def WriteJSON(myDict: dict, datasetName: str, jsonFileNameToSave: str) -> None:
    """
    Writes and creates a file with format json.
    Args:
        myDict (dict): A dictionary with the data of the json to create.
        fileName (str): The name of the final File.
    """
    msn = Messenger()
    formatJSON = f"{datasetName}.{jsonFileNameToSave}"
    try:
        msn.print_message(f'Trying write the file {formatJSON}')
        with open(formatJSON, 'w+') as jsonFile:
            jsonFile.write(json.dumps(myDict, sort_keys=True, indent=4, separators=(',', ':')))
            jsonFile.close()
            msn.print_message('Success: Json file created!')
    except Exception as e:
        msn.print_message(
            'Error: The json could not be written',
            f'Exception: {e}'
        )

def WriteCSV(myList: list, datasetName: str, tableName: str) -> None:
    """
    Writes and creates a file with format csv.
    Args:
        myList (list): A list with all the registers inside.
        tableName (str): Name of the table with all the registers to make the file.
    """
    msn = Messenger()
    formatCSV = f"{datasetName}.{tableName}.csv"
    try:
        msn.print_message(f'Trying write the file {formatCSV}')
        with open(formatCSV, 'w+') as csvFile:
            csvFile.write(str(myList))
            csvFile.close()
            msn.print_message('Success: CSV file created!')
    except Exception as e:
        msn.print_message(
            'Error: The CSV could not be written',
            f'Exception: {e}'
        )
        

def WriteSQL(myListOfQuerys: list, datasetName: str, tableName: str) -> None:
    """
    Writes and creates a file with format sql.
    Args:
        myList (list): A list with all the registers inside.
        tableName (str): Name of the table with all the registers to make the file.
    """
    msn = Messenger()
    formatSQL = f"{datasetName}.{tableName}.sql"
    try:
        msn.print_message(f'Trying write the file {formatSQL}')
        with open(formatSQL, 'w+') as sqlFile:
            sqlFile.write(str(myListOfQuerys))
            sqlFile.close()
            msn.print_message('Success: SQL file created!')
    except Exception as e:
        msn.print_message(
            'Error: The SQL could not be written',
            f'Exception: {e}'
        )
        

def SortSingleFile(filename:str, formatFile:str, datasetName: str,directoryToSave:str, moved:bool) -> bool:
    """[summary]
    Moves a single file to a directory.
    Args:
        filename (str): [Name of the file to be moved.]
        formatFile (str): [Format extension of the file to be moved.]
        datasetName (str): [Name of the dataset to be used in the directory to be created.]
        directoryToSave (str): [Name of the directory to save the file.]
        moved (bool): [Boolean state that indicates if the file has been moved or not.]
    Returns:
        bool: [True if the file was moved, False otherwise.]
    """
    msn = Messenger()
    if filename.endswith(f'.{formatFile}'):
        directory = f'{datasetName}.{directoryToSave}'
        if not os.path.exists(directory):
            os.makedirs(directory)
        shutil.move(filename, directory)
        msn.print_message(f'Success: {filename} moved to {directory}.')
        moved = True
    return moved


def SortFiles(exceptedFile: str, datasetName: str,directoryOfCSV:str, directoryOfJson:str, directoryOfSQL:str, currentDir:str) -> bool:
    """ 
    Moves the files with format json and csv (except the configuration's json) to two directories, one for all the json and the other for the csv.
    Args:
        exceptedFile (str): File of tables's configuration (json)
        currentDir ([type]): Current directory with the files.
    Returns:
        bool: [True if the specified files was moved, False otherwise.]
    """
    msn = Messenger()
    moveFiles = False
    try:
        msn.print_message(f'Trying read files in {currentDir}.')
        for filename in os.listdir(currentDir):
            if (not filename.endswith("Configurations.json") and (not filename.endswith(f"{exceptedFile}"))):
                moveFiles = SortSingleFile(filename, 'csv', datasetName, directoryOfCSV, moveFiles)
                moveFiles = SortSingleFile(filename, 'json', datasetName, directoryOfJson, moveFiles)
                moveFiles = SortSingleFile(filename, 'sql', datasetName, directoryOfSQL, moveFiles)
    except Exception as e:
        msn.print_message(
            f'Error: Reading of {currentDir} has failed.',
            f'Exception: {e}'
        )
    finally:
        return moveFiles
