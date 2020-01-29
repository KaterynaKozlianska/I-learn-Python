###Задание 4. Overall optimization (differential evolution)
# f(x) = sin(x / 5) * exp(x / 10) + 5 * exp(-x / 2), на промежутке [1, 30]

from scipy import optimize
import math

def f(x):
    return (math.sin(x/5.)*math.exp(x/10.)+5*math.exp(-x/2.))

bounds=[(1,30)]
result=optimize.differential_evolution(f, bounds)
print (result)