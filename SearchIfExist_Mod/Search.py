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

def searchIfExist(jasonDictionary: dict, currentDir: str, dataSetName: str, dirNameJSONFiles: str, jsonFinalName: str) -> dict:
    """
    Tries to open a file with the name of the current directory and the name of the dataset. 
    If not exist, returns an empty dictionary.
    """
    try:
        searchExistantJson = f"{currentDir}\\{dataSetName}.{dirNameJSONFiles}\\{dataSetName}.{jsonFinalName}"
        searchExistantJson = FH.openFile(searchExistantJson)
    except FileNotFoundError:
        print("File not found")
    finally:
        return jasonDictionary
