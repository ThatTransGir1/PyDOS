from time import sleep
from random import randint
def intro():
    print("PyBIOS (version BETA 1.0)")
    num1 = randint(10, 60)
    sleep(5)
    print("Booting from Hard Disk")
    sleep(num1)
    print("Starting PyDOS...\n")
