#!/usr/bin/python
#title			:dbconnect.py
#description		:Class to connect to the MYSQL database
#author			:Anderson Torres
#date			:20181116
#version		:0.1
#usage			:python dbconnect.py
#notes			:
#python_version	:2.6.6
#==============================================================================

import yaml
import mysql.connector

class dbconnect:

   def __init__(self):
       pass


   def connect(self):
       with open('database/config.yml', 'r') as ymlfile:
           cfg = yaml.load(ymlfile)

       dbhost = cfg['mysql']['host']
       dbdatabase= cfg['mysql']['database']
       dbuser = cfg['mysql']['user']
       dbpassword = cfg['mysql']['password']

       db = mysql.connector.connect(user=dbuser, password=dbpassword,host=dbhost, database=dbdatabase)

       return db
