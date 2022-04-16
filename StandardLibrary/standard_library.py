# standard_library.py
"""Python Essentials: The Standard Library.
<Name> Zhongyu Wang
<Class> Mth 420
<Date> 4/15/2022
"""


# Problem 1
def prob1(L):
    """Return the minimum, maximum, and average of the entries of L
    (in that order).
    """
    x = min(L)
    y = max(L)
    z = sum(L)
    a = len(L)
    b = z/a
    return x, y, b
#raise NotImplementedError("Problem 1 complete")


# Problem 2
def prob2():
    """Determine which Python objects are mutable and which are immutable.
    Test numbers, strings, lists, tuples, and sets. Print your results.
    """
    a = int(7)
    b = a
    a = a + 1
    print(a, b)
    print("numbers are immutable")
    c = str("hello")
    d = c
    c = "world"
    print(c,d)
    
#raise NotImplementedError("Problem 2 Incomplete")

prob2()


# Problem 3
def hypot(a, b):
    """Calculate and return the length of the hypotenuse of a right triangle.
    Do not use any functions other than sum(), product() and sqrt that are 
    imported from your 'calculator' module.

    Parameters:
        a: the length one of the sides of the triangle.
        b: the length the other non-hypotenuse side of the triangle.
    Returns:
        The length of the triangle's hypotenuse.
    """
    x = a * a
    y = b * b
    k = x + y
    import math
    z =math.sqrt(k)
    return z

a = input("input the length one side for x:")
a = float(a)
b = input("input the length of the other side for y:")
b = float(b)
A = hypot(a, b)
print(A)

    #raise NotImplementedError("Problem 3 complete")


# Problem 4
def power_set(A):
    """Use itertools to compute the power set of A.

    Parameters:
        A (iterable): a str, list, set, tuple, or other iterable collection.

    Returns:
        (list(sets)): The power set of A as a list of sets.
    """
    from itertools import combinations
    x = len(A)
    for i in range (x+1):
        if i == 0:
            print("[ ]")
        else:
            result = list(combinations(A, i))
            print(result)
#raise NotImplementedError("Problem 4 Incomplete")
A = "ABC"
power_set(A)

# Problem 5: Implement shut the box.
def shut_the_box(player, timelimit):
    """Play a single game of shut the box."""