# matplotlib_intro.py
"""Python Essentials: Intro to Matplotlib.
<Name> Zhongyu Wang
<Class>Mth 420
<Date>4/28/2022
"""
import numpy as np
from matplotlib import pyplot as plt
# Problem 1
def var_of_means(n):
    """Construct a random matrix A with values drawn from the standard normal
    distribution. Calculate the mean value of each row, then calculate the
    variance of these means. Return the variance.

    Parameters:
        n (int): The number of rows and columns in the matrix A.

    Returns:
        (float) The variance of the means of each row.
    """
    A = np.random.normal(size=(n,n))
    x = np.mean(A, axis = 1)
    y = np.var(x)
    return y
print(var_of_means(5))
    
    
    #raise NotImplementedError("Problem 1 Incomplete")

def prob1():
    """Create an array of the results of var_of_means() with inputs
    n = 100, 200, ..., 1000. Plot and show the resulting array.
    """
    A = var_of_means(100)
    B = var_of_means(200)
    C = var_of_means(300)
    D = var_of_means(400)
    E = var_of_means(500)
    F = var_of_means(600)
    G = var_of_means(700)
    H = var_of_means(800)
    I = var_of_means(900)
    J = var_of_means(1000)
    X = np.array([A, B, C, D, E, F, G, H, I, J])
    K = plt.plot(X)
    return K
print(prob1())
    #raise NotImplementedError("Problem 1 Incomplete")


# Problem 2
def prob2():
    """Plot the functions sin(x), cos(x), and arctan(x) on the domain
    [-2pi, 2pi]. Make sure the domain is refined enough to produce a figure
    with good resolution.
    """
    import math
    x = np.linspace(-2*np.pi, 2*np.pi, 100)
    a = plt.plot(x,np.sin(x))
    b = plt.plot(x,np.cos(x))
    c = plt.plot(x,np.arctan(x))
    return a, b, c
print(prob2())
    #raise NotImplementedError("Problem 2 Incomplete")


# Problem 3
def f(x):
    with np.errstate(divide='ignore', invalid='ignore'):
        return 1/(x-1)
def prob3():
    """Plot the curve f(x) = 1/(x-1) on the domain [-2,6].
        1. Split the domain so that the curve looks discontinuous.
        2. Plot both curves with a thick, dashed magenta line.
        3. Set the range of the x-axis to [-2,6] and the range of the
           y-axis to [-6,6].
    """
    x = np.linspace(-2, 6, 100)
    y = f(x)
    z = plt.plot(x, y, linewidth = 4)
    plt.xlim(-2, 6)
    plt.ylim(-6, 6)
    return z
print(prob3())
    
    #raise NotImplementedError("Problem 3 Incomplete")


# Problem 4
def prob4():
    """Plot the functions sin(x), sin(2x), 2sin(x), and 2sin(2x) on the
    domain [0, 2pi].
        1. Arrange the plots in a square grid of four subplots.
        2. Set the limits of each subplot to [0, 2pi]x[-2, 2].
        3. Give each subplot an appropriate title.
        4. Give the overall figure a title.
        5. Use the following line colors and styles.
              sin(x): green solid line.
             sin(2x): red dashed line.
             2sin(x): blue dashed line.
            2sin(2x): magenta dotted line.
    """
    fig = plt.figure(22)
    x = np.linspace(0, 2*np.pi, 100)
    a =  plt.subplot(221)
    a.plot(x, np.sin(x), 'g-')
    plt.axis([0,2*np.pi,-2,2]) 
    plt.title('sin(x)')
    b =  plt.subplot(222)
    b.plot(x, np.sin(2*x), 'r--')
    plt.axis([0,2*np.pi,-2,2]) 
    plt.title('sin(2x)')
    c =  plt.subplot(223)
    c.plot(x, 2*np.sin(x), 'b--')
    plt.axis([0,2*np.pi,-2,2]) 
    plt.title('2sin(x)')
    d =  plt.subplot(224)
    d.plot(x, 2*np.sin(2*x), 'm:')
    plt.axis([0,2*np.pi,-2,2])  
    plt.title('2sin(2x)')
    fig.suptitle('functions')
    k = plt.figure()
    return k
print(prob4())
   # raise NotImplementedError("Problem 4 Incomplete")


# Problem 5
def prob5():
    """Visualize the data in FARS.npy. Use np.load() to load the data, then
    create a single figure with two subplots:
        1. A scatter plot of longitudes against latitudes. Because of the
            large number of data points, use black pixel markers (use "k,"
            as the third argument to plt.plot()). Label both axes.
        2. A histogram of the hours of the day, with one bin per hour.
            Label and set the limits of the x-axis.
    """
    raise NotImplementedError("Problem 5 Incomplete")


# Problem 6
def prob6():
    """Plot the function f(x,y) = sin(x)sin(y)/xy on the domain
    [-2pi, 2pi]x[-2pi, 2pi].
        1. Create 2 subplots: one with a heat map of f, and one with a contour
            map of f. Choose an appropriate number of level curves, or specify
            the curves yourself.
        2. Set the limits of each subplot to [-2pi, 2pi]x[-2pi, 2pi].
        3. Choose a non-default color scheme.
        4. Add a colorbar to each subplot.
    """
    x = np.linspace(-2*np.pi, 2*np.pi, 100)
    y = x.copy()
    X, Y = np.meshgrid(x, y) 
    Z = np.sin(X) * np.sin(Y)/(X*Y)
    g = plt.figure(12)
    plt.subplot(122)
    plt.pcolormesh(X, Y, Z, cmap="viridis")
    plt.colorbar()
    plt.xlim(-2*np.pi, 2*np.pi)
    plt.ylim(-2*np.pi, 2*np.pi)
    plt.subplot(122)
    plt.contour(X, Y, Z, 10, cmap="coolwarm")
    plt.colorbar()
    k = plt.figure()
    return k
print(prob6())


    
    #raise NotImplementedError("Problem 6 Incomplete")
