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

import datetime
import os
from Modules_4.GetConfigs_Mod.Configs import ScriptConfigurator as Config
from Modules_4.Message_Mod.Message import Messenger as Msn
from Modules_4.Formatter_Mod.Timer import Timer as Tmr
from Modules_4.FileHandle_Mod.FileHandle import OpenFile as Open

################################ SETUP AREA ################################
configurator = Config(os.path.dirname(os.path.realpath(__file__)))
################################ SETUP AREA ################################

def SEA_MDG() -> None:
    dataset = configurator.Dataset_Name
    try:
        # Abre el archivo con todas las tablas del dataset
        DICT_DATASET_TABLES = Open(configurator.Absolute_Path_Config_File)

        if configurator.isSql():
            # Crear registros tipo sql
            pass
        else:
            # Crear registros tipo csv
            
            pass


    except Exception as e:
        Msn.print_message(f'Error: {e}')


if __name__ == "__main__":
    start_time = datetime.datetime.now()
    try:
        # ?#########? Start Objects Instances ##########
        timer = Tmr()
        # ?#########? End Objects Instances ##########
        
        # ?#########? Start Timer Config ##########
        timer.CrudeTime = start_time
        # ?#########? End Timer Config ##########

        # ?#########? Start Print Message ##########
        Msn.print_message(f"Elapsed Time: {timer.FormattedTimeStr}")
        # ?#########? End Print Message ##########
        
    except Exception as e:
        Msn.print_message(f'Error: {e}')
    finally:
        end = input()