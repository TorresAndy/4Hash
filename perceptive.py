#!/usr/bin/python
#title                  :perceptive.py
#description            :generate Perceptual Hashes
#author                 :Anderson Torres
#date                   :20181124
#version                :1.0
#usage                  :called within class -  image as parameter
#notes                  :
#python_version :2.6.6
#==============================================================================

from PIL import Image
import imagehash

class hash:
   def __init__(self):
      pass

   def ahash(self, image):
      h = imagehash.average_hash(Image.open(image))
      return h

   def dhash(self, image):
      h = imagehash.dhash(Image.open(image))
      return h

   def phash(self, image):
      h = imagehash.phash(Image.open(image))
      return h

   def whash(self, image):
      h = imagehash.whash(Image.open(image))
      return h
