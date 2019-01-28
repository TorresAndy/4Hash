#!/usr/bin/python
#title                  :frames.py
#description            :Extract all frames from a video file
#author                 :Anderson Torres
#date                   :20181124
#version                :1.0
#usage                  :called within class
#notes                  :
#python_version :2.6.6
#==============================================================================

import timing
import cv2
import threading
import imutils



class extraction:

   def __init__(self,location,video):
      self.location = location
      self.cap = cv2.VideoCapture(video)
      self.video_length = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
      self.video_fps = round(self.cap.get(cv2.CAP_PROP_FPS),2)
      self.video_time = round((self.video_length / self.video_fps),2)
      self.video_resolution = str(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)) + "/" + str(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT ))


   def saveImages(self,imagename,frame):
        t = threading.Thread(target=cv2.imwrite,args=(imagename,frame,))
        t.start()


   def info(self):
      print ("[INFO]")
      print (" - Video Reprodution time: %s seconds") %(self.video_time)
      print (" - Frame Rate: %s/fps") %(self.video_fps)
      print (" - Number of frames: %s") %(self.video_length)
      print (" - Video Resolution: %s") %(self.video_resolution)


   def extract(self):
      count = 0

      # Start converting the video
      print ("[INFO]")
      print (" - Starting frames extraction")

      while self.cap.isOpened():
        ret, frame = self.cap.read() #Extracting Frames
        frame_time = round((self.cap.get(cv2.CAP_PROP_POS_MSEC)/1000),2)
        frame_name = self.location + "/%#05d_%s.jpg" % (count+1,frame_time)
        frame_small = imutils.resize(frame, width=640) #Resizing the frame to save space and processing
        # Calling function to save images in folder
        self.saveImages(frame_name,frame_small)
        count = count + 1
        # If there are no more frames left
        video_length = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
        if (count > (video_length - 1)):
            # Release the feed
            self.cap.release()
            # Print status
            print ("[INFO]")
            print (" - Done extracting frames")
            break
