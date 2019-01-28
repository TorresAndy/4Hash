#!/usr/bin/python
#title			:compare.py
#description		:Compare Perceptual Hashes
#author			:Anderson Torres
#date			:20181124
#version		:1.0
#usage			:python compare.py
#notes			:
#python_version	:2.6.6
#==============================================================================

from database.finditems import finditems
from progressbar import ProgressBar, Timer, Counter, Percentage, Bar
import timing
import time
import codecs
import csv

class compare:
    def __init__(self):
        self.a = finditems()

    def getValues(self,candID,candName,refeID,refeName):

        try:
          a = self.a.aHash(candID,refeID)
          d = self.a.dHash(candID,refeID)
          p = self.a.pHash(candID,refeID)
          w = self.a.wHash(candID,refeID)
          for hash in a:
              ahash = str(hash[0])
          for hash in d:
              dhash = str(hash[0])
          for hash in p:
              phash = str(hash[0])
          for hash in w:
            whash = str(hash[0])

          print("%s| %s | %s | %s | %s | %s") % (candName,refeName,ahash,dhash,phash,whash)

        except:
          print("[ERROR] Something wrong happened")

    def getFiles(self):
        candidates = self.a.findCandidateFiles()
        references = self.a.findReferenceFiles()
        #for candidate in candidates:
        #    candID = str(candidate[0])
        #    candName = str(candidate[1])  
        for reference in references: 
            refeID = str(reference[0])
            refeName = str(reference[1])
            self.getValues('ee4913c4d3cd680779dde9cb205383dde976c835','movies/deadpool_flipped_10.mov',refeID,refeName)

a = compare()
a.getFiles()


