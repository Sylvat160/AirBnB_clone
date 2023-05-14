#!/usr/bin/python3
"""
Console for AirBnB clone project
"""


import cmd
from models.base_model import BaseModel
from models.__init__ import storage


class HBNBCommand(cmd.Cmd):
    """Entry point of the command interpreter"""

    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program : Ctrl + D"""
        print()
        return True

    def emptyline(self):
        """Do nothing when empty line is entered"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
