from PIL import Image
import numpy
from numpy import asarray

def ImagetoNumpy(ImageDirectory , mode = 'L'  , verbosity = False):
    image = Image.open(ImageDirectory).convert(mode)
    if verbosity == True:
        print(image.format)
        print(image.size)
        print(image.mode)
        image.show()

    data = asarray(image)

    if verbosity == True:
        print(type(data))
        print(data.shape)
    return(data)

#Myimage = ImagetoNumpy('photo.jpg' , verbosity= False)

def CreateArray(ImageData , verbosity = False):
    shape = ImageData.shape
    NewArray = numpy.empty(shape, dtype=float, order='C')
    if verbosity == True:
        print(NewArray.shape)
        image2 = Image.fromarray(NewArray)
        image2.show()
    return(NewArray)

#NewArray = CreateArray(Myimage , verbosity= False)


def Cutofflayers(cutoff , Imagedirectory , cutABorbL = 'below' , save = True , verbosity = False):
    Imagedata = ImagetoNumpy(Imagedirectory, verbosity=False)
    NewArray = CreateArray(Imagedata, verbosity=False)
    shape = NewArray.shape
    for x in range(shape[0]):
        for y in range(shape[1]):
            if cutABorbL == 'below':
                if Imagedata[x, y] <= cutoff:
                    NewArray[x, y] = Imagedata[x, y]
            if cutABorbL == 'above':
                if Imagedata[x, y] >= cutoff:
                    NewArray[x, y] = Imagedata[x, y]
    if verbosity == True:
        print(NewArray)
        image2 = Image.fromarray(NewArray)
        image2.show()

#Cutofflayers(20 , 'photo.jpg' ,  cutABorbL = 'above' , save = True , verbosity = True)


def BelowCutofflayers(cutoff , Imagedata , save = True , verbosity = False):
    NewArray = CreateArray(Imagedata, verbosity=False)
    shape = NewArray.shape
    for x in range(shape[0]):
        for y in range(shape[1]):
            if Imagedata[x, y] <= cutoff:
                NewArray[x, y] = Imagedata[x, y]
    return(NewArray)

def CutintoNlayers(N , Imagedirec , verbosity = False):

    Imagedata = ImagetoNumpy(Imagedirec , verbosity=False)
    shape = Imagedata.shape
    for x in range(1, N+1):
        if x == 1:
            cutoff = x * 256 / N
            ArrayUp = BelowCutofflayers(cutoff , Imagedata, save=True, verbosity=False)
            ImageName = './output/' + str(x) + '-' + str(N) + Imagedirec
            image2 = Image.fromarray(ArrayUp).convert('RGB').save(ImageName)
            #image2.show()

        else:
            cutoffup = x * 256 / N
            cutoffdown = (x - 1) * 256 / N
            ArrayUp  = BelowCutofflayers(cutoffup , Imagedata, save=True, verbosity=False)
            ArrayDown = BelowCutofflayers(cutoffdown, Imagedata, save=True, verbosity=False)
            FinalArray = ArrayUp - ArrayDown
            #print(FinalArray)
            ImageName = './output/' + str(x) + '-' + str(N) + Imagedirec
            image2 = Image.fromarray(FinalArray).convert('RGB').save(ImageName)
            #image2.show()

CutintoNlayers(6 , 'photo.jpg', verbosity = True)

'''
def AddingTwoNumpyArray(Array1 , ArraytoAddInto, Location1 , Location2):
    shape = Array1.shape
    for x in range(shape[0]):
        for y in range(shape[1]):
            a = round(x + Location1(shape[0]))
            b = round(y +  Location2(shape[1]))
            ArraytoAddInto[a , b] = Array1[x, y]
    return(ArraytoAddInto)

def GenerateClipartofallImagesTogehter(N , Imagedirec):

    Imagedata = ImagetoNumpy(Imagedirec , verbosity=False)
    shape = Imagedata.shape
    BigArray = numpy.empty([shape[0]*2 , shape[1]*2 ], dtype=float, order='C')
    print(N**2)

    for x in range(1, N+1):
        if x == 1:
            cutoff = x * 256 / N
            ArrayUp = BelowCutofflayers(cutoff , Imagedata, save=True, verbosity=False)
            AddingTwoNumpyArray(ArrayUp, BigArray, 0, 0)

        else:
            cutoffup = x * 256 / N
            cutoffdown = (x - 1) * 256 / N
            ArrayUp  = BelowCutofflayers(cutoffup , Imagedata, save=True, verbosity=False)
            ArrayDown = BelowCutofflayers(cutoffdown, Imagedata, save=True, verbosity=False)
            FinalArray = ArrayUp - ArrayDown
            AddingTwoNumpyArray(FinalArray , BigArray, 1, 1)

    ImageName = './output/BIgOutput' + str(N) + Imagedirec
    image2 = Image.fromarray(BigArray).convert('RGB').save(ImageName)
    image2.show()
'''
