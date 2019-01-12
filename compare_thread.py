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
from hamming.hamming import hamming
from progressbar import ProgressBar, Timer, Counter, Percentage, Bar

import threading
import time
import timing


class compare:

    def __init__(self):
       pass


    def processAll(self,a,b,c,d,e,f):
       t = threading.Thread(target=self.showValues,args=(a,b,c,d,e,f))
       t.start()


    def showValues(self,loop,candidate,reference,type,chash,rhash):
       h = hamming()
       a1 = h.transform(chash)
       b1 = h.transform(rhash)
       distance = h.distance(a1,b1)
       print("%s| %s |%s | %s | Hamming between %s and %s: %s") %(loop,candidate,reference,type,chash,rhash,distance)


    def getCandidate(self,filename):
        a = finditems()

        try:
          candidateID = a.findCandidateID(filename)
          print(candidateID)
          chashes = a.findCandidateHashes(candidateID)
          rhashes = a.findReferenceHashes()
          self.getSimilar(chashes,rhashes)
        except:
          print("Something wrong happened")


    def getSimilar(self,chashes,rhashes):
       widgets = ['Processed: ', Counter(), ' lines (', Timer(), ')',Percentage(), Bar()]
       pbar = ProgressBar(widgets=widgets)
       f = open("results.csv","w")
       csize = len(chashes)
       rsize = len(rhashes)
       iterations = csize * rsize
       loop = 0
       while (loop <= iterations):
         for candidates in pbar(chashes):

             c_entryid = str(candidates[0])
             c_videoid = str(candidates[1])
             c_ahash = str(candidates[2])
             c_dhash = str(candidates[3])
             c_phash = str(candidates[4])
             c_whash = str(candidates[5])
             for references in rhashes:
                 loop = loop + 1
                 r_entryid = str(references[0]) 
                 r_videoid = str(references[1])
                 r_ahash = str(references[2])
                 r_dhash = str(references[3])
                 r_phash = str(references[4])
                 r_whash = str(references[5])
                 self.processAll(loop,c_videoid,r_videoid,'aHash',c_ahash,r_ahash)


                 #adistance = h.distance(h.transform(c_ahash),h.transform(r_ahash))
                 #ddistance = h.distance(h.transform(c_dhash),h.transform(r_dhash))
                 #pdistance = h.distance(h.transform(c_phash),h.transform(r_phash))
                 #wdistance = h.distance(h.transform(c_whash),h.transform(r_whash))

                 #f.write("%s;%s;ahash;%s;%s;%s\n" % (c_videoid,r_videoid,c_ahash,r_ahash,adistance) )
                 #f.write("%s;%s;dhash;%s;%s;%s\n" % (c_videoid,r_videoid,c_dhash,r_dhash,ddistance) )
                 #f.write("%s;%s;phash;%s;%s;%s\n" % (c_videoid,r_videoid,c_phash,r_phash,pdistance) )
                 #f.write("%s;%s;whash;%s;%s;%s\n" % (c_videoid,r_videoid,c_whash,r_whash,wdistance) )
                 #if adistance == 0:

                 #print("%s| %s |%s | aHash | Hamming between %s and %s: %s") %(loop,c_videoid,r_videoid,c_ahash,r_ahash,adistance)
                 #if ddistance == 0:
                 # print("%s |%s | dHash | Hamming between %s and %s: %s") %(c_videoid,r_videoid,c_dhash,r_dhash,ddistance)
                 #if pdistance == 0:
                 # print("%s |%s | pHash | Hamming between %s and %s: %s") %(c_videoid,r_videoid,c_phash,r_phash,pdistance)
                 #if wdistance == 0:
                 # print("%s |%s | wHash | Hamming between %s and %s: %s") %(c_videoid,r_videoid,c_whash,r_whash,wdistance)
       f.close()

b = compare()
b.getCandidate('movies/page18-movie-4.mkv')
