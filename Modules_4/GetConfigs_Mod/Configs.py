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
    _FILENAME = 'Configurations.json'
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
        self._configFile = FH.OpenFile(self.Filename)
        self.MainPath = dir

    @property
    def Filename(self) -> str:
        """[summary]
        Gets the name of the configuration file.
        Returns:
            [str]: [the name of the configuration file as a string]
        """
        return self._FILENAME

    @property
    def MainPath(self)->str:
        """[summary]
        Gets the main path of the script.
        Returns:
            [str]: [the main path of the script as a string]
        """
        return self._currentDir
    

    @MainPath.setter
    def MainPath(self, path:str)->None:
        """[summary]
        Sets the main path of the script.
        Args:
            path (str): [the path of the main directory of the script]
        """
        self._currentDir = path

    @property
    def Script_Version(self)->str:
        """[summary]
        Gets the version of the script.
        Returns:
            [str]: [the version of the script as a string]
        """
        return self._version
    
    @Script_Version.setter
    def Script_Version(self, version:str)->None:
        """[summary]
        Sets the version of the script.
        Args:
            version (str): [the version of the script as a string]
        """
        self._version = version

    @property
    def Script_Name(self)->str:
        """[summary]
        Gets the name of the script.
        Returns:
            [str]: [the name of the script as a string]
        """
        return self._scriptName
    
    @Script_Name.setter
    def Script_Name(self, name:str)->None:
        """[summary]
        Sets the name of the script.
        Args:
            name (str): [the name of the script as a string]
        """
        self._scriptName = name

    @property
    def JSON_File_Name(self)->str:
        """[summary]
        Gets the name of the JSON file to save all the created pks.
        Returns:
            [str]: [the name of the JSON file as a string]
        """
        return self._configFile['Configurations']['NameOfDatasetToSaveInJson']

    @property
    def CSV_Directory(self)->str:
        """[summary]
        Gets the absolute path of the directory where the CSV files will be saved.
        Returns:
            [str]: [the absolute path of the directory where the CSV files will be saved as a string]
        """
        return self._configFile['Configurations']['Directory_To_Save_csvFiles']

    @property
    def SQL_Directory(self)->str:
        """[summary]
        Gets the absolute path of the directory where the SQL files will be saved.
        Returns:
            [str]: [the absolute path of the directory where the SQL files will be saved as a string]
        """
        return self._configFile['Configurations']['Directory_To_Save_sqlFiles']

    @property
    def JSONDirectory(self)->str:
        """[summary]
        Gets the absolute path of the directory where the JSON files will be saved.
        Returns:
            [str]: [the absolute path of the directory where the JSON files will be saved as a string]
        """
        return self._configFile['Configurations']['Directory_To_Save_jsonFiles']

    @property
    def Dataset_Name(self)->str:
        """[summary]
        Gets the name of the dataset.
        Returns:
            str: [the name of the dataset as a string]
        """
        return self._configFile['Configurations']['DatasetName']

    @property
    def Name_Config_Dataset(self)->str:
        """[summary]
        Gets the name of the dataset's configuration file.
        Returns:
            str: [the name of the dataset's configuration file as a string]
        """
        return self._configFile['Configurations']['DatasetFileToOpen']

    @property
    def CurrentDir(self)->str:
        """[summary]
        Gets the current directory of the script.
        Returns:
            [str]: [the current directory of the script as a string]
        """
        return self._currentDir
    
    def ScriptNameAndVersion(self)->str:
        """[summary]
        Gets the name and version of the script.
        Returns:
            [str]: [the name and version of the script as a string]
        """
        return f'{self.Script_Name} {self.Script_Version}'

    def isSql(self)->bool:
        """[summary]
        Checks if the configuration file is in SQL format.
        Returns:
            bool: [True if the configuration file is in SQL format, False otherwise]
        """
        return self._configFile['Configurations']['SQL_Format']

    def Absolute_Path_Config_File(self)->str:
        """[summary]
        Gets the absolute path of the configuration file.
        Returns:
            [str]: [the absolute path of the configuration file as a string]
        """
        return self.Name_Config_Dataset
