# Process to capture , each frame of a video file and save it as its own image.
# This will give you N X images based on the frame rate and video length.
# Becaues taking a video of the object is easier than scraping google for the images you need.
# 12 Feb 2023
# Michael J. Stattelman
#/////////////////////////////////////////////////////////////////////////////////////////
# python split_videos_in_dir__into_images.py
import cv2
import glob
import os
import uuid


dirname = 'videos/'
outDir = 'images/'

def getFileName(vidFile):
  head,tail = os.path.split(os.path.splitext(vidFile)[0])
  return str(tail)

def createDir(pathname,Dirname,vidFile):
  path = os.path.join(pathname, Dirname)
  createdDir = os.mkdir(path)
  createFrames(path,vidFile)


def createFrames(outDir,vidInput):
  vidcap = cv2.VideoCapture(vidInput)
  success,image = vidcap.read()
  count = 0
  while success:
    cv2.imwrite(str(outDir+"/")+"frame%d.jpg" % count, image)     # save frame as JPEG file      
    success,image = vidcap.read()
    print('Read a new frame: ', success)
    count += 1

def renameImages(dirCreated): 
  srcDir = outDir+dirCreated
  for count, filename in enumerate(os.listdir(srcDir)): 
    dst = str(uuid.uuid4()) + ".jpg"
    src = srcDir + filename 
    dst = srcDir + dst 
    # rename all the files 
    os.rename(src, dst) 


vidfiles = []
for file in glob.glob(dirname+"*.mp4"):
    vidfiles.append(file)

#print(len(vidfiles))

for vFile in vidfiles:
  print(str(vFile))
  newDirName = getFileName(vFile)
  createDir(outDir,newDirName,vFile)
  renameImages(newDirName+"/")