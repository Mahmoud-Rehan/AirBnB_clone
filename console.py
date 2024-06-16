#!/usr/bin/python3
""" HBNBCommand Class Module """
import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """ HBNBCommand Class """
    prompt = "(hbnb) "

    classes = {
            "BaseModel": BaseModel
            }

    def do_quit(self, line):
        """ Quit command to exit the program """
        return (True)

    def do_EOF(self, line):
        """ EOF signal to exit the program """
        print("")
        return (True)

    def emptyline(self):
        """ Pass when getting an empty line """
        pass

    def do_create(self, line):
        """ Creates a new instance of a class """
        if line:
            try:
                new_obj = HBNBCommand.classes[line]()
                new_obj.save()
                print(new_obj.id)
            except Exception:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        """ Show the string representation of an instance
        based on <Class name> and <Id> """
        lines = line.split()

        if not lines:
            print("** class name missing **")
        elif lines[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(lines) < 2:
            print("** instance id missing **")
        else:
            key = f"{lines[0]}.{lines[1]}"

            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])


if __name__ == "__main__":
    HBNBCommand().cmdloop()
