#!/usr/bin/python3
""" Console Implementation """
from cmd import Cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import json


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
        """ print an instance """
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

    def do_destroy(self, line):
        """ Deletes an instance """
        try:
            if line:
                class_name, class_id = line.split(" ")
                class_repr = "{}.{}".format(class_name, class_id)
                data = FileStorage()
                data.reload()
                data_loaded = data.all()
                if class_repr in list(data_loaded.keys()):
                    data_loaded.pop(class_repr)
                    d = {}
                    for key, value in data_loaded.items():
                        d[key] = value.to_dict()
                    with open(data.path(), mode='w', encoding="utf-8") as file:
                        file.write(json.dumps(d))
                else:
                    print("** no instance found **")
            else:
                print("** class name missing **")
        except ValueError:
            print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, line):
        """ Prints all string representation of all instances """
        if line:
            data = FileStorage()
            data.reload()
            data_loaded = data.all()
            print_all = []
            for key, value in data_loaded.items():
                list_key = key.split('.')
                if line == list_key[0]:
                    obj = eval(line)(**value.to_dict())
                    str_obj = obj.__str__()
                    print_all.append(str_obj)
            print(print_all)

        else:
            print("** class name missing **")

    def do_update(self):
        """ Updates an instance by adding or updating attribute """
        pass


if __name__ == "__main__":
    ''' Entry point for the loop '''
    HBNBCommand().cmdloop()
