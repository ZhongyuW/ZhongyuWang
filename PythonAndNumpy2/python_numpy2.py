# python_intro.py
"""Python Essentials: Introduction to Python.
<Name> Zhongyu Wang
<Class>Mth 420
<Date>4/22/2022
"""
import numpy as np
#Problem 1
def isolate(a, b, c, d, e):
    print(a, b, c, sep = "  ", end = " ")
    print(d, e)
A = isolate(1, 2, 3, 4, 5)
print(A)

    #raise NotImplementedError("Problem 1 Incomplete")

#Problem 2
def first_half(str):
    return str[:len(str)//2]
    
B = first_half("Zhongyu")
print(B)

    #raise NotImplementedError("Problem 2 Incomplete")


def backward(str):
    return str[::-1]
C = backward("Zhongyu11")
print(C)

    #raise NotImplementedError("Problem 2 Incomplete")

#Problem 3
def list_ops(list):
            list.append("eagle")
            list[2] = "fox"
            list.pop(1)
            list.reverse()
            list[0] = "hawk"
            list.append("hunter")
            A = list
            return A
D = list_ops(["bear", "ant", "cat", "dog"])
print(D)

    
    #raise NotImplementedError("Problem 3 Incomplete")

#Problem 4
def alt_harmonic(n):
    """Return the partial sum of the first n terms of the alternating
    harmonic series. Use this function to approximate ln(2).
    """
    if n < 2:
        return 1
    else: 
        return ((-1) ** (n + 1))/n + (alt_harmonic(n-1))
E = alt_harmonic(99)
print(E)
    #raise NotImplementedError("Problem 4 Incomplete")



def prob5(A):
    """Make a copy of 'A' and set all negative entries of the copy to 0.
    Return the copy.

    Example:
        >>> A = np.array([-3,-1,3])
        >>> prob4(A)
        array([0, 0, 3])
    """
    A = np.maximum(A, 0)
    print(A)
A = np.array([[1,2,3],[-1,-2,-3]])
F = prob5(A)
print(F)
    #raise NotImplementedError("Problem 5 Incomplete")

def prob6(A, B, C):
    """Define the matrices A, B, and C as arrays. Return the block matrix
                                | 0 A^T I |
                                | A  0  0 |,
                                | B  0  C |
    where I is the 3x3 identity matrix and each 0 is a matrix of all zeros
    of the appropriate size.
    """
    A = A.reshape((2, 3))
    I = eye(3)
    D = np.colum_stack((np.zeros(3), np.zeros(3), np.zeros(3), A.T, I))
    E = np.colum_stack((A, np.zeros(2), np.zeros(2), np.zeros(2),np.zeros(2),np.zeros(2),))
    F = np.colum_stack((B, np.zeros(3), zeros(3), C))
    G = np.vstack(D, E, F)
    return G
A = np.array([[0, 2, 4], [1, 3, 5]])
B = np.array([[3, 0, 0], [3, 3, 0], [3, 3, 3]])
C = np.array([[-2, 0, 0], [0, -2, 0], [0, 0, -2]])
print(prob6(A, B, C)
    #raise NotImplementedError("Problem 6 Incomplete")

#def prob7(A):
    #Divide each row of 'A' by the row sum and return the resulting array.

    #Example:
        #>>> A = np.array([[1,1,0],[0,1,0],[1,1,1]])
        #>>> prob6(A)
        #array([[ 0.5       ,  0.5       ,  0.        ],
               #[ 0.        ,  1.        ,  0.        ],
               #[ 0.33333333,  0.33333333,  0.33333333]])
    #
    #raise NotImplementedError("Problem 7 Incomplete")


#def prob8(A):
    #"""Given the array stored in grid.npy, return the greatest product of four
    #adjacent numbers in the same direction (up, down, left, right, or
    #diagonally) in the grid.
    #"""
 
    #raise NotImplementedError("Problem 8 Incomplete")