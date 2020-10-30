# Open the file in read mode 

Namelist = []

Totaltext = []

text1 = "print"


import os

# List all files in a directory using os.listdir
basepath = '/home/amritpal/Downloads/Coding/Test'
for entry in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath, entry)):
        Namelist.append(entry)
    #print(Namelist)

for n in range (0, len(Namelist)):
    '''print(n)
    print(Namelist[n])'''
    nameoffile = Namelist[n]
    text = open( nameoffile ,  "r")
    
    for line in text:
        Totaltext.append(line)
        #print(line)
        text1 += line

print(text1)


file1 = open("text.txt" , "w+")
# \n is placed to indicate EOL (End of Line) 
file1.write(text1)  
file1.close()


