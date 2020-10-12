
import cv2
import os

image_folder = '/home/amritpal/Downloads/GAN---99-99/output'
video_name = 'video.avi'

def sort(lst):
    lst = [str(i) for i in lst]
    lst.sort()
    lst = [int(i) if i.isdigit() else i for i in lst]
    return lst


import re


def sorted_nicely(l):
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(l, key=alphanum_key)



images = [img for img in os.listdir(image_folder) if img.endswith(".png")]

print(sorted_nicely(images))
images = sorted_nicely(images)
#print(images)
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, 4, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()