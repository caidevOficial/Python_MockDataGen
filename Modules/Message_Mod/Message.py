# GNU General Public License V3
#
# Copyright (c) 2022 [FacuFalcone]
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
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

class Messenger:
    """[summary]
    Class to print messages in the console. \n
    Returns:
        class: [CloneMessenger]. \n
    """
    # ?######? START ATTRIBUTES #######
    __message: str = ''
    __messages: list = []
    # ?######? END ATTRIBUTES #######

    def __init__(self) -> None:
        pass

    # ?######? START PROPERTIES #######

    @property
    def Message(self) -> str:
        """[summary] \n
        Get the message of the class. \n
        Returns:
            str: Message of the class. \n
        """
        return self.__message
    
    @property
    def Messages(self) -> list:
        """[summary] \n
        Get the messages of the class. \n
        Returns:
            list: Messages of the class. \n
        """
        return self.__messages

    @Message.setter
    def Message(self, message: str) -> None:
        """[summary] \n
        Sets the message of the class. \n
        Args:
            message (str): The message to be printed in the console. \n
        """
        self.__message = message

    # ?######? END PROPERTIES #######

    # ?###########? START METHODS ############

    def add_message(self, message: str) -> None:
        """[summary] \n
        Adds a message to the list of messages of the class. \n
        Args:
            message (str): The message to be added to the list of messages. \n
        """
        self.Messages.append(message)
    
    def add_messages(self, *args) -> None:
        """[summary] \n
        Adds messages to the list of messages of the class. \n
        Args:
            *args (str): The messages to be added to the list of messages. \n
        """
        for i in args:
            self.Messages.append(i)

    def message_decor(self, func) -> None:
        """[summary]\n
        Decorator to show a message before and after the function.
        
        Args:
            func (function): [The function to be decorated.]
        """
        def wrapper(*args):
            self.add_messages(args)
            max_len = max([len(i) for i in self.Messages])
            symbols = ''.join(['#' for _ in range(max_len)])
            print(symbols)
            func(*args)
            print(f'{symbols}\n')
            self.Messages.clear()
        return wrapper

    @message_decor
    def print_message(self, message: str) -> None:
        """[summary]\n
        Prints a message.
        
        Args:
            message (str): [The message to be printed.]
        """
        print(message)

    def Initialize_Messenger(self, message: str) -> None:
        """[summary] \n
        Initializes the class with a message. \n
        Args:
            message (str): The message to be printed in the console. \n
        """
        self.Message = message

    def Generate_Symbols(self) -> str:
        """[summary] \n
        Generates a string of symbols of the same length of the message of the class. \n
        Returns:
            str: String of symbols of the same length of the message of the class. \n
        """
        return ''.join(['#' for i in range(len(self.Message))])

    # ?###########? END METHODS ############