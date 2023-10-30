import os

#to get the current working directory
directory = os.getcwd()
path = input("give the path of the created files")
save_path =  r''+ path
prefix = input("give the prefix of the created files")
ext= input("give the extension of the created files")
start = int (input("Please enter the start of created files: "))
stop = int (input("Please enter the stop of created files: "))
for i in range(start, stop, 1) :
    file_name = prefix + str( i ) + "." + ext
    completeName = os.path.join(save_path, file_name)
    open(completeName, "w").close()
print(directory)