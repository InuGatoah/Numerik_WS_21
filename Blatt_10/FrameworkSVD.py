import numpy as np
from scipy import io
from matplotlib import pyplot

def ComputeSVD(A):
    """Given a quadratic matrix this function computes the singular value 
       decomposition of this matrix using a stable numerical scheme.
      \return A triple (U,Sigma,V) of matrices of shape identical to A such that 
              U.dot(Sigma).dot(np.conj(V.T)) provides a singular value decomposition 
              of A. The singular values should be in descending order."""
    


def VerifySVD(A,U,Sigma,V):
    """This function checks whether the given square matrices provide an SVD of the 
       square matrix A. Results are printed."""
    # Test whether the matrices provide a factorization
    DeltaA=U.dot(Sigma).dot(np.conj(V.T))
    print("The relative error of U*Sigma*V^* is:")
    print(np.linalg.norm(A-DeltaA)/np.linalg.norm(A))
    # Test whether U and V are unitary
    print("If U is unitary, the following number should be near zero:")
    print(np.linalg.norm(np.eye(A.shape[0])-U.dot(np.conj(U.T))))
    print("If V is unitary, the following number should be near zero:")
    print(np.linalg.norm(np.eye(A.shape[1],A.shape[1])-V.dot(np.conj(V.T))))
    print("")


if(__name__=="__main__"):
    # Construct a random matrix for testing
    MatrixSize=40
    RandomMatrix=np.random.rand(MatrixSize,MatrixSize)
    # Test ComputeSVD()
    print("Testing ComputeSVD():")
    U,Sigma,V=ComputeSVD(RandomMatrix)
    VerifySVD(RandomMatrix,U,Sigma,V)
   