import os 
if os.path.exists("realfile.txt"):
    os.remove("realfile.txt")
else:
    print("The file does not exist")