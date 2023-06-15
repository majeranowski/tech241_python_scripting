import os
import subprocess

# Stores the file path to the current file
script_dir = os.path.dirname(__file__)
# Stores the filepath to the script you want to run
script_absolute_path = os.path.join(script_dir + "/shell_script.sh")

#Calls the shell file and runs it
subprocess.call(['sh', script_absolute_path])