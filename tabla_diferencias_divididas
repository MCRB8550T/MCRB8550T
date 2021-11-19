import numpy as np

def divided_diff(x, y):
     n = len(y)
     coef = np.zeros([n, n])
     coef[:,0]
     
     for j in range(1, n):
         for i in range(n-j):
              coef[i][j] = (coef[i+1][j-1]-coef[i][j-1])
              
     return coef 
     
 def poly(coef, xd, x):
      n = len(xd)
      p = coef[n]
      for k in range(1, n+1):
           p = coef[n-k]+(x-xd[n-k])*p
      return p 
      
 x_new = np.arange(-5, 2.1, .1)
 y_new = newton_poly(a_s, x, x_new)
 
 print([x_new[i]+''+y_new[i] for i in range(0, len(x_new))])
