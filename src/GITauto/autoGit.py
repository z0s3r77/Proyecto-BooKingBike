import subprocess
import random


def gitPush(message):

    subprocess.run(["git", "add", "."])

    if not message:
        subprocess.run(["git", "commit" , "-m", "base de datos actualizada" ], stdout=subprocess.DEVNULL)
    else:
        subprocess.run(["git", "commit" , "-m", message ], stdout=subprocess.DEVNULL)

    try:
        subprocess.run(["git", "push","origin", "master"], stdout=subprocess.DEVNULL)
        return True
    except:
        return False


# Como lo subo a master?