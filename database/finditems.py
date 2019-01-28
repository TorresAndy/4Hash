#!/usr/bin/python
#title                  :findiitems.py
#description            :Class to find values in database
#author                 :Anderson Torres
#date                   :20181124
#version                :1.0
#usage                  :called within class
#notes                  :
#python_version :2.6.6
#==============================================================================

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
                             "AND candidateFile.videohash = %s",(filename,))
        records = self.cursor.fetchall()
        if records:
           return records

   def findReferenceHashes(self,filename):
        self.cursor.execute("SELECT referenceHash.id,videoID,aHash,dHash,pHash,wHash FROM referenceHash,referenceFile "
                            "WHERE referenceHash.videoID = referenceFile.videohash " 
                            "AND referenceFile.videohash = %s",(filename,))
        records = self.cursor.fetchall()
        if records:
           return records
   
   def findCandidateFiles(self):
        self.cursor.execute("SELECT candidateFile.videohash, candidateFile.videoName FROM candidateFile")
        records = self.cursor.fetchall()
        if records:
           return records

   def findReferenceFiles(self):
        self.cursor.execute("SELECT referenceFile.videohash, referenceFile.videoName FROM referenceFile")
        records = self.cursor.fetchall()
        if records:
           return records


   def aHash(self,candidate,reference):
        self.cursor.execute("SELECT COUNT(A.adistance) as totalvalues " 
                            "FROM (SELECT bit_count(cast(conv(candidateHash.aHash,16,10) as UNSIGNED) ^ cast(conv(referenceHash.aHash,16,10)as UNSIGNED) ) as adistance "
                            "FROM candidateFile, candidateHash, referenceFile, referenceHash "
                            "WHERE candidateFile.videohash = candidateHash.videoID "
                            "AND referenceFile.videohash = referenceHash.videoID "
                            "AND candidateFile.videohash = %s "
                            "AND referenceFile.videohash = %s ) as A "
                            "WHERE A.adistance <= 13",(candidate,reference,))
        records = self.cursor.fetchall()
        if records:
           return records


   def dHash(self,candidate,reference):
        self.cursor.execute("SELECT COUNT(A.ddistance) as totalvalues " 
                            "FROM (SELECT bit_count(cast(conv(candidateHash.dHash,16,10) as UNSIGNED) ^ cast(conv(referenceHash.dHash,16,10)as UNSIGNED) ) as ddistance "
                            "FROM candidateFile, candidateHash, referenceFile, referenceHash "
                            "WHERE candidateFile.videohash = candidateHash.videoID "
                            "AND referenceFile.videohash = referenceHash.videoID "
                            "AND candidateFile.videohash = %s "
                            "AND referenceFile.videohash = %s ) as A "
                            "WHERE A.ddistance <= 13",(candidate,reference,))
        records = self.cursor.fetchall()
        if records:
           return records


   def pHash(self,candidate,reference):
        self.cursor.execute("SELECT COUNT(A.pdistance) as totalvalues " 
                            "FROM (SELECT bit_count(cast(conv(candidateHash.pHash,16,10) as UNSIGNED) ^ cast(conv(referenceHash.pHash,16,10)as UNSIGNED) ) as pdistance "
                            "FROM candidateFile, candidateHash, referenceFile, referenceHash "
                            "WHERE candidateFile.videohash = candidateHash.videoID "
                            "AND referenceFile.videohash = referenceHash.videoID "
                            "AND candidateFile.videohash = %s "
                            "AND referenceFile.videohash = %s ) as A "
                            "WHERE A.pdistance <= 13",(candidate,reference,))
        records = self.cursor.fetchall()
        if records:
           return records


   def wHash(self,candidate,reference):
        self.cursor.execute("SELECT COUNT(A.wdistance) as totalvalues " 
                            "FROM (SELECT bit_count(cast(conv(candidateHash.wHash,16,10) as UNSIGNED) ^ cast(conv(referenceHash.wHash,16,10)as UNSIGNED) ) as wdistance "
                            "FROM candidateFile, candidateHash, referenceFile, referenceHash "
                            "WHERE candidateFile.videohash = candidateHash.videoID "
                            "AND referenceFile.videohash = referenceHash.videoID "
                            "AND candidateFile.videohash = %s "
                            "AND referenceFile.videohash = %s ) as A "
                            "WHERE A.wdistance <= 13",(candidate,reference,))
        records = self.cursor.fetchall()
        if records:
           return records



   def dbclose(self):
      if self.db:
        self.db.close()
        print ("[INFO]")
        print (" - database Closed")






