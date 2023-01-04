import subprocess
import random


subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit" , "-m", "actualizado gitPages" ], capture_output=False)