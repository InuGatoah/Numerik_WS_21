#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
from numpy import linalg as la

def cmp(a, b):
    return bool(a > b) - bool(a < b) 

def Householder(A):
    """Computes a QR-decomposition of the given matrix using the Householder 
       algorithm.
      \return A pair (NormalList,R) where NormalList is a list of Householder 
              normal vectors and R is an upper triangular matrix shaped like A.
      \sa ComputeQ """
    NormalList = []
    (m,n) = A.shape
    R = np.copy(A)
    
    for k in range(0,n):
        uk = np.zeros(m-k)
        for i in range(0,m-k):
            uk[i] = R[k+i][k]
        uk[0] = uk[0] + cmp(uk[0],0) * la.norm(uk)
        uk = uk / la.norm(uk)
        
        vk = np.zeros(m)
        for i in range(0, m-k):
            vk[k+i] = uk[i]
            
        R = R - 2 * np.dot(np.outer(vk,vk),R)
        NormalList.append(vk)
        
        for i in range(0,m):
            for j in range(0,n):
                if abs(R[i][j]) < 0.00000000001:
                    R[i][j] = 0
    
    return (NormalList,R)
	


def ComputeQ(NormalList):
    """Given a normal list such as the one returned by householder() this 
       function computes the corresponding orthogonal matrix."""
    m = NormalList[1].size
    Q = np.identity(m)
    
    for v in NormalList:
        Q = Q - np.dot(Q, 2*np.outer(v,v))
        
    return Q
	


if(__name__=="__main__"):
    A=np.random.rand(4,3)
    NormalList,R=Householder(A)
    Q=ComputeQ(NormalList)
    print("The following matrix should be upper triangular:")
    print(R)
    print("If the solution consitutes a decomposition, the following is near zero:")
    print(la.norm(A-np.dot(Q,R)))
    print("If Q is unitary, the following is near zero:")
    print(la.norm(np.dot(Q.T,Q)-np.eye(Q.shape[0])))


# In[ ]:




