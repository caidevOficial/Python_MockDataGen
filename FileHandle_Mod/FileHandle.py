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


def SingleMessage(message: str) -> None:
    """[summary]
    Prints a formatted message, receiving a string as a parameter.
    Args:
        message (str): [Message to show in the console.]
    """
    print("######################################################")
    print(f'###     {message}')
    print("######################################################\n")

def DoubleMessage(message1: str, message2: str) -> None:
    """[summary]
    Prints a formatted message, receiving two strings as a parameter.
    Args:
        message1 (str): [First Message to show in the console.]
        message2 (str): [Second Message to show in the console.]
    """
    print("######################################################")
    print(f'###     {message1}')
    print(f'###     {message2}')
    print("######################################################\n")


def OpenFile(abspath: str) -> dict:
    """[summary]
    Opens the file specified in 'abspath'.
    Args:
        abspath (str): The path with the name of the file to open.

    Returns:
        [dict]: [The json parsed with the configuration of the tables inside.]
    """
    try:
        SingleMessage(f'Trying to open {abspath}')
        with open(abspath, 'r+') as schemafile:
            TABLE_FIELDS = json.load(schemafile)
            print("Success: File Opened!")
    except Exception as e:
        TABLE_FIELDS = {}
        DoubleMessage(f'\nError opening the file {abspath}','An empty dictionary will be returned.')
        SingleMessage(f"\nException: {e}")

    return TABLE_FIELDS


def WriteJSON(myDict: dict, datasetName: str, jsonFileNameToSave: str) -> None:
    """
    Writes and creates a file with format json.
    Args:
        myDict (dict): A dictionary with the data of the json to create.
        fileName (str): The name of the final File.
    """
    formatJSON = f"{datasetName}.{jsonFileNameToSave}"

    try:
        SingleMessage(f'Trying write the file {formatJSON}')
        with open(formatJSON, 'w+') as jsonFile:
            jsonFile.write(json.dumps(myDict, sort_keys=True, indent=4, separators=(',', ':')))
            jsonFile.close()
            SingleMessage('Success: Json file created!')
    except Exception as e:
        SingleMessage('\nError: The json could not be written')
        SingleMessage(f"\nException: {e}")


def WriteCSV(myList: list, datasetName: str, tableName: str) -> None:
    """
    Writes and creates a file with format csv.
    Args:
        myList (list): A list with all the registers inside.
        tableName (str): Name of the table with all the registers to make the file.
    """
    formatCSV = f"{datasetName}.{tableName}.csv"

    try:
        SingleMessage(f'Trying write the file {formatCSV}')
        with open(formatCSV, 'w+') as csvFile:
            csvFile.write(str(myList))
            csvFile.close()
            SingleMessage('Success: CSV file created!')
    except Exception as e:
        SingleMessage('\nError: The CSV could not be written')
        SingleMessage(f"\nException: {e}")


def SortFiles(exceptedFile: str, datasetName: str,directoryOfCSV:str, directoryOfJson:str, currentDir:str) -> bool:
    """ 
    Moves the files with format json and csv (except the configuration's json) to two directories, one for all the json and the other for the csv.
    Args:
        exceptedFile (str): File of tables's configuration (json)
        currentDir ([type]): Current directory with the files.
    """
    moveFiles = False
    try:
        SingleMessage(f'Trying read files in {currentDir}.')

        for filename in os.listdir(currentDir):
            if filename.endswith('.csv'):
                directory = f'{datasetName}.{directoryOfCSV}'
                if not os.path.exists(directory):
                    os.makedirs(directory)
                shutil.move(filename, directory)
                SingleMessage(f'Success: {filename} moved to {directory}.')

            if not filename.startswith(exceptedFile) and filename.endswith('.json') and (not filename.startswith('Configurations')):
                directory = f'{datasetName}.{directoryOfJson}'
                if not os.path.exists(directory):
                    os.makedirs(directory)
                shutil.move(filename, directory)
                SingleMessage(f'Success: {filename} moved to {directory}.')
                moveFiles = True
    except Exception as e:
        SingleMessage(f'\nError: Reading of {currentDir} has failed.')
        SingleMessage(f"\nException: {e}")
    finally:
        return moveFiles
