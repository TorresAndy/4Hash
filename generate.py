#!/usr/bin/python

#    Extract video frames and generates hashes using ImageHash functions:
#    Average Hash, Difference Hash, Perceptual Hash and Wavelet Hash
#    (C) Anderson Torres, 2018

from frames import extraction
from perceptive import hash
from database.hashdb import hashdb

import os
import time
import hashlib
import json
#import threading
#import concurrent.futures


class generate:
   """ Main class that call the perceptual hash methods """

   def __init__(self,video):
      """ Initiating the class
      Parameters
      ----------
      video: object
         The actual videofile to be processed

      """

      self.video = video
      self.frameslocation = ''

   def location(self):
      """ Generate the folder based on the video file sha1 string """

      hash_object = hashlib.sha1(self.video)
      self.videosha = hash_object.hexdigest()  # sha1 hash to distinguish the video file and make it unique in the database
      self.frameslocation = "frames/" + self.videosha

      try:
         print ("[INFO]")
         print (" - Fingerprinting process started")
         print (" - Frames folder created with name: %s") %(self.videosha)
         os.mkdir(self.frameslocation)

      except OSError:
         pass

   def framesextraction(self):
       """ Calls the method that will actually extract the video frames """
       self.location()
       self.v = extraction(self.frameslocation,self.video)
       self.v.info()                #  Prints the video information
       self.v.extract()             #  The actual frame extraction
       print ("[INFO]")
       print (" - Frames extraction completed")


   def is_image(self,filename,folder):
       """ Check if the files within the folder are actually images that can be processed
           return the full name of the frame file
       """
       f = filename.lower()
       if f.endswith(".png") or f.endswith(".jpg") or \
          f.endswith(".jpeg") or f.endswith(".bmp") or f.endswith(".gif") or '.jpg' in f:
          file = folder + "/" + f
       return file

   def images(self):
       """ Generate a list with the frames files names """
       filenames = []
       try:
          for root, dirs, files in os.walk(self.frameslocation):
              for filename in files:
                  filenames.append(self.is_image(filename,self.frameslocation))
          return filenames

       except OSError:
         pass

   def dbcheck(self,videotype):
       d = hashdb()
       if videotype == 'reference':
          if d.referenceUnique(self.videosha):
             d.referenceVideo(self.videosha,self.video,self.frameslocation,self.v.video_resolution,self.v.video_time,self.v.video_fps,self.v.video_length)
             self.hashes(videotype)
          else:
             print("INFO]")
             print(" - Reference Video already exist")
             print(" - Nothing to do")
       elif videotype == 'candidate':
          if d.candidateUnique(self.videosha):
             d.candidateVideo(self.videosha,self.video,self.frameslocation,self.v.video_resolution,self.v.video_time,self.v.video_fps,self.v.video_length)
             self.hashes(videotype)
          else:
             print("INFO]")
             print(" - Candidate Video already exist")
             print(" - Nothing to do")


   def hashes(self,videotype):
       """ Print the hashes for Generate a list with the frames files names """
       """ Generate a list with the frames files names """
       print("[INFO]")
       print(" - Generating hashes..\n")
       d = hashdb()
       files = self.images()
       time.sleep(5)
       h = hash()
       for file in sorted(files):




           ahash = str(h.ahash(file))
           dhash = str(h.dhash(file))
           phash = str(h.phash(file))
           whash = str(h.whash(file))



           print ("%s %s %s %s %s %s") %(self.videosha,file, ahash, dhash, phash, whash)

           if videotype == 'reference':
              d.referenceHash(self.videosha, file, ahash, dhash, phash, whash)
           elif videotype == 'candidate':
              d.candidateHash(self.videosha, file, ahash, dhash, phash, whash)


       d.dbclose()
       # with open('database/hashes.json','w') as f:
       #   json.dump(LINES,f)
       #   f.close()

   #def imagehash(self):
       #with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
       #    futures = [executor.submit(self.hashes, file) for file in sorted(files)]




a = generate('movies/sample.mkv')
a.framesextraction()
a.dbcheck('reference')
