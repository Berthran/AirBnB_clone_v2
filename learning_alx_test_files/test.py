import sys
import os
import shutil

# Backup the file storage and clean it up
file_path = "file.json"
# Backup
if os.path.exists(file_path):
    shutil.copy(file_path, "tmp_file_path.json")
# Cleanup
if os.path.exists(file_path):
    os.remove(file_path)

# Backup console file
shutil.copy("console.py", "tmp_console_main.py")

# Backup models/__init__.py file
shutil.copy("models/__init__.py", "models/tmp__init__.py")

# Overwrite the models/__init__.py file with switch_to_file_storage.py
shutil.copy("switch_to_file_storage.py", "models/__init__.py")

# Updating Console to Remove __main__
with open("tmp_console_main.py", "r") as file_i:
    console_lines = file_i.readlines()
    with open("console.py", "w") as file_o:
        in_main = False
        for line in console_lines:
            if "__main__" in line:
                in_main = True
            elif in_main:
                if "cmdloop" not in line:
                    file_o.write(line.lstrip("    ")) 
            else:
                file_o.write(line)

# import  modified console
import console
import inspect # This is used to inspect the objects in the console module
import io
import cmd

# Create Console
# Find the class object HBNBCommand which is a class in the console module
# and a sub-class of the cmd.Cmd module

console_obj = "HBNBCommand"
for name, obj in inspect.getmembers(console):
    if inspect.isclass(obj) and issubclass(obj, cmd.Cmd):
        console_obj = obj

my_console = console_obj(stdout=io.StringIO(), stdin=io.StringIO())
my_console.use_rawinput = False

# Create a function to exec console commands
def exec_command(my_console, the_command, last_lines=1):
    # Set up a string buffer to capture the console output
    my_console.stdout = io.StringIO()

    # Store the original value of sys.stdout
    real_stdout = sys.stdout

    # Redirect sys.stdout to the string buffer
    sys.stdout = my_console.stdout

    # Execute the console command using the onecmd method of the console object
    my_console.onecmd(the_command)

    # Restore the original value of sys.stdout
    sys.stdout = real_stdout

    # Get the captured console output and split it into lines
    lines = my_console.stdout.getvalue().split("\n")

    # Return the last 'last_lines' number of lines from the captured output
    return "\n".join(lines[(-1*(last_lines+1)):-1])


# Tests
state_name = "California"
result = exec_command(my_console, "create State name=\"{}\"".format(state_name))
print(f"The result: {result}")
if result is None or result == "":
    print("FAIL: No ID retrieved")
with open(file_path, "r") as file:
    s_file = file.read()
    if result not in s_file:
        print("FAIL: New ID not in the JSON file")
print("OK", end="")


## Restores the backups
shutil.copy("tmp_console_main.py", "console.py")
shutil.copy("models/tmp__init__.py", "models/__init__.py")

