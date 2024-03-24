#!/usr/bin/python3
""" HBNBCommand Interpreter Module """
import cmd


class HBNBCommand(cmd.Cmd):
    """ HBNBCommand Interpeter Class """
    prompt = "(hbnb) "

    def do_quit(self, command):
        """ Quit the console """
        print("")
        return (True)

    def do_EOF(self, command):
        """ Exit when received a signal """
        print("")
        return (True)

    def emptyline(self):
        """ Pass when empty line """
        pass

    def do_create(self, command):
        if command:
            try:
                new_class = globals().get(command, None)
                new_obj = new_class()
                new_obj.save()
                print(new_obj.id)
            except Exception:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, command):
        cmd_array = command.split()

        if len(cmd_array) < 1:
            print("** class name missing **")
        elif cmd_array[0] not in classes:
            print("** class doesn't exist **")
        elif len(cmd_array) < 2:
            print("** instance id missing **")
        elif f"{cmd_array[0]}.{cmd_array[1]}" not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()["{}.{}".format(cmd_array[0], cmd_array[1])])

if __name__ == "__main__":
    HBNBCommand().cmdloop()
