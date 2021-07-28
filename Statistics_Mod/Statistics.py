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

def CountRegisters(jsonWithRegisters: dict) -> int:
    """[summary]
        Count the number of registers in the json file.
    Args:
        jsonWithRegisters (dict): [Collection with the registers as pk]
    Returns:
        int: [The ammount of registers]
    """
    totalRecords = 0
    for k,v in jsonWithRegisters.items():
        for v,i in v.items():
            totalRecords += i.__len__()
    return round(totalRecords, 2)

def FormatAmountRegisters(amount:int) -> str:
    """[summary]
        Format the amount of registers as a string.
    Args:
        amount (int): [Initial Amount of registers.]
    Returns:
        str: [The amount of registers as a string.]
    """
    message = ""
    if(amount >= 1000000):
        amount /= 1000000
        message = f"{amount} Million"
    elif(amount >= 1000):
        while(amount >= 1000):
            amount /= 1000
        amount = round(amount, 1)
        message = f"{amount} Thousand"
    
    return message

def TimeFormatted(start_time:datetime) -> str:
    """[summary]
        Format the time (seconds) as a string.
    Args:
        start_time (datetime): [Amount of time]
    Returns:
        str: [The message with the time]
    """
    seconds = ( datetime.datetime.now() - start_time ).total_seconds()
    m, s = divmod(seconds, 60)
    return "{:02.0f} minute(s) {:02.0f} seconds".format(m, s)