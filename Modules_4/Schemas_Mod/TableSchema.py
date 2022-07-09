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

class TableSchema:

    _table_name: str = None
    _table_dataset: str = None
    _table_metadata: dict = {}
    _table_columns_data: list = [dict]
    _table_columns_names: list = [str]

    def __init__(self):
        pass

    @property
    def Table_Dataset(self):
        return self._table_dataset
    
    @Table_Dataset.setter
    def Table_Dataset(self, table_dataset: str):
        self._table_dataset = table_dataset

    @property
    def Table_Name(self) -> str:
        return self._table_name
    
    @Table_Name.setter
    def Table_Name(self, table_name: str) -> None:
        self._table_name = table_name
    
    @property
    def Metadata(self) -> dict:
        return self._table_metadata[0]
    
    @Metadata.setter
    def Metadata(self, table_metadata: list) -> None:
        self._table_metadata = table_metadata[0]
    
    @property
    def Columns_Data(self) -> list:
        return self._table_columns_data
    
    @Columns_Data.setter
    def Columns_Data(self, table_columns: list) -> None:
        self._table_columns_data = table_columns
    
    @property
    def Columns_Names(self) -> list:
        return self._table_columns_names
    
    @Columns_Names.setter
    def Columns_Names(self, table_columns_names: list) -> None:
        self._table_columns_names = table_columns_names
    
    def __str__(self):
        return f"{self.Table_Dataset}.{self.Table_Name}"
    
    def Columns_Names_to_string(self) -> str:
        return ",".join(self.Columns_Names)
