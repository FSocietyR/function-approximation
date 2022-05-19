from sympy import *
import sympy
import matplotlib.pyplot as plt 
from random import randint
import numpy as np
from scipy.linalg import solve
from scipy.linalg import lstsq
#from time import localtime
import os
import time


class Function:
    def __init__(self, x : np.array = [], y : np.array = [],
                    coeff: dict = {'A_n' : None, 'D_n' : None, 'E_n' : None, 'C_n' : None}):
        self.x = x
        self.y = y
        self.coeff = coeff

class _func_fit(Function):
    def __init__(self, x : np.array, y : np.array,
                    tolerance : float, tolerance_diff : float  ):
        self.x = None
        self.y = None
        self.tolerance = tolerance
        self.tolerance_diff = tolerance_diff
    
    def tolerance_check():
        pass

def  nd_order_curve(*args) -> list:
    x, y = args[0][0], args[0][1]
    def pretty_out(matrix):
        dic = {'A_n' : matrix[0], 'D_n': matrix[1], 'E_n' : matrix[2], 'C_n' : matrix [-1]} 
        return dic

    #chck_mass = [ [x := randint(1,100), y := randint(1,100), x ** 2, 2 * x, 2 * y, y ** 2] for _ in range(4)]
    chck_mass = []
    for _ in range(len(x)):
        chck_mass.append([x[_], y[_], x[_] ** 2, 2 * x[_], 2 * y[_], y[_] ** 2])

    dots = {'X': [], 'Y': []}
    for element in chck_mass:
        dots['X'].append(element[0])
        dots['Y'].append(element[1])

    for _ in range(4):
        for i in range(2):
            del chck_mass[_][0]

    f_matrix = np.array(chck_mass)
    #f_matrix = np.array([[1, 2, 2, 1], [4, 4, 4, 4], [16, 8, 32 ,16**2], [25, 10, 50, 625]])
    s_matrix = np.array([-1,-1,-1,-1]).reshape(4,1)

    try:
        return {'f': 0, 'coeff': pretty_out(solve(f_matrix, s_matrix)), 'dots' : dots}
    except Exception as Error:
        print(Error)
        return {'f': 1, 'coeff': pretty_out(lstsq(f_matrix,s_matrix)[0]), 'dots' : dots}


def plot_drawer_nd_order_curve(*args) -> None:

    from sympy import solve as solver
    from alive_progress import alive_bar as bar

    timeone = time.perf_counter()
    clear = lambda : os.system('cls')
    function = Function()
    UNNEEDED_MEMORY = nd_order_curve(args[0])
    function.coeff, dots = UNNEEDED_MEMORY['coeff'], UNNEEDED_MEMORY['dots']
    del UNNEEDED_MEMORY
    X = dots['X']; X = np.array(X)
    Y = dots['Y']; Y = np.array(Y)
    print(f"DOTS :: {dots}")
    print(f"coeff :: {function.coeff}")   
    x, y = symbols('x y')
    A_n, C_n, D_n, E_n = symbols('A_n C_n D_n E_n')

    A_n = function.coeff['A_n'][0]
    D_n = function.coeff['D_n'][0]
    E_n = function.coeff['E_n'][0]
    C_n = function.coeff['C_n'][0]

    WILL_BE_DELETED_SOON  = [_ for _ in range(-10**3 + 1,10**3+1)]

    firstind = 0
    for x in WILL_BE_DELETED_SOON:
        expr = A_n * x ** 2 + D_n * 2 * x + E_n * 2 * y + C_n * y ** 2  + 1
        ans = solver(expr, y)

        if type(ans[0]) != sympy.core.add.Add:
            function.y.append(ans[0])
            function.x.append(x)

        if type(ans[-1]) != sympy.core.add.Add:
            function.y.append(ans[-1])
            function.x.append(x)

        procent = len(function.x) / (4*10**3-4) * 100

        for _ in range(firstind, 21):
            if (_ * 5) == int(procent):
                print(f"procent work...{int(procent)}%")
                firstind = _+1
                break
    timetwo = time.perf_counter()
    print(f"time executed :: {timetwo - timeone}")
    plt.plot(function.x, function.y, color = 'red')
    # plt.plot(function.x[1], function.y[1], color = 'red')
    plt.scatter(X, Y, color = 'cyan')
    plt.scatter(function.x, function.y, s = 5)
    plt.show()
    # print(len(function.x[0]), len(function.x[1]))

def input_cord() -> list:
    cordx = list(map(float, input().split(' ')))
    cordy = list(map(float, input().split(' ')))
    return cordx, cordy   

if __name__ == "__main__":
    os.system('cls')
    arg = input_cord()
    print(arg)
    plot_drawer_nd_order_curve(arg)
