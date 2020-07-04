#!/usr/bin/python3
""" Console Implementation """
from cmd import Cmd


class HBNBCommand(Cmd):
    """ command interpreter methods """

    prompt = "(hbnb) "

    def do_quit(self, line):
        """ exit the program """
        return True

    def do_EOF(self, line):
        """ exit the program """
        return True

    def emptyline(self):
        """ empty line """
        pass

if __name__ == "__main__":
    ''' Entry point for the loop '''
    HBNBCommand().cmdloop()
