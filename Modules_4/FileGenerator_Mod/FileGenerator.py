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

from io import StringIO
import pandas as pd


class FileGenerator:
    _file_str: str = None
    _counter: int = None
    _file_type: str = None
    _filename: str = None
    _dataframe: pd.DataFrame = None
    _header: bool = False

    # ?### Magic Functions: Start ###

    def __init__(self, file_type: str):
        self._file_str = StringIO()
        self.File_Type = file_type
    
    def __del__(self):
        """[summary]\n
        Delete the string builder.\n
        """
        self._file_str.close()
    
    def __iter__(self):
        self.Counter = 0
        return self
    
    def __next__(self):
        if self.Counter < self.Length_List:
            self.Counter += 1
            return self.String_Value.split('\n')[self.Counter - 1]
        else:
            raise StopIteration

    # ?### Magic Functions: End ###

    @property
    def Header(self):
        """[summary]\n
        Get the boolean status if can write the header of the file.\n
        """
        return self._header
    
    @Header.setter
    def Header(self, value: bool):
        """[summary]\n
        Set the boolean status if can write the header of the file.\n
        Args:
            value (bool): [Boolean status]\n
        """
        self._header = value

    @property
    def Filename(self) -> str:
        """[summary]\n
        Get the filename.\n
        """
        return self._filename
    
    @Filename.setter
    def Filename(self, filename: str):
        """[summary]\n
        Set the filename.\n
        Args:
            filename (str): [Filename]\n
        """
        self._filename = filename

    @property
    def Dataframe(self) -> str:
        """[summary]\n
        Get the Dataframe.\n
        """
        return self._dataframe
    
    @Dataframe.setter
    def Dataframe(self, value: pd.DataFrame):
        """[summary]\n
        Set the Dataframe.\n
        Args:
            value (str): [Value to be set]\n
        """
        self._dataframe = value

    @property
    def File_Type(self):
        """[summary]\n
        Get the file type.\n
        """
        return self._file_type
    
    @File_Type.setter
    def File_Type(self, file_type: str):
        """[summary]\n
        Set the file type.\n
        Args:
            file_type (str): [File type]\n
        """
        self._file_type = file_type.lower()

    @property
    def Counter(self) -> int:
        """[summary]\n
        Get the counter of the string builder.\n
        Returns:
            [int]: [Counter of the string builder]\n
        """
        return self._counter
    
    @property
    def String_Value(self) -> str:
        """[summary]\n
        Get the string value of the string builder.\n
        Returns:
            [str]: [String value of the string builder]\n
        """
        return self._file_str.getvalue()
    
    @property
    def Length(self) -> int:
        """[summary]\n
        Get the length of the string builder.\n
        Returns:
            [int]: [Length of the string builder]\n
        """
        return self.__len__()

    @property
    def Length_List(self) -> list:
        """[summary]\n
        Get the amount of lines of the StringBuilder.\n
        Returns:
            [list]: [Amount of lines of the StringBuilder in a list]\n
        """
        return len(self.String_Value.split('\n'))
    
    @Counter.setter
    def Counter(self, value: int):
        """[summary]\n
        Set the counter of the string builder.\n
        Args:
            value (int): [Counter to be set]\n
        """
        self._counter = value

    def Write_File(self):
        if self.File_Type == 'csv':
            self.Dataframe.to_csv(self.Filename, sep=',', chunksize=None, index=False, header=self.Header)
            self.Header = False
        elif self.File_Type == 'json':
            self.Dataframe.to_json(self.Filename, orient='records', lines=True)


    def Append(self, text: str = None):
        """[summary]\n
        Append a text to the string builder in the same line.\n
        Args:
            text (str, optional): [Test to be appended]\n
        """
        if not text is None:
            self._file_str.write(text)
        else:
            self._file_str.write('')
    
    def AppendLine(self, text: str = None):
        """[summary]\n
        Append a text to the string builder in a new line.\n
        Args:
            text (str, optional): [Test to be appended]\n
        """
        if not text is None:
            self.Append(f'{text}\n')
        else:
            self.Append('\n')
    
    def Clear(self):
        """[summary]\n
        Clear the string builder.\n
        """
        self._file_str.close()
        self._file_str = StringIO()