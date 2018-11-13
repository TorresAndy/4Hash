#!/usr/bin/python

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
