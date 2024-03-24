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

if __name__ == "__main__":
    HBNBCommand().cmdloop()
