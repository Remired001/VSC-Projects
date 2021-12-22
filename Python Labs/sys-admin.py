# import os

# os.system("ls")

# import subprocess

# subprocess.run(["ls"])

# subprocess.run(["ls","-l"])

import subprocess

# subprocess.run(["ls","-l","categorize-values.py"])

command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run({command,commandArgument})