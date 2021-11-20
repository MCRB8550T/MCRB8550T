matriz triangular inferior para la tabla de diferencias divididas

import numpy as np
import matplotlib.pyplot as plt

from copy import deepcopy



def dd(x, i, j):
  return x[i+j]-x[i]

'''
la matriz triangular inferior para la table de diferencias dividas
'''
def matriz_ti(x, y):
  n = len(x)
  rows = [["0" for i in range(0, n)] for i in range(0, n)]
  ri = -1
  for row in rows:
    print("ligne a nouveau \n")
    ci=-1
    ri += 1
    for col in row:
      print("colone a nouveau... \n")
      ci +=1
      if ci==0:
        print("zeroth column:")
        rows[ri][ci]="1"
        print(rows[ri][ci])
      elif(ci<=ri):
        print("le nombre de colone est moins o egal!")
        prod = ""
        for k in range(0, ci):
          prod = prod + "(x_"+str(ci)+"-x_"+str(k)+")"
        print(str(ri)+","+str(ci))
        print(prod)
        rows[ri][ci]=prod
      else:
        print("de lo contrario, caso alcanzado!")
        print(str(ri)+","+str(ci)+"(2)")
        print(rows[ri][ci])
     return rows
