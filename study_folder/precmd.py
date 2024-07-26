# The `precmd` method is called before a command is executed. It is used majorly to modify the command input or perform any pre-processing
# The `postcmd`  method is called after a command has been executed. It can be used to perform any post-processing, such as cleanup or logging.

import cmd

class MyCmd(cmd.Cmd):
    prompt = '$ ' 

    def precmd(self, line):
        print(f"[DEBUG] About to execute: {line}")
        return line

    def postcmd(self, stop, line):
        print(f"[DEBUG] Finished executing: {line}")
        return stop

    def do_greet(self, line):
        """Greet the user"""
        print(f"Hello, {line}!")

    def do_exit(self, line):
        """Exit the command loop"""
        print("Goodbye!")
        return True

if __name__ == '__main__':
    MyCmd().cmdloop()

# When to use a precmd
# when you need to perform actions before a command is executed, such as logging, command modification, input validation, or setting up the environment.

# When to use a postcmd
# when you need to perform actions after a command is executed, such as cleanup, logging the result, or updating the state.
