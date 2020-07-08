#!/usr/bin/python3
""" Console Implementation """
from cmd import Cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
import json
import shlex


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
                args = line.split(" ")
                if not isinstance(eval(args[0])(), BaseModel):
                    raise NameError
                if len(args) < 2:
                    raise ValueError
                obj_name, obj_id = args
                obj_repr = "{}.{}".format(obj_name, obj_id)
                data = FileStorage()
                data.reload()
                data_loaded = data.all()
                if obj_repr in list(data_loaded.keys()):
                    print(data_loaded[obj_repr])
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
                args = line.split(" ")
                if not isinstance(eval(args[0])(), BaseModel):
                    raise NameError
                if len(args) < 2:
                    raise ValueError
                obj_name, obj_id = args
                obj_repr = "{}.{}".format(obj_name, obj_id)
                data = FileStorage()
                data.reload()
                data_loaded = data.all()
                if obj_repr in list(data_loaded.keys()):
                    data_loaded.pop(obj_repr)
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
        try:
            if line:
                if not isinstance(eval(line)(), BaseModel):
                    raise NameError
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
        except NameError:
            print("** class doesn't exist **")

    def do_update(self, line):
        """ Updates an instance by adding or updating attribute """
        if line:
            args = shlex.split(line)
            if len(args) < 2:
                print("** instance id missing **")
                return False
            elif len(args) < 3:
                print("** attribute name missing **")
                return False
            elif len(args) == 3:
                print("** value missing **")
                return False
            else:
                obj_name, obj_id, obj_attr, obj_value = args
            obj_repr = "{}.{}".format(obj_name, obj_id)
            data = FileStorage()
            data.reload()
            data_loaded = data.all()
            for key, value in data_loaded.items():
                if key == obj_repr:
                    obj = eval(obj_name)(**value.to_dict())
                    if obj_name in obj.__dict__.keys():
                        obj[obj_name] = obj_value
                    else:
                        setattr(obj, obj_attr, obj_value)
                    d = {}
                    for s_key, s_value in data_loaded.items():
                        d[s_key] = s_value.to_dict()
                    with open(data.path(), mode='w', encoding="utf-8") as file:
                        file.write(json.dumps(d))
                    break
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")


if __name__ == "__main__":
    ''' Entry point for the loop '''
    HBNBCommand().cmdloop()
