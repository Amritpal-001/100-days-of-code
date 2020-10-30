import numpy as np

'''
int servo1 = 75 - 179
int servo2 = 1 - 90    a
int servo3 = 45 -60 - 145    b
int servo4 = 179

#b = servo2 - 90
#a  servo1
b = 
'''

l5 = 9
l3 = 9

import xlwt
from xlwt import Workbook
wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')
sheet1.write(0, 0, 'Sr.no')
sheet1.write(0, 1, 'Servo 2 angle')
sheet1.write(0, 2, 'Servo 3 angle')
sheet1.write(0, 3, 'VertDist Point 2')
sheet1.write(0, 4, 'HorizDist Point2')
sheet1.write(0, 5, 'Sigma')

c = 1
amax = 90
for servo3 in range(0, amax, 10):
    for servo2 in range(45,amax ,5):
        if  servo3 < servo2:
            if servo3 + servo2 < 180:

                a = servo2
                b = servo3

                Sigma =  (180- a - b)/2
                Sigma = Sigma * (np.pi) / 90
                #sin = np.sin(a-b)
                #cos1 = np.cos(a-b)

                Theta = (a - b)/2   #in radians
                #d = d*180/(np.pi)   #in terms of pi
                Theta = Theta * (np.pi) / 90  # in terms of pi

                cos1 = np.cos(2*Theta)
                sin1 = np.sin(2 * Theta)
                cos2 = np.cos(Theta)
                sin2 = np.sin(Theta)
                #l9 = l3*(   sin**2  - (1-cos)**2    )

                l8 = l3*(sin1)
                l9 = (l8)/cos2

                VertDistPoint2  = (np.sin(Sigma) ) *  l9
                HorizDistPoint2  = (np.cos(Sigma) ) *  l9
                #print(Sigma)
                #print(a , b, Theta, sin2,l8, l9,Sigma, VertDistPoint2, HorizDistPoint2)
                print(a , b ,  l9 , VertDistPoint2, HorizDistPoint2)
                sheet1.write(c, 0, c)
                sheet1.write(c, 1, a)
                sheet1.write(c, 2, b)
                sheet1.write(c, 3, VertDistPoint2)
                sheet1.write(c, 4, HorizDistPoint2)
                sheet1.write(c, 5, Sigma)
                c += 1

wb.save('xlwt example.xls')