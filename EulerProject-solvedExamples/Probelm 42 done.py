
import re

MyTextFile = open('files/p042_words.txt' , 'r')
#print(MyTextFile)
for a in MyTextFile:
    MyFileList = re.findall("[a-zA-Z\-\.'/]+" ,a)

#print(len(MyFileList))

def TriangleNumberList(TillX):
    TriangleNumberList = []
    for i in range(1 ,TillX):
        TraingleNumber = i*(i+1)/2
        TriangleNumberList.append(int(TraingleNumber))
    #print(TriangleNumberList)
    return(TriangleNumberList)

TriangleNumberList = TriangleNumberList(23)

def TriangularWord(inputword):
    NumericalSum = 0
    for a in inputword:
        a = a.lower()
        NumericalSum += ord(a) - 96
        #print(NumericalSum)
    if NumericalSum in TriangleNumberList:
        #print('True' , NumericalSum)
        return (True)

    #else: print("not in list")


TriangularWord('SKY')

c = 0
for i in MyFileList:
    if TriangularWord(i) == True:
        c += 1
        
print(c)