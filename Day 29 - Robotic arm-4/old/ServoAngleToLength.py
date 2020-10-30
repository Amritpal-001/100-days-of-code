#import numpy as np
import math
from xlwt import Workbook


l5 = 9
l3 = 9

amax = 180

def pivalue(x):
    return(x*math.pi/180)

def initExcelFile():
    workbook = Workbook()
    sheet = workbook.add_sheet('Sheet 1')
    sheet.write(0, 0, 'Sr.no')
    sheet.write(0, 1, 'Servo 2 angle')
    sheet.write(0, 2, 'Servo 3 angle')
    sheet.write(0, 3, 'VertDist Point 2')
    sheet.write(0, 4, 'HorizDist Point2')
    sheet.write(0, 5, 'Sigma')
    return(workbook , sheet)

def ServoAngleToBaseLengthAllValues(save = True):
    c = 1
    sheet = initExcelFile()
    workbook = sheet[0]
    sheet1 = sheet[1]
    for servo2 in range(45,amax ,2):
        for servo3 in range(0, amax, 2):
            if  servo3 < servo2:
                if servo3 + servo2 < 180:
                    a = servo2
                    b = servo3

                    Sigma =  (180- a - b)/2
                    Sigma = pivalue(Sigma)
                    Theta = (a - b)/2
                    Theta = pivalue(Theta)

                    cos1 = math.cos(2*Theta)
                    sin1 = math.sin(2 * Theta)
                    cos2 = math.cos(Theta)
                    sin2 = math.sin(Theta)

                    l8 = l3*(sin1)
                    l9 = (l8)/cos2


                    VertDistPoint2  = round( (math.sin(Sigma) ) *  l9 , 2)
                    HorizDistPoint2  = round((math.cos(Sigma) ) *  l9 , 2)

                    #print(a , b, Theta, sin2,l8, l9,Sigma, VertDistPoint2, HorizDistPoint2)
                    print(a , b ,  l9 , VertDistPoint2, HorizDistPoint2)
                    sheet1.write(c, 0, a)
                    sheet1.write(c, 1, b)
                    sheet1.write(c, 2, l9)
                    sheet1.write(c, 3, VertDistPoint2)
                    sheet1.write(c, 4, HorizDistPoint2)
                    #sheet1.write(c, 5, Sigma)
                    c += 1
    if save == True:
        workbook.save('Values1111.xls')

ServoAngleToBaseLengthAllValues(save = True)

def BaseCoordintatesToServoAngle(x , y ):




#def RealCoordintatesToServoAngle(x , y ):
