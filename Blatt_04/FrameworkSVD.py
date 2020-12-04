import numpy as np
from numpy.linalg import eig
import math 

def RandomVector(V):
    b,n = V.shape
    v = np.random.rand(n)
    v = v / np.linalg.norm(v)
    return v


def ComputeSVD(A):
    m,n = A.shape
    B = np.dot(A.T, A)
    w , V = np.linalg.eig(B)
    #V berechnen
    a,b = V.shape
    V = np.transpose(V)
    for i in range(b,n):
        V = np.append(V, RandomVector(V))
    V = np.transpose(V)
    #Sigma berechnen
    Sigma = np.zeros((m,n))
    for i in range(min(n, w.size)):
        Sigma[i,i] = math.sqrt(w[i])
    #U berechnen
    U = np.dot(A,V)
    for i in range(n):
        U[:,i] = U[:,i] / Sigma[i,i]
    U = np.transpose(U)
    for i in range(m-n):
        U = np.append(U,RandomVector(U))
    U = np.reshape(U, (m,m))
    U = np.transpose(U)
    return (U,Sigma,V.T)


def PseudoInverse(A):
    U, Sigma , V = ComputeSVD(A)
    m,n = A.shape
    for i in range(n):
        if Sigma[i,i] != 0:
            Sigma[i,i] = 1.0/Sigma[i,i]
    Sigma = np.transpose(Sigma)
    V = np.transpose(V)
    U = np.transpose(U)
    return np.dot(V, np.dot(Sigma,U))
    

def LinearSolve(A, b):
    P = PseudoInverse(A)
    return np.dot(P,b)

if (__name__ == "__main__"):
    # Try the SVD decomposition
    A = np.matrix([
        [1.0,1.0,1.0],
        [1.0,2.0,3.0],
        [1.0,4.0,9.0],
        [1.0,8.0,27.0]
    ])
    U, Sigma, V = ComputeSVD(A)
    print ("U =" , U)
    print ("Sigma = " , Sigma)
    print ("V = " , V)
    print("If the following numbers are nearly zero, SVD seems to be working.")
    print(np.linalg.norm(U*Sigma*V.H - A))
    print(np.linalg.norm(U.H*U-np.eye(3)))
    print(np.linalg.norm(V.H*V-np.eye(3)))
    # Try solving a least squares system
    b = np.matrix([1.0,2.0,3.0,4.0]).T
    x = LinearSolve(A,b)
    print("If the following number is nearly zero, linear solving seems to be working.")
    print(np.linalg.norm(x-np.linalg.lstsq(A,b)[0]))
