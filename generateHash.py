#!/usr/bin/python
from frameExtract import frames 
from hashImage import hashImage 
import os 
import sys 
import time 
import threading 
import concurrent.futures 



def usage():
    sys.stderr.write("""SYNOPSIS: %s [folder/location] [video file]
    Extract video frames and generates hashes using ImageHash functions:
    Average Hash, Difference Hash, Perceptual Hash and Wavelet Hash
    (C) Anderson Torres, 2018
      """ % sys.argv[0])
    sys.exit(1) 


def imagelocation(location):
    try:
        os.mkdir(location)
    except OSError:
        pass 

def is_image(filename,folder):
    f = filename.lower()
    if f.endswith(".png") or f.endswith(".jpg") or \
       f.endswith(".jpeg") or f.endswith(".bmp") or f.endswith(".gif") or '.jpg' in f:
       file = folder + "/" + f
       return file 

def images(location):
    filenames = []
    for root, dirs, files in os.walk(location):
       for filename in files:
           filenames.append(is_image(filename,location))
       return filenames 

def hashes(file):
    h = hashImage()
    print ("%s %s %s %s %s") %(file, h.ahash(file), h.dhash(file), h.phash(file), h.whash(file))


#if __name__ == '__main__':
with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
   folder = sys.argv[1] if len(sys.argv) > 2 else usage()
   video = sys.argv[2]
   imagelocation(folder)
   v = frames(folder,video)
   v.info()
   v.extract()
   files = images(folder)
   print("Generating hashes..\n")
   time.sleep(2)
   futures = [executor.submit(hashes, file) for file in sorted(files)]
      #a = threading.Thread(target=hashes,args=(file,)) a.start()
