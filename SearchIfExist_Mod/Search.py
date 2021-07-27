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

from FileHandle_Mod import FileHandle as FH

def SearchIfExist(jasonDictionary: dict, currentDir: str, dataSetName: str, dirNameJSONFiles: str, jsonFinalName: str) -> dict:
    """[summary]
    Tries to open a file with the name of the current directory and the name of the dataset. 
    If not exist, returns an empty dictionary.
    Args:
        jasonDictionary (dict): [Dictionary to be updated with the data from the file]
        currentDir (str): [Current directory of the executable]
        dataSetName (str): [First Part of the name of the folder/file that contains the JSON files]
        dirNameJSONFiles (str): [Second Part of the name of the folder that contains the JSON files]
        jsonFinalName (str): [Second part of the name of the JSON file that contains the data]
    Returns:
        dict: [An empty dictionary if fails to open the file, otherwise, the dictionary is returned]
    """
    try:
        searchExistantJson = f"{currentDir}\\{dataSetName}.{dirNameJSONFiles}\\{dataSetName}.{jsonFinalName}"
        jasonDictionary = FH.openFile(searchExistantJson)
    except FileNotFoundError as e:
        FH.printMessageS("File not found")
        print(f"Exception: {e}")
    finally:
        return jasonDictionary
