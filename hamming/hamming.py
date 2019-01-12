#!/usr/bin/python
import binascii

class hamming:


    def __init__(self):
       pass


    def transform(self,hexvalue):
       integer = int(hexvalue,16)
       binvalue = format(integer,'0>64b')
       return binvalue


    def distance(self,a,b):
       lengthofa = len(a)
       lengthofb = len(b)
       if lengthofa != lengthofb:
          return False
       count = 0
       for i in range (0,lengthofa):
          if a[i] != b[i]:
             count += 1
       return count
