
#Pen constants
Baseheight = 5
ProjectionDepth = 5
ProjectionforwardLength = 5
ProjectionDepthfromGround = ProjectionDepth + Baseheight
ProjectionforwardLengthfromGround = ProjectionforwardLength

class NewVectorFromServo():
    def TipPositionToBase(x , y ):
        Newx = x - ProjectionforwardLength
        Newy = y + ProjectionDepth
        return(Newx , Newy)

    def BasePositionToTip(  x , y):
        Newx = x + ProjectionforwardLength
        Newy = y - ProjectionDepth
        return(Newx , Newy)

print(NewVectorFromServo.TipPositionToBase(12,13))

class NewVectorFromBase():
    def TipPositionToBase(x , y ):
        Newx = x - ProjectionforwardLengthfromGround
        Newy = y + ProjectionDepthfromGround
        return(Newx , Newy)

    def BasePositionToTip(  x , y):
        Newx = x + ProjectionforwardLengthfromGround
        Newy = y - ProjectionDepthfromGround
        return(Newx , Newy)

print(NewVectorFromBase.TipPositionToBase(12,13))


'''class NewVectorFromServo:
    def __init__(self):
        self.height = 5
        self.ProjectionDepth = ProjectionDepth
        self.ProjectionforwardLength = ProjectionforwardLength
        self.ProjectionDepthfromGround = ProjectionDepth + self.height
        self.ProjectionforwardLengthfromGround = ProjectionforwardLength

    def TipPositionToBase( self , x , y ):
        Newx = x - self.ProjectionforwardLength
        Newy = y + self.ProjectionDepth
        return(Newx , Newy)

    def BasePositionToTip( self, x , y):
        Newx = x + self.ProjectionforwardLength
        Newy = y - self.ProjectionDepth
        return(Newx , Newy)

print(NewVectorFromServo.TipPositionToBase(, 10,5))
'''

'''class NewVectorFromGround():
    def __init__(self):
        self.height = 5
        self.ProjectionDepth = ProjectionDepth
        self.ProjectionforwardLength = ProjectionforwardLength
        self.ProjectionDepthfromGround = ProjectionDepth + self.height
        self.ProjectionforwardLengthfromGround = ProjectionforwardLength

    def TipPositionToBase( x , y):
        Newx = x - self.ProjectionforwardLength
        Newy = y + self.ProjectionDepth
        return(Newx , Newy)

    def BasePositionToTip( x , y):
        Newx = x + self.ProjectionforwardLength
        Newy = y - self.ProjectionDepth
        return(Newx , Newy)

print(NewVectorFromGround.TipPositionToBase( 10,5))
#3D plane'''