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
from Modules.Message_Mod.Message import Messenger
from GetData_Mod import GetData as GD


def CreateData(JSON_ALL_TABLES: dict, jsonRecord:dict, dataSetName:str, sqlStatement:bool) -> bool:
    """[summary]
    Creates the data for a file.
    Args:
        JSON_ALL_TABLES (dict): [Dictionary with all the tables and their columns]
        jsonRecord (dict): [Json that contains all the pk and fk of the tables]
        dataSetName (str): [Name of the dataset that will be created]
        sqlStatement (bool): [Boolean state that indicates if the data will be created for SQL or not]
    Returns:
        bool: [True if the file was created successfully or False if it wasn't]
    """
    msn = Messenger()
    success = False
    for tableName in JSON_ALL_TABLES:
        if (not tableName in jsonRecord.keys()):
            msn.print_message(f"Obtaining the amount of registers for table: {tableName}")
            amountOfRegisters = GD.GetAmountOfRegisters(JSON_ALL_TABLES, tableName)
            msn.print_message(
                f"Registers for {tableName}: {amountOfRegisters}", 
                f"Generating data for {tableName}",
                "This may taking a while, bassed on the",
                "Amount of registers and amount of columns"
            )
            dataMockRecord, actualTableDictionary = GD.CreateRecords(JSON_ALL_TABLES, tableName, amountOfRegisters, jsonRecord, sqlStatement)
            jsonRecord = actualTableDictionary
        if(sqlStatement):
            msn.print_message(f"Creating SQL file for {tableName}")
            FH.WriteSQL(dataMockRecord, dataSetName, tableName)
            success = True
        else:
            msn.print_message(f"Creating CSV file for {tableName}")
            FH.WriteCSV(dataMockRecord, dataSetName, tableName)
            success = True
    return success

def CreateRegisterForCSV(JSON_ALL_TABLES: dict, jsonRecord:dict, dataSetName:str, sqlStatement:bool):
    """[summary]
    Creates a csv file with the data
    Args:
        JSON_ALL_TABLES (dict): [Dictionary with all the tables and their columns]
        jsonRecord (dict): [Json that contains all the pk and fk of the tables]
        dataSetName (str): [Name of the dataset that will be created]
        sqlStatement (bool): [Boolean state that indicates if the data will be created for SQL or not]
    Returns:
        bool: [True if the file was created successfully or False if it wasn't]
    """
    return CreateData(JSON_ALL_TABLES, jsonRecord, dataSetName, sqlStatement)

def CreateRegisterForSQL(JSON_ALL_TABLES: dict, jsonRecord:dict, dataSetName:str, sqlStatement:bool):
    """[summary]
    Creates a sql file with the data and the tables
    Args:
        JSON_ALL_TABLES (dict): [Dictionary with all the tables and their columns]
        jsonRecord (dict): [Json that contains all the pk and fk of the tables]
        dataSetName (str): [Name of the dataset that will be created]
        sqlStatement (bool): [Boolean state that indicates if the data will be created for SQL or not]
    Returns:
        bool: [True if the file was created successfully or False if it wasn't]
    """
    return CreateData(JSON_ALL_TABLES, jsonRecord, dataSetName, sqlStatement)

