#!/usr/bin/python
import time 
import cv2 
import threading 
import imutils 
import json 



class frames:

   def __init__(self,location,video):
      self.location = location
      self.cap = cv2.VideoCapture(video)
      self.video_length = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
      self.video_fps = round(self.cap.get(cv2.CAP_PROP_FPS),2)
      self.video_time = round((self.video_length / self.video_fps),2)
      self.video_resolution = str(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)) + "/" + str(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT ))
      self.metadata = {}


   def saveImages(self,imagename,frame):
        t = threading.Thread(target=cv2.imwrite,args=(imagename,frame,))
        t.start()


   def info(self):
      print ("[INFO]")
      print (" - Video Reprodution time: %s seconds") %(self.video_time)
      print (" - Frame Rate: %s/fps") %(self.video_fps)
      print (" - Number of frames: %s") %(self.video_length)
      print (" - Video Resoltion: %s") %(self.video_resolution)
      self.metadata['video'] =[]
      self.metadata['frames'] =[]
      self.metadata['video'].append({
           'video_name':'video',
           'video_length':self.video_length,
           'video_fps':self.video_fps,
           'video_time':self.video_time,
           'video_resolution':self.video_resolution
           })


   def extract(self):
      # Log the time
      time_start = time.time()
      count = 0
      # Start converting the video
      print ("[INFO] Collecting metadata..")
      print ("[INFO] Extracting frames..\n")
      while self.cap.isOpened():
        ret, frame = self.cap.read() #Extracting Frames
        frame_time = round((self.cap.get(cv2.CAP_PROP_POS_MSEC)/1000),2)
        frame_name = self.location + "/%#05d_%s.jpg" % (count+1,frame_time)
        frame_small = imutils.resize(frame, width=640)
        # Calling function to save images in folder
        self.metadata['frames'].append({'framename':frame_name,'frametime':frame_time})
        self.saveImages(frame_name,frame_small)
        count = count + 1
        # If there are no more frames left
        video_length = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
        if (count > (video_length - 1)):
            # Log the time again
            time_end = time.time()
            # Release the feed
            self.cap.release()
            # Print stats
            print ("[INFO] Done extracting frames")
            print ("[INFO] It took %d seconds forconversion." % (time_end-time_start))
            break
      with open('metadata.json','w') as f:
          json.dump(self.metadata,f)
          f.close()
