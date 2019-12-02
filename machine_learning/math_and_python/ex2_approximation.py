### Задание 2:
## Рассмотрим сложную математическую функцию на отрезке [1, 15]:
# f(x) = sin(x / 5) * exp(x / 10) + 5 * exp(-x / 2)
## Как известно, многочлен степени n (то есть w_0 + w_1 x + w_2 x^2 + ... + w_n x^n) 
# однозначно определяется любыми n + 1 различными точками, через которые он проходит. 
# Это значит, что его коэффициенты w_0, ... w_n можно определить системой линейных уравнений,
# где через x_1, ..., x_n, x_{n+1} обозначены точки, через которые проходит многочлен, 
# а через f(x_1), ..., f(x_n), f(x_{n+1}) — значения, которые он должен принимать в этих точках.

#1. Сформируйте систему линейных уравнений (то есть задайте матрицу коэффициентов A и свободный вектор b) 
# для многочлена первой степени, который должен совпадать с функцией f в точках 1 и 15.
# Решите данную систему с помощью функции scipy.linalg.solve. Нарисуйте функцию f и полученный многочлен

import numpy as np
import scipy as sp
from scipy import linalg
import math

def f(x):
    return (math.sin(x/5.)*math.exp(x/10.)+5*math.exp(-x/2.))

x=np.arange(1,16,0.1)
y=list(map(f,x))


def get_matrix(x_points):
    n=len(x_points)
    matrix=[]
    for x in x_points:
        row=[]
        for i in range(n):
            row.append(x**i)
        matrix.append(row)
    return (np.array(matrix))

def get_approximate_values(w,x_points):
    y=[]
    for x in x_points:
        y_curr=0
        for i in range(len(w)):
            y_curr+=w[i]*(x**i)
        y.append(y_curr)
    return (y)  

x_2=[1,15]
A_2=get_matrix(x_2)
# print ('A_2', A_2, '\n')
y_2=list(map(f,x_2))
# print ('y_2', y_2, '\n')
w_2=sp.linalg.solve(A_2,y_2)
print ('w_2', w_2, '\n')
y_approx_2=get_approximate_values(w_2,x)
# print ('y_approx_2', y_approx_2, '\n')

#2. Повторите те же шаги для многочлена второй степени, который совпадает с функцией f в точках 1, 8 и 15
x_3=[1,8,15]
A_3=get_matrix(x_3)
# print ('A_3', A_3, '\n')
y_3=list(map(f,x_3))
# print ('y_3', y_3, '\n')
w_3=sp.linalg.solve(A_3,y_3)
print ('w_3', w_3, '\n')
y_approx_3=get_approximate_values(w_3,x)
# print ('y_approx_3', y_approx_3, '\n')

#3. Повторите те же шаги для многочлена третьей степени, который совпадает с функцией f в точках 1, 4, 10 и 15. 
# Хорошо ли он аппроксимирует функцию? 
# Коэффициенты данного многочлена (четыре числа в следующем порядке: w_0, w_1, w_2, w_3) являются ответом на задачу
x_4=[1,4,10,15]
A_4=get_matrix(x_4)
# print ('A_4', A_4, '\n')
y_4=list(map(f,x_4))
# print ('y_4', y_4, '\n')
w_4=sp.linalg.solve(A_4,y_4)
print ('w_4', w_4, '\n')
y_approx_4=get_approximate_values(w_4,x)
# print ('y_approx_4', y_approx_4, '\n')

result=w_4
print ('result:',result)

#4. Построение графика

from matplotlib import pyplot as plt
plt.plot(x,y)
plt.plot(x,y_approx_2)
plt.plot(x,y_approx_3)
plt.plot(x,y_approx_4)
plot=[[plt.plot(x,y)],[plt.plot(x,y_approx_2)],[plt.plot(x,y_approx_3)],[plt.plot(x,y_approx_4)]]
print (plot)