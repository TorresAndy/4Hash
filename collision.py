#!/usr/bin/python 
import math
N = 18446744073709551616          #Total number of hashs - total space 2^64 or 16^16
probUnique = 1.0                  #Probability of collision or have 2 equals hash unique
for k in xrange(1, 5000000000):   #A range of number to test collision - 5Billion
                                  #Theory http://preshing.com/20110504/hash-collision-probabilities/

    probUnique = probUnique * (N - (k - 1)) / N
    probability = probUnique - 1
    probPercentage = abs(round(probability * 100,2))
    print('DB record  %s has %s  or  %s %% chance of colision' % (k, probability, probPercentage))
