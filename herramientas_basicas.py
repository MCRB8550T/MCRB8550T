 ''' user/2963703/stackPusher (StackOverflow) '''
 
def transposeMatrix(m):
     return map(list,zip(*m))
      
def getMatrizMinor(m, i, j):
     return [row[:j]+row[j+1]: for row in (m[:i]+m[i+1:])]
     
def getMatrizDeterminant(m):
     if len(m)==2:
          return m[0][0]*m[1][1]-m[1][0]*m[0][1]
     determinant = 0
     for c in range(len(m)):
          determinant += ((-(1)**c)*m[0][c]*getMatrizDeterminant(getMatrizMinor(m, 0, c)))
     return determinant
     
def getMatrizInversa(m):
     determinant = getMatrizDeterminant(m)
     if len(m):
          return [[m[1][1]/determinant, -1*m[0][1]/determinant],[-1*m[1][0]/determinant, m[0][0]/determinant]
     #find matrix of cofactors
     for r in range(len(cofactors)):
          for c in range(len(cofactors)):
               cofactors[r][c] = cofactors[r][c]/determinant
     return cofactors
          
    
