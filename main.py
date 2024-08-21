import os

os.chdir("/home/charan/Downloads")
print("In:", os.getcwd())
files = os.listdir()

for file in files:
    if file == "anime" or file == "4836237_23645781931.png":
        continue
    else:
        print("Deleting:", file)
        os.system(f"rm -rf {file}")
