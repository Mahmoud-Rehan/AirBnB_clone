#!/usr/bin/python3
""" HBNBCommand Class Module """
import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand console class
    """
    prompt = "(hbnb) "

    def emptyline(self):
        """
        Do nothing when an empty line is entered.
        """
        pass

    def do_EOF(self, arg):
        """
        EOF (Ctrl+D) signal to exit the program.
        """
        return True

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
