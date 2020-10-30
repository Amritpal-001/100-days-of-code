from PIL import Image
import numpy
from numpy import asarray

image = Image.open('photo.jpg').convert('L')
print(image.format)
print(image.size)
print(image.mode)
#image.show()


data = asarray(image)
print(type(data))
print(data.shape)
#print(data)

#Photo bak from array
#image2 = Image.fromarray(data)

shape = data.shape
Myarray = numpy.empty(shape, dtype=float, order='C')

'''print(data[3 , :])
print(data[3])'''


#print(Myarray)

cutoff = 120

print(data[10,10])

for x in range(shape[0]):
    for y in range(shape[1]):
        if data[x,y] <= cutoff:
            #print(data[x,y])
            Myarray[x,y] = data[x,y]

print(Myarray)
image2 = Image.fromarray(Myarray)
image2.show()




