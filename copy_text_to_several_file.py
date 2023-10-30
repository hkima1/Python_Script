import os
fold = input("give the path of the specified folder")
save_fold =  r''+ fold
files = [f for f in os.listdir(save_fold) if os.path.isfile(save_fold +"\\"+f) and os.path.splitext(f)[1] != ".py" ]
print(files)

# open a file that contain the text
path = input("give the path of the copied file")
save_path =  r''+ path
file1 = open(save_path , "r")

# read the file
read_content = file1.read()

for f in files :
    with open(save_fold +"\\"+f, 'w') as file:
              file.write(read_content)

 
