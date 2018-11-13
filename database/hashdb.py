#!/usr/bin/python
import mysql.connector

class hashdb:

   def __init__(self):
      self.db = mysql.connector.connect(user='hashdb', password='And3rs0nT0rr3s',host='localhost', database='hashdb')
      self.cursor = self.db.cursor()
      print ("[INFO]")
      print (" - database Connected")

   def referenceVideo(self,videohash,videoName,videoPath,videoResolution,videoDuration,videofps,videoFrames):
        self.cursor.execute('''INSERT INTO referenceFile
                            (videohash,videoName, videoPath, videoResolution, videoDuration, videoFrames,videofps)
                            VALUES(%s,%s,%s,%s,%s,%s,%s)''',(videohash,videoName, videoPath, videoResolution, videoDuration, videoFrames,videofps))
        self.db.commit()

   def candidateVideo(self,videohash, videoName, videoPath,videoResolution,videoDuration,videofps,videoFrames):
        self.cursor.execute('''INSERT INTO candidateFile(videohash,videoName, videoPath, videoResolution, videoDuration, videoFrames,videofps)
                      VALUES(%s,%s,%s,%s,%s,%s,%s)''', (videohash,videoName, videoPath, videoResolution, videoDuration, videoFrames, videofps))
        self.db.commit()

   def referenceHash(self, videoID, frameName, aHash, dHash, pHash, wHash):
      self.cursor.execute('''INSERT INTO referenceHash(videoID, frameName, aHash, dHash, pHash, wHash)
                      VALUES(%s,%s,%s,%s,%s,%s)''', (videoID, frameName, aHash, dHash, pHash, wHash))
      self.db.commit()

   def candidateHash(self, videoID, frameName, aHash, dHash, pHash, wHash):
      self.cursor.execute('''INSERT INTO referenceHash(videoID, frameName, aHash, dHash, pHash, wHash)
                      VALUES(%s,%s,%s,%s,%s,%s)''', (videoID, frameName, aHash, dHash, pHash, wHash))
      self.db.commit()

   def referenceUnique(self,videohash):
      self.cursor.execute("SELECT * FROM referenceFile WHERE videohash = %s" , (videohash,))
      exists = self.cursor.fetchone()
      if not exists:
         return True
      else:
         return  False

   def candidateUnique(self,videohash):
      self.cursor.execute("SELECT * FROM candidateFile WHERE videohash = %s" , (videohash,))
      exists = self.cursor.fetchone()
      if not exists:
         return True
      else:
         return  False


   def dbclose(self):
      if self.db:
        self.db.close()
        print ("[INFO]")
        print (" - database Closed")



