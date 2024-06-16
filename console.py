#!/usr/bin/python3
""" HBNBCommand Class Module """
import cmd
from models.base_model import BaseModel


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

if __name__ == "__main__":
    HBNBCommand().cmdloop()
