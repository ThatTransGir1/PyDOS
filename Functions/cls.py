import os
import platform
def cls():
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Linux":
        os.system("clear")
    elif platform.system() == "Darwin":
        os.system("clear")