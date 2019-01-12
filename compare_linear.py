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
import time
import timing
import codecs

class compare:

    def __init__(self,resultname):
        self.resultname =  resultname

    def getHashes(self,candidateName,referenceName):
        a = finditems()

        try:
          print("Processing %s versus %s") % (candidateName,referenceName)
          chashes = a.findCandidateHashes(candidateName)
          rhashes = a.findReferenceHashes(referenceName)
          self.getSimilar(chashes,rhashes)
        except:
          print("Something wrong happened")


    def getSimilar(self,chashes,rhashes):
       h = hamming()
       results = "/mnt/HD1/" + self.resultname
       f = codecs.open(results,"a",'utf-8-sig')
       f.write("loop;loop1;c_videoid;r_videoid;c_entryid;r_entryid;c_ahash;r_ahash;adistance;c_dhash;r_dhash;ddistance;c_phash;r_phash;pdistance;c_whash;r_whash;wdistance\n")

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

               f.write("%s;%s;'%s';'%s';%s;%s;'%s';'%s';%s;'%s';'%s';%s;'%s';'%s';%s;'%s';'%s';%s\n" %(loop,loop1,c_videoid,r_videoid,c_entryid,r_entryid,c_ahash,r_ahash,adistance,c_dhash,r_dhash,ddistance,c_phash,r_phash,pdistance,c_whash,r_whash,wdistance))

       f.close()

a = compare('comparacao_1.csv')
a.getHashes('movies/small.mkv','movies/small.mkv')

b = compare('comparacao_7.csv')
b.getHashes('movies/small.mkv','movies/beyond-white-space-trailer-1_h720p.mov')

c = compare('comparacao_2.csv')
c.getHashes('movies/small.mkv','movies/sample.mkv')

d = compare('comparacao_3.csv')
d.getHashes('movies/small.mkv','movies/bounty-killer-trailer-1_h720p.mov')

e = compare('comparacao_4.csv')
e.getHashes('movies/small.mkv','movies/once-upon-a-deadpool-trailer-1_h720p.mov')

f = compare('comparacao_5.csv')
f.getHashes('movies/small.mkv','movies/page18-movie-4.mkv')

g = compare('comparacao_6.csv')
g.getHashes('movies/small.mkv','movies/secret-life-of-pets-2-trailer-2_h720p.mov')

h = compare('comparacao_8.csv')
h.getHashes('movies/small.mkv','movies/the-vanishing-trailer-1_h720p.mov')

i = compare('comparacao_9.csv')
i.getHashes('movies/small.mkv','movies/almost-almost-famous-trailer-1-ca_h720p.mov')

j = compare('comparacao_10.csv')
j.getHashes('movies/small.mkv','movies/dead-in-a-week-trailer-1_h720p.mov')

k = compare('comparacao_11.csv')
k.getHashes('movies/small.mkv','movies/pokemon-detective-pikachu-trailer-1_h720p.mov')

l = compare('comparacao_12.csv')
l.getHashes('movies/small.mkv','movies/dumbo-trailer-2_h720p.mov')

m = compare('comparacao_13.csv')
m.getHashes('movies/small.mkv','movies/aquaman-trailer-3_h720p.mov')


