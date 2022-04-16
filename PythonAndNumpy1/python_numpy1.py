# python_intro.py
"""Python Essentials: Introduction to Python.
<Name> Zhongyu Wang
<Class> Mth 420
<Date> 4/15/2022
"""

#Problem 1
r = 10
x , y = 4, 3
x,y = 4,3
pi = 3.14159
z = x / y
V = z * pi * (r ** 3)
print(V)

#Problem 2
print("Hello, world!") 

#Problem 3
def sphere_volume(r):
    pi = 3.14159
    A = (4/3) * pi * r * r * r
    return A

r = input("input the number for r:")
r = float(r)

A = sphere_volume(r)
print("the volume is", A)

#problem 4
import numpy as np
def prob4():
    A = np.array([[1, 2, 3], [4, 5, 6]])
    B = np.array([[2, 6, -5, 3], [5, -8, 9, 7], [9, -3, -2, -3]])
    x = np.dot(A, B)
    return x

x = prob4()
print(x)

#problem 5
def tax_liability(s):
    a = 9875
    b = 40125
    c = 85525
    if s <= a:
        s = s/10
    elif s >= a and s <= b:
            s = 0.12 * (s - a) + 987.5
    elif s >= b:
        s = 0.22 * (s - b) + 987.5 + 3630
    return s
        
s = input("input your salary for s:")
s = float(s)

A = tax_liability(s)
print("the total tax is", A)

#problem6
def prob6a():
    A = list(range(1,7))
    B = list([5, 5, 5, 5, 5, 5, 5])
    x = A@B
    y = A + B
    z = 5 * A
    return x, y, z

m = prob6a()
print(m)

def prob6b():
    A, B = np.array([1, 2, 3, 4, 5, 6, 7]), np.array([5, 5, 5, 5, 5, 5, 5])
    x = np.dot(A, B)
    y = A + B
    z = 5 * A
    return x, y, z

n = prob6b()
print(n)
