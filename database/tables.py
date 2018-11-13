#!/usr/bin/python

#import sqlite3
import mysql.connector


conn = mysql.connector.connect(user='hashdb', password='And3rs0nT0rr3s',host='localhost', database='hashdb')
cursor = conn.cursor()

TABLES = {}

TABLES['referenceFile'] = (
         "CREATE TABLE `referenceFile`("
         " `id` INT(11) NOT NULL AUTO_INCREMENT,"
         " `videohash` VARCHAR(160) NOT NULL,"
         " `videoName` VARCHAR(200) NOT NULL,"
         " `videoPath` VARCHAR(1000) NOT NULL,"
         " `videoResolution` VARCHAR(30) NOT NULL,"
         " `videoDuration` VARCHAR(20) NOT NULL,"
	 " `videoFrames` INT(10) NOT NULL,"
	 " `videofps` VARCHAR(10) NOT NULL,"
         " PRIMARY KEY (`id`)"
         ") ENGINE=InnoDB")

TABLES['referenceHash'] = (
         "CREATE TABLE `referenceHash`("
         " `id` INT(11) NOT NULL AUTO_INCREMENT,"
         " `videoID` VARCHAR(160) NOT NULL,"
         " `frameName` VARCHAR(2000) NOT NULL,"
	 " `aHash` VARCHAR(30) NOT NULL,"
	 " `dHash` VARCHAR(30) NOT NULL,"
	 " `pHash` VARCHAR(30) NOT NULL,"
	 " `wHash` VARCHAR(30) NOT NULL,"
         " PRIMARY KEY (`id`)"
         ") ENGINE=InnoDB")


TABLES['candidateFile'] = (
         "CREATE TABLE candidateFile("
         " `id` INT(11) NOT NULL AUTO_INCREMENT,"
         " `videohash` VARCHAR(160) NOT NULL,"
         " `videoName` VARCHAR(200) NOT NULL,"
         " `videoPath` VARCHAR(1000) NOT NULL,"
         " `videoResolution` VARCHAR(30) NOT NULL,"
         " `videoDuration` VARCHAR(20) NOT NULL,"
	 " `videoFrames` INT(10) NOT NULL,"
	 " `videofps` VARCHAR(10) NOT NULL,"
         " PRIMARY KEY (`id`)"
         ") ENGINE=InnoDB")

TABLES['candidateHash'] = (
         "CREATE TABLE candidateHash("
         " `id` INT NOT NULL AUTO_INCREMENT,"
         " `videoID` VARCHAR(160) NOT NULL,"
         " `frameName` VARCHAR(2000) NOT NULL,"
	 " `aHash` VARCHAR(30) NOT NULL,"
	 " `dHash` VARCHAR(30) NOT NULL,"
	 " `pHash` VARCHAR(30) NOT NULL,"
	 " `wHash` VARCHAR(30) NOT NULL,"
         " PRIMARY KEY (`id`)" 
         ") ENGINE=InnoDB")



for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name))
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("Table already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

cursor.close()
conn.close()
