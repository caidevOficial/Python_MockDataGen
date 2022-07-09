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

import FileHandle_Mod.FileHandle as FH

class ScriptConfigurator():
    """[summary]
    Configurator class of the DataMock Generator Script.
    Returns:
        [class]: [This object gets all the information from the Configurations.json file]
    """
    _currentDir = ''
    _configFile = {}
    _scriptName = "MockData Generator"
    _version = "v3.2.11"

    def __init__(self, dir:str) -> None:
        """[summary]
        Constructor of the class.
        Args:
            dir (str): [the absolute path of the directory where the script is located]
        """
        self._configFile = FH.OpenFile('Configurations.json')
        self.setMainPath(dir)

    def setMainPath(self, path:str)->None:
        """[summary]
        Sets the main path of the script.
        Args:
            path (str): [the path of the main directory of the script]
        """
        self._currentDir = path

    def getScriptNameAndVersion(self)->str:
        """[summary]
        Gets the name and version of the script.
        Returns:
            [str]: [the name and version of the script as a string]
        """
        return f'{self.getScriptName()} {self.getScriptVersion()}'

    def getScriptVersion(self)->str:
        """[summary]
        Gets the version of the script.
        Returns:
            [str]: [the version of the script as a string]
        """
        return self._version

    def getScriptName(self)->str:
        """[summary]
        Gets the name of the script.
        Returns:
            [str]: [the name of the script as a string]
        """
        return self._scriptName

    def getJSONFileName(self)->str:
        """[summary]
        Gets the name of the JSON file to save all the created pks.
        Returns:
            [str]: [the name of the JSON file as a string]
        """
        return self._configFile['Configurations']['NameOfDatasetToSaveInJson']

    def isSql(self)->bool:
        """[summary]
        Checks if the configuration file is in SQL format.
        Returns:
            bool: [True if the configuration file is in SQL format, False otherwise]
        """
        return self._configFile['Configurations']['SQL_Format']

    def getCSVDirectory(self)->str:
        """[summary]
        Gets the absolute path of the directory where the CSV files will be saved.
        Returns:
            [str]: [the absolute path of the directory where the CSV files will be saved as a string]
        """
        return self._configFile['Configurations']['Directory_To_Save_csvFiles']

    def getSQLDirectory(self)->str:
        """[summary]
        Gets the absolute path of the directory where the SQL files will be saved.
        Returns:
            [str]: [the absolute path of the directory where the SQL files will be saved as a string]
        """
        return self._configFile['Configurations']['Directory_To_Save_sqlFiles']

    def getJSONDirectory(self)->str:
        """[summary]
        Gets the absolute path of the directory where the JSON files will be saved.
        Returns:
            [str]: [the absolute path of the directory where the JSON files will be saved as a string]
        """
        return self._configFile['Configurations']['Directory_To_Save_jsonFiles']

    def getDatasetName(self)->str:
        """[summary]
        Gets the name of the dataset.
        Returns:
            str: [the name of the dataset as a string]
        """
        return self._configFile['Configurations']['DatasetName']

    def getNameConfigOfDataset(self)->str:
        """[summary]
        Gets the name of the dataset's configuration file.
        Returns:
            str: [the name of the dataset's configuration file as a string]
        """
        return self._configFile['Configurations']['DatasetFileToOpen']

    def getAbsolutePathOfConfigFile(self)->str:
        """[summary]
        Gets the absolute path of the configuration file.
        Returns:
            [str]: [the absolute path of the configuration file as a string]
        """
        return self.getNameConfigOfDataset()

    def getCurrentDir(self)->str:
        """[summary]
        Gets the current directory of the script.
        Returns:
            [str]: [the current directory of the script as a string]
        """
        return self._currentDir