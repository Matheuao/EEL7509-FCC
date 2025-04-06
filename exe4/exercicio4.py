"""
Escreva um programa que resolva o seguinte sistema de equações
usando representação matricial e inversão de matrizes:

sistema = {x - y + z = 3
           3x + 2y + z = 3
           x - 2y - 5z = 1
           }
"""

import numpy as np

def linear_system_solver(A,B):
    """ return the solution for the linear system 

        A*X = B
    """

    A_inv = np.linalg.inv(A)
    X = A_inv @ B

    return X

A  = np.array([[1, -1, 1],
              [3, 2, 1],
              [1, -2, -5]], dtype=float)
B = np.array([3,3,1], dtype= float)

X = linear_system_solver(A,B)

print(X)