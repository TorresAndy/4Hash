#!/usr/bin/python
import mysql.connector
from dbconnect import dbconnect
from progressbar import ProgressBar, Timer, Counter, Percentage, Bar


class finditems:

   def __init__(self):
      self.a = dbconnect()
      self.db = self.a.connect()
      self.cursor = self.db.cursor()
      print ("[INFO]")
      print (" - database Connected")

   def calculateHashes(self):
        self.cursor.execute("SELECT "
                            "    candidateHash.id as recordID,"
                            "    candidateFile.videoHash as candidate,"
                            "    referenceFile.videoHash as reference,"
                            "    candidateHash.aHash as c_ahash,"
                            "    referenceHash.aHash as r_ahash,"
                            "    bit_count(cast(conv(candidateHash.aHash,16,10) as UNSIGNED) ^ cast(conv(referenceHash.aHash,16,10)as UNSIGNED) ) as adistance,"
                            "    candidateHash.dHash as c_dhash,"
                            "    referenceHash.dHash as r_dhash,"
                            "    bit_count(cast(conv(candidateHash.dHash,16,10) as UNSIGNED) ^ cast(conv(referenceHash.dHash,16,10)as UNSIGNED) ) as ddistance, "
                            "    candidateHash.pHash as c_phash,"
                            "    referenceHash.pHash as r_phash, "
                            "    bit_count(cast(conv(candidateHash.pHash,16,10) as UNSIGNED) ^ cast(conv(referenceHash.pHash,16,10)as UNSIGNED) ) as pdistance, "
                            "    candidateHash.wHash as c_whash, "
                            "    referenceHash.wHash as r_whash, "
                            "    bit_count(cast(conv(candidateHash.wHash,16,10) as UNSIGNED) ^ cast(conv(referenceHash.wHash,16,10)as UNSIGNED) ) as wdistance "
                            "    FROM candidateFile, candidateHash, referenceFile, referenceHash "
                            "    WHERE candidateFile.videohash = candidateHash.videoID")
        size = 200000
        loop = 0
        loop1 = 0
        widgets = ['Processed: ', Counter(), ' lines (', Timer(), ')',Percentage(), Bar()]
        pbar = ProgressBar(widgets=widgets,maxval=4000).start()

        f =  open("/mnt/HD1/results.csv","w")
        while True:
             records = self.cursor.fetchmany(size)
             loop1 = loop1 + 1
             pbar.update(loop1)
             if not records:
                break
             for row in records:
                 loop = loop +  1 
                 #print("%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s") % (loop1,loop,row[0],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14])
                 f.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (loop1,loop,row[0],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14]))
        pbar.finish()  



   def dbclose(self):
      if self.db:
        self.db.close()
        print ("[INFO]")
        print (" - database Closed")



a = finditems()
a.calculateHashes()
a.dbclose()
