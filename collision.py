#!/usr/bin/python

import threading
probUnique = 1.0       #Constante, probabilidade de se ter dois valores iguais.

def domath(n,k):
   t = threading.Thread(target=collision, args=(n,k))
   t.start()

def collision(N,k):
      #Teoria http://preshing.com/20110504/hash-collision-probabilities/
      global probUnique  #Para modificar a variável global
      probUnique = probUnique * (N - (k - 1)) / N
      probability = probUnique - 1
      probPercentage = abs(round(probability * 100,2))
      print('Registro  %s tem %s  ou  %s %% chances de colisao' % (k, probability, probPercentage))

#N = 18446744073709551616          #Universo de hashs possiveis -  2^64 or 16^16
N = 256          #Universo de hashs possiveis -  2^64 or 16^16
for k in range(1, 256):   #Numero de hash gerados - 5Billion
   domath(N,k)
