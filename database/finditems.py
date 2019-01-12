#!/usr/bin/python
import mysql.connector
from dbconnect import dbconnect



class finditems:

   def __init__(self):
      self.a = dbconnect()
      self.db = self.a.connect()
      self.cursor = self.db.cursor()
      print ("[INFO]")
      print (" - database Connected")

   def findCandidateID(self,filename):
        self.cursor.execute("SELECT videohash FROM candidateFile WHERE videoName = %s",(filename,))
        records = self.cursor.fetchall()
        for row in records:
            candidateID = row[0]
        return candidateID

   def findCandidateHashes(self,filename):
        self.cursor.execute("SELECT candidateHash.id,videoID,aHash,dHash,pHash,wHash FROM candidateHash,candidateFile "
                             "WHERE candidateHash.videoID = candidateFile.videohash "
                             "AND candidateFile.videoName = %s",(filename,))
        #self.cursor.execute("SELECT id,videoID,aHash,dHash,pHash,wHash FROM candidateHash WHERE videoID = %s",(candidateID,))
        records = self.cursor.fetchall()
        if records:
           return records

   def findReferenceHashes(self,filename):
        self.cursor.execute("SELECT referenceHash.id,videoID,aHash,dHash,pHash,wHash FROM referenceHash,referenceFile "
                            "WHERE referenceHash.videoID = referenceFile.videohash " 
                            "AND referenceFile.videoname = %s",(filename,))
        records = self.cursor.fetchall()
        if records:
           return records



   def dbclose(self):
      if self.db:
        self.db.close()
        print ("[INFO]")
        print (" - database Closed")






