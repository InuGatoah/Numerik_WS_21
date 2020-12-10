import numpy as np
from scipy import linalg

def QR(A):
    """Given a matrix A with full column rank this function uses the classical 
       Gram-Schmidt algorithm to compute a QR decomposition. It returns a tuple 
       (Q,R) of np.matrix objects with Q having shape identical to A and Q*R=A."""
    
    n, m = A.shape
    Q = np.zeros((n, m))
    R = np.zeros((m, m))
    
    for j in range(m):
        R[j, j] = np.linalg.norm(A[:, j:j+1].reshape(-1), 2)
        Q[:, j:j+1] = A[:, j:j+1]/R[j, j]
        R[j:j+1, j+1:m+1] = np.dot(Q[:, j:j+1].T, A[:, j+1:m+1])
        A[:, j+1:m+1] = A[:, j+1:m+1] - np.dot(Q[:, j:j+1], R[j:j+1, j+1:m+1])
        
    return np.asmatrix(Q), np.asmatrix(R)     


def BackSubstitution(R: np.matrix, y: np.ndarray):
    """Given a square upper triangular matrix R and a vector y of same size this 
       function solves R*x=y using backward substitution and returns x."""


def LeastSquares(A, b):
    """Given a matrix A and a vector b this function solves the least squares 
       problem of minimizing |A*x-b| and returns the optimal x."""


if(__name__ == "__main__"):
    A = np.random.rand(13, 10) * 1000
    # Try the QR decomposition
    A = np.matrix([
        [1.0, 1.0, 1.0],
        [1.0, 2.0, 3.0],
        [1.0, 4.0, 9.0],
        [1.0, 8.0, 27.0]
    ])
    Q, R = QR(A)
    print("If the following numbers are nearly zero, QR seems to be working.")
    print(np.linalg.norm(Q*R-A))
    print(np.linalg.norm(Q.H*Q-np.eye(3)))
    # Try solving a least squares system
    b = np.matrix([1.0, 2.0, 3.0, 4.0]).T
    x = LeastSquares(A, b)
    print("If the following number is nearly zero, least squares solving seems to be working.")
    print(np.linalg.norm(x-np.linalg.lstsq(A, b)[0]))
