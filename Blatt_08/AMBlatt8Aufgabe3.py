#!/usr/bin/env python
# coding: utf-8

# In[14]:


from math import sqrt
from pprint import pprint
 
def cholesky(A):
    n = len(A)

    # Create zero matrix for L
    rows, cols = n,n
    L = [([0]*cols) for i in range(rows)]

    # Perform the Cholesky decomposition
    for i in range(n):
        for k in range(i+1):
            tmp_sum = sum(L[i][j] * L[k][j] for j in range(k))
            
            if (i == k): # Diagonal elements
                L[i][k] = sqrt(A[i][i] - tmp_sum)
            else:
                L[i][k] = (1.0 / L[k][k] * (A[i][k] - tmp_sum))
    return L
 
A = [[6, 3, 4, 8], [3, 6, 5, 1], [4, 5, 10, 7], [8, 1, 7, 25]]
P = cholesky(A)


print("A =" , A)
print("P = " , P)


# In[20]:


from math import sqrt
from pprint import pprint
 
def cholesky(A):
    n = len(A)

    # Create zero matrix for L
    rows, cols = n,n
    L = [([0]*cols) for i in range(rows)]

    # Perform the Cholesky decomposition
    for i in range(n):
        for k in range(i+1):
            tmp_sum = sum(L[i][j] * L[k][j] for j in range(k))
            
            if (i == k): # Diagonal elements
                L[i][k] = sqrt(A[i][i] - tmp_sum)
            else:
                L[i][k] = (1.0 / L[k][k] * (A[i][k] - tmp_sum))
    return L
 

B = [[1, 2], [1, 1]]
N = cholesky(B)


print("B =" , B)
print("N = " , N)
#obwohl es normalerweise nicht durchfuerhbar ist, gibt das program ein "loesubg" 


# In[ ]:




