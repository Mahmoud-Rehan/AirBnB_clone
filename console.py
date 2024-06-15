#!/usr/bin/python3
""" HBNBCommand Class Module """
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

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


if __name__ == "__main__":
    HBNBCommand().cmdloop()