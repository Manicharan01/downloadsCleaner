import os

download_path = "/home/charan/Downloads"  # The directory we want to work on

# This sets the given directory as working, so that we can maniupulte said directory
os.chdir(download_path)

# Dict Initalizing
fileAndFolderMapper = {
    "dirs": [],
    "music": [],
    "video": [],
    "image": [],
    "misc": [],
}


# To populate the fileAndFolderMapper dict with the files according to their extension type
def mapperPopulator(files):
    for file in files:
        if os.path.isdir(download_path + "/" + file):
            fileAndFolderMapper["dirs"].append(file)

        elif os.path.isfile(download_path + "/" + file):
            extension = os.path.splitext(file)[1]
            if extension == ".png" or extension == ".jpg":
                fileAndFolderMapper["image"].append(file)
            elif extension == ".mp4" or extension == ".mkv":
                fileAndFolderMapper["video"].append(file)
            elif extension == ".mp3":
                fileAndFolderMapper["music"].append(file)


# To populate the files list with the files available is the Downloads directory
files = os.listdir()


# Gives control to mapperPopulator to populate the dict with files available in directory
if files:
    mapperPopulator(files)


# This runs until list available in fileAndFolderMapper are empty
while True:
    for file in fileAndFolderMapper["music"]:
        os.system("mv" + " '" + file + "' " + "/home/charan/Music")
    fileAndFolderMapper["music"].clear()
    for file in fileAndFolderMapper["video"]:
        os.system("mv" + " '" + file + "' " + "/home/charan/Videos")
    fileAndFolderMapper["video"].clear()
    for file in fileAndFolderMapper["image"]:
        os.system("mv" + " '" + file + "' " + "/home/charan/Pictures")
    fileAndFolderMapper["image"].clear()
    break
