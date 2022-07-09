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

from Modules_4.Message_Mod.Message import Messenger
from Modules_4.Schemas_Mod.TableSchema import TableSchema
from Modules_4.GetConfigs_Mod.Configs import ScriptConfigurator as SC
from Modules_4.FileHandle_Mod.FileHandle import OpenFile as Open

def setup_schema(configurator: SC, tableName: str):
    """[summary]
    Sets up the schema for the table
    Args:
        configurator (ScriptConfigurator): [ScriptConfigurator object]
        tableName (str): [Name of the table that will be created]
    Returns:
        TableSchema: [TableSchema object]
    """
    schema = TableSchema()
    schema.Table_Dataset = configurator.Dataset_Name
    schema.Table_Name = tableName
    schema.Metadata = schema.Table_Name["Metadata"]
    schema.Columns_Data = schema.Table_Name["Data"]
    schema.Columns_Names = [column["name"] for column in schema.Metadata]
    return schema

def CreateData(DICT_DATASET_TABLES: dict, configurator: SC, isSql: bool = False) -> bool:
    """[summary]
    Creates the data for a file.
    Args:
        DICT_DATASET_TABLES (dict): [Dictionary with all the tables of the dataset and their columns]
        configurator (ScriptConfigurator): [ScriptConfigurator object]
        sqlStatement (bool): [Boolean state that indicates if the data will be created for SQL or not]
    Returns:
        bool: [True if the file was created successfully or False if it wasn't]

    """
    json_pk_of_tables = {}
    msn = Messenger()
    success = False
    
    for tableName in DICT_DATASET_TABLES:
        
        schema = setup_schema(configurator, tableName)
        
        if (not schema.Table_Name in json_pk_of_tables.keys()):
            msn.print_message(f"Obtaining the amount of registers for table: {schema.Table_Name}")
            
            amountOfRegisters = schema.Metadata["AmountOfRegisters"] | 1000
            
            msn.print_message(
                f"Registers for {schema.Table_Name}: {amountOfRegisters}", 
                f"Generating data for {schema.Table_Name}",
                "This may taking a while, bassed on the",
                "Amount of registers and amount of columns"
            )
            #TODO: Generate the data for the table
            # dataMockRecord, actualTableDictionary = GD.CreateRecords(DICT_DATASET_TABLES, tableName, amountOfRegisters, jsonRecord, sqlStatement)
            # jsonRecord = actualTableDictionary
        if(isSql):
            msn.print_message(f"Creating SQL file for {schema.Table_Name}")
            # FH.WriteSQL(dataMockRecord, schema.Table_Dataset, schema.Table_Name)
            success = True
        else:
            msn.print_message(f"Creating CSV file for {schema.Table_Name}")
            # FH.WriteCSV(dataMockRecord, schema.Table_Dataset, schema.Table_Name)
            success = True
    return success, json_pk_of_tables

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
