#!/usr/bin/python
#title			:compare.py
#description		:Compare Perceptual Hashes
#author			:Anderson Torres
#date			:20181124
#version		:1.0
#usage			:python compare_linear.py
#notes			:
#python_version	:2.6.6
#==============================================================================

from database.finditems import finditems
from hamming.hamming import hamming
from progressbar import ProgressBar, Timer, Counter, Percentage, Bar
import time
import timing
import codecs

class compare:

    def __init__(self):
        self.a = finditems()

    def getValues(self,candID,candName,refeID,refeName):

        try:
          print("Processing %s| %s") % (candName,refeName)
          filename = candID + "_x_" + refeID + ".csv"
          chashes = self.a.findCandidateHashes(candID)
          rhashes = self.a.findReferenceHashes(refeID)
          self.getSimilar(chashes,rhashes,filename)
        except:
          print("Something wrong happened")


    def getSimilar(self,chashes,rhashes,filename):
       results = "/mnt/HD1/comparacoes/software/" + filename

       h = hamming()
       f = codecs.open(results,"a",'utf-8-sig')
       f.write("loop;loop1;c_videoid;r_videoid;c_entryid;r_entryid;c_hash;r_hash;distance;hash\n")

       loop = 0
       loop1 = 0
       loop2 = 0

       widgets = ['Processed: ', Counter(), ' lines (', Timer(), ')',Percentage(), Bar()]
       pbar = ProgressBar(widgets=widgets)

       for candidates in pbar(chashes):
           loop = loop + 1
           c_entryid = str(candidates[0])
           c_videoid = str(candidates[1])
           c_ahash = str(candidates[2])
           c_dhash = str(candidates[3])
           c_phash = str(candidates[4])
           c_whash = str(candidates[5])
           for references in rhashes:
               loop1 = loop1 + 1
               r_entryid = str(references[0]) 
               r_videoid = str(references[1])
               r_ahash = str(references[2])
               r_dhash = str(references[3])
               r_phash = str(references[4])
               r_whash = str(references[5])

               adistance = h.distance(h.transform(c_ahash),h.transform(r_ahash))
               ddistance = h.distance(h.transform(c_dhash),h.transform(r_dhash))
               pdistance = h.distance(h.transform(c_phash),h.transform(r_phash))
               wdistance = h.distance(h.transform(c_whash),h.transform(r_whash))
               if adistance <= 13:
                  f.write("%s;%s;'%s';'%s';%s;%s;'%s';'%s';%s;ahash\n" %(loop,loop1,c_videoid,r_videoid,c_entryid,r_entryid,c_ahash,r_ahash,adistance))
               if ddistance <= 13:
                  f.write("%s;%s;'%s';'%s';%s;%s;'%s';'%s';%s;dhash\n" %(loop,loop1,c_videoid,r_videoid,c_entryid,r_entryid,c_dhash,r_dhash,ddistance))
               if pdistance <= 13:
                  f.write("%s;%s;'%s';'%s';%s;%s;'%s';'%s';%s;phash\n" %(loop,loop1,c_videoid,r_videoid,c_entryid,r_entryid,c_phash,r_phash,pdistance))
               if wdistance <= 13:
                  f.write("%s;%s;'%s';'%s';%s;%s;'%s';'%s';%s;whash\n" %(loop,loop1,c_videoid,r_videoid,c_entryid,r_entryid,c_whash,r_whash,wdistance))
       f.close()


    def getFiles(self):
        candidates = self.a.findCandidateFiles()
        references = self.a.findReferenceFiles()
        for candidate in candidates:
            candID = str(candidate[0])
            candName = str(candidate[1])

            for reference in references:
                refeID = str(reference[0])
                refeName = str(reference[1])
                self.getValues(candID,candName,refeID,refeName)

a = compare()
a.getFiles()

