import os
import time
from Functions.fileandfolder import File, Folder
import Functions.help as help
import Functions.cls as cls
import Functions.startup as startup
import Functions.dateandtime as dateandtime
import Functions.echo as echo

# Create File and Folder Structure
root = Folder("root")
myDocuments = root.mkdir("myDocuments")
myPictures = root.mkdir("myPictures")
myVideos = root.mkdir("myVideos")
maths = myDocuments.mkdir("Maths")
computerscience = myDocuments.mkdir("ComputerScience")
english = myDocuments.mkdir("English")
photos = myPictures.mkdir("Photos")
cartoons = myPictures.mkdir("Cartoons")
file1 = myDocuments.newFile("timetable.doc")
file2 = photos.newFile("sea.jpg")
file3 = photos.newFile("house.jpg")
file4 = photos.newFile("cat.jpg")
file5 = cartoons.newFile("mickey.png")
file6 = cartoons.newFile("bugs-bunny.png")
file7 = english.newFile("essay.doc")
file5 = computerscience.newFile("hello-world.py")
file7 = computerscience.newFile("space-invader.py")
file8 = computerscience.newFile("pacman.py")
file9 = maths.newFile("primary-numbers.txt")
cls.cls()

# Start DOS Emulator!
currentFolder = root
startup.intro()
# currentFolder.dir()

while True:
    # print("")
    instruction = input("C:\>").split(" ")
    if instruction[0].upper() == "EXIT":
        print("Shutting down PyDOS")
        time.sleep(30)
        break

    elif instruction[0].upper() == "HELP":
        help.helpscrn()

    elif instruction[0].upper() == "CLS":
        cls.cls()

    elif instruction[0].upper() == "DIR":
        currentFolder.dir()

    elif instruction[0].upper() == "DEL":
        if len(instruction) < 2:
            print("Invalid file name or file not found")
        else:
            currentFolder.delete(instruction[1])
    elif instruction[0].upper() == "RENAME":
        if len(instruction) < 3:
            print("Invalid file name or file not found")
        else:
            currentFolder.rename(instruction[1], instruction[2])

    elif instruction[0].upper() == "CD":
        if len(instruction) < 2:
            print("Invalid file name or file not found")
        else:
            foldername = instruction[1]
            subFolder = currentFolder.cd(foldername)
            if subFolder != False:
                currentFolder = subFolder
                print("Current Folder: " + currentFolder.foldername)

    elif instruction[0].upper() == "MKDIR":
        if len(instruction) < 2:
            print("Bad command or file name")
        else:
            foldername = instruction[1]
            currentFolder.mkdir(foldername)
    elif instruction[0].upper() == "DATE":
        dateandtime.date()
    elif instruction[0].upper() == "TIME":
        dateandtime.time()
    elif instruction[0].upper() == "ECHO":
        echo.echo(list1 = instruction, list2 = instruction[0])

    else:
        print("Bad command or file name")
