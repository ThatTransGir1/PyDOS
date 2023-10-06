class File:
    def __init__(self, filename, parent):
        self.filename = filename
        self.parent = parent


class Folder:
    def __init__(self, foldername, parent=None):
        self.foldername = foldername
        self.subFolders = []
        self.files = []
        self.parent = parent
        if parent != None:
            parent.subFolders.append(self)

    # A function to create a new file into this folder
    def newFile(self, file):
        file = File(file, self)
        self.files.append(file)
        return file

    # A function to create a new subfolder (MaKe DIRectory)
    def mkdir(self, foldername):
        for f in self.subFolders:
            if f.foldername == foldername:
                print("This subfolder already exists!")
                return False
        subFolder = Folder(foldername, self)
        print("New Subfolder created!")
        return subFolder

    # A function to list the content of a folder (DIRectory)
    def dir(self):
        print(self.foldername + ":")
        if self.parent != None:
            print(" + ..")
        for folder in self.subFolders:
            print(" + " + folder.foldername)
        for file in self.files:
            print(" - " + file.filename)

    # A function to delete a file or a subfolder (DEL)
    def delete(self, filename):
        for folder in self.subFolders:
            if folder.foldername == filename:
                self.subFolders.remove(folder)
                print(filename + " has been deleted!")
                return True
        # Not a folder could be a file
        for file in self.files:
            if file.filename == filename:
                self.files.remove(file)
                print(filename + " has been deleted!")
                return True
        print("Could not delete file or folder. File or folder not found.")
        return False

    # A function to rename a file or a subfolder (RENAME)
    def rename(self, filename, newname):
        for folder in self.subFolders:
            if folder.foldername == filename:
                folder.foldername = newname
                print(filename + " has been renamed!")
                return True
        # Not a subfolder could be a file...
        for file in self.files:
            if file.filename == filename:
                file.filename = newname
                print(filename + " has been renamed!")
                return True
        print("Could not rename file or folder. File or folder not found.")
        return False

    # A fuction to navigate to a subfolder or the parent folder (..) (Change Directory)
    def cd(self, foldername):
        if foldername == "..":
            if self.parent == None:
                print("Invalid operation. This is the root folder.")
                return False
            else:
                return self.parent
        for f in self.subFolders:
            if f.foldername == foldername:
                return f
        print("Subfolder does not exist.")
        return False
