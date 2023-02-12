# Process to capture , create a greyscale copy and recreate each image and all variations of that image for training.
# This will give you 1 X 16 count. For every 1 image 15 will be generated.
# Becaues Sometimes you have to create more data from the original to expand the dataset with viable images.
# 12 Feb 2023
# Michael J. Stattelman
#/////////////////////////////////////////////////////////////////////////////////////////
import re
import os
import cv2
import sys
import uuid
import glob
import PIL
from PIL import Image


def files2():
  file_list = []
  for file in glob.glob("*.jpg"):
        file_list.append(file)
  return file_list


def createGreycopies(greyList):
  for x in range(len(greyList)):
    image = cv2.imread(greyList[x])
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(str(uuid.uuid4())+'-grey.jpg', image_gray)

def flip_save(saveList):
  for x in range(len(saveList)): 
      picture= Image.open(saveList[x])
      picture.transpose(PIL.Image.Transpose.FLIP_LEFT_RIGHT).save(str(uuid.uuid4())+'horizontal.jpg')


def rotate_save(rotateList):
  for x in range(len(rotateList)): 
      picture= Image.open(rotateList[x])
      picture.rotate(90).save(str(uuid.uuid4())+'rotated-90.jpg')
      picture.rotate(180).save(str(uuid.uuid4())+'rotated-180.jpg')
      picture.rotate(270).save(str(uuid.uuid4())+'rotated-270.jpg')


# Get the image directory
origImg = 'OriginalImages'
current_path = os.getcwd()
# Creat the full path
image_files = os.path.join(current_path,origImg)
# Drop into the image directory
os.chdir(image_files)
# Get a list of all images in the directory
myList = files2()
print(str('Original list: '),len(myList))
# Create Greyscale copies
createGreycopies(myList)
# Update list with new count.
myList2 = files2()
print(str('List with grey: '),len(myList2))
# Flip to the horizontal and save each image with a mirror opposite
flip_save(myList2)
# Update list with new count.
myList3 = files2()
# Now conduct the rotation and saving of each image by 90, 160 and 270 degrees.
rotate_save(myList3)
# Update list with new count.
myList4 = files2()
print(str('List with all images: '),len(myList4))