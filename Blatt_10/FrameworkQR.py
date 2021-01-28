import numpy as np

def QRAlgorithm(Matrix):
    """Computes the Eigenvalues of the given matrix and returns them."""
    

if(__name__=="__main__"):
    Matrix=np.random.rand(5,5);
    Matrix+=Matrix.T;
    print('Eigenvalues computed by QRAlgorithm():');
    print(sorted(QRAlgorithm(Matrix)));
    print('Eigenvalues computed by numpy.linalg.eigh():');
    print(sorted(np.linalg.eigh(Matrix)[0]));
