#!/usr/bin/python3
""" HBNBCommand Class Module """
import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """ HBNBCommand Class """
    prompt = "(hbnb) "

    classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
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


    def do_destroy(self, line):
        """ Deletes an instance based on
        <Class name> and <Id> """
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
                del storage.all()[key]
                storage.save()


    def do_all(self, line):
        """ prints all string representatio of all instances """
        my_objects = storage.all()
        lines = shlex.split(line)

        if len(lines) == 0:
            print([str(v) for k, v in my_objects.items()])
        elif lines[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
        else:
            for key, value in my_objects.items():
                if key.split(".")[0] == lines[0]:
                    print(str(value))


    def do_update(self, line):
        lines = line.split()

        if not lines:
            print("** class name missing **")
            return

        if lines[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if len(lines) < 2:
            print("** instance id missing **")
            return

        key = f"{lines[0]}.{lines[1]}"

        if key not in storage.all():
            print("** no instance found **")
            return

        if len(lines) < 3:
            print("** attribute name missing **")
            return

        if len(lines) < 4:
            print("** value missing **")
            return

        setattr(storage.all()[key], lines[2], lines[3])
        storage.save()




if __name__ == "__main__":
    HBNBCommand().cmdloop()
