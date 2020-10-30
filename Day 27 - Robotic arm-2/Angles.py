import numpy as np

q = np.sin((np.pi)/2)
w = np.arcsin(q)
w = w * (57.2958)

def InvSin(x):                 #Inverse Sin in degrees
    b = np.arcsin(x)
    b = b * (57.2958)
    return(b)

LongArmPeripheralPart =  9
l5 = LongArmPeripheralPart

BaseBlackArm = 9.5
l3 = BaseBlackArm

#a = servo3
#b = servo2
a = (np.pi)/3
b = (np.pi)/2

Sigma =  (180- a - b)/2
print(Sigma)
sin1 = np.sin(a-b)
cos1 = np.cos(a-b)


l9 = l3*(   sin1**2  - (1-cos1)**2    )
print(l9)
#HorizontalDIstPoint2 =
VertDistPoint2  = (np.sin(Sigma) ) *  l9
print(VertDistPoint2)

