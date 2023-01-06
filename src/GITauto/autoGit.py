import subprocess
import random


def gitPush(message):

    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit" , "-m", message ], stdout=subprocess.DEVNULL)
    subprocess.run(["git", "push",])

# Como lo subo a master?