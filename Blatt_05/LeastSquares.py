import numpy as np
from scipy import linalg

def QR(A):
    """Given a matrix A with full column rank this function uses the classical 
       Gram-Schmidt algorithm to compute a QR decomposition. It returns a tuple 
       (Q,R) of np.matrix objects with Q having shape identical to A and Q*R=A."""
    
    V = A.copy()
    n, m = A.shape
    Q = np.zeros((n, m))
    R = np.zeros((m, m))
    
    for j in range(m):
        R[j, j] = np.linalg.norm(V[:, j:j+1].reshape(-1), 2)
        Q[:, j:j+1] = V[:, j:j+1]/R[j, j]
        R[j:j+1, j+1:m+1] = np.dot(Q[:, j:j+1].T, V[:, j+1:m+1])
        V[:, j+1:m+1] = V[:, j+1:m+1] - np.dot(Q[:, j:j+1], R[j:j+1, j+1:m+1])
        
    return np.asmatrix(Q), np.asmatrix(R)     


def BackSubstitution(R: np.matrix, y: np.ndarray):
    """Given a square upper triangular matrix R and a vector y of same size this 
       function solves R*x=y using backward substitution and returns x."""
    
    n = R.shape[1]
    x = np.zeros((n, 1), dtype = np.dtype)
    
    #Backward substitution
    for i in range(n-1, -1, -1):
        x[i] = y[i]
        for j in range(i+1, n):
            x[i] -= x[j] * R[i, j]
        x[i] /= R[i,i]

    #old code
    #n, m = R.shape
    #x = np.zeros_like(y)
    #
    #for i in range(m):
    #    x[i] = y[i] / R[i, i] 
    #    y[1:i-1] = y[1:i-1, i] * x[i]
        
    return x


def LeastSquares(A, b):
    """Given a matrix A and a vector b this function solves the least squares 
       problem of minimizing |A*x-b| and returns the optimal x."""
    
    Q, R = QR(A)
    R  = BackSubstitution(R, b)
    
    x = np.linalg.inv(R) * R * b
    
    return x


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
