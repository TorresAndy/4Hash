#!/usr/bin/python
class hamming:
    def __init__(self, a, b):
       self.a = a
       self.b = b
    def distance(self):
       lengthofa = len(self.a)
       lengthofb = len(self.b)
       if lengthofa != lengthofb:
          return False
       count = 0
       for i in range (0,lengthofa):
          if a[i] != b[i]:
             count += 1
       return count
