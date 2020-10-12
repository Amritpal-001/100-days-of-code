import PIL
from PIL import Image
import os

def converttothunbnail(img , thumbnailDim):
    size = thumbnailDim
    Myimg = Image.open(img)
    Myimg.thumbnail(size)
    Myimg.save(img + "thumbnail.", "JPEG")
    return(Myimg)

def GenerateBaseImage(size, color=(255,255,255)):
    blank_image = PIL.Image.new(mode = 'RGB', size = size, color=color)
    out = "BaseImage.jpg"
    blank_image.save(out)
    return(out)

def AddImageTogether(img1path, Baseimage ,  StartPointX , StartPointY , thumbnailDim):
    img= converttothunbnail(img1path , thumbnailDim)
    blank_image = Image.open(Baseimage)
    out = "./output/" + os.path.basename(img1path)
    headbox = (0, 0, 3000, 3000)
    blank_image.crop(box=headbox)
    blank_image.paste(img, ( StartPointX , StartPointY , StartPointX+ img.size[0], StartPointY+img.size[1]) )
    blank_image.save(out)
    blank_image.show()

thumbnailDim = (224,224)
BaseImageSize = (1000 , 1000)

img1path = 'Images/01.jpg'
StartPointX = 350
StartPointY = 750

Baseimage = GenerateBaseImage(BaseImageSize)
AddImageTogether(img1path, Baseimage , StartPointX , StartPointY , thumbnailDim = thumbnailDim)