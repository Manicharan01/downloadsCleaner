import os

download_path = "/home/charan/Downloads"
os.chdir(download_path)
print("In:", os.getcwd())
files = os.listdir()

fileAndFolderMapper = {"dirs": [], "music": [], "video": [], "image": [], "misc": []}

for file in files:
    if os.path.isdir(download_path + "/" + file):
        fileAndFolderMapper["dirs"].append(file)

    elif os.path.isfile(download_path + "/" + file):
        extension = os.path.splitext(file)[1]
        print(extension)
        if extension == ".png" or extension == ".jpg":
            fileAndFolderMapper["image"].append(file)
        elif extension == ".mp4" or extension == ".mkv":
            fileAndFolderMapper["video"].append(file)
        elif extension == ".mp3":
            fileAndFolderMapper["music"].append(file)

print(fileAndFolderMapper)
