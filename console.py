#!/usr/bin/python3
""" Console Implementation """
from cmd import Cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


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

    def do_create(self, line):
        """ Create new instance """
        try:
            if not line:
                print("** class name missing **")
            else:
                instance = eval(line)()
                instance.save()
                print(instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """ print instance """
        try:
            if line:
                class_name, class_id = line.split(" ")
                class_repr = "{}.{}".format(class_name, class_id)
                data = FileStorage()
                data.reload()
                data_loaded = data.all()
                if class_repr in list(data_loaded.keys()):
                    print(data_loaded[class_repr])
                else:
                    print("** no instance found **")
            else:
                print("** class name missing **")
        except ValueError:
            print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")


if __name__ == "__main__":
    ''' Entry point for the loop '''
    HBNBCommand().cmdloop()
