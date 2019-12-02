### Задание 5. Minimization Non-smooth functions.py
# h(x) = int(f(x)) при f(x) = sin(x / 5) * exp(x / 10) + 5 * exp(-x / 2), на промежутке [1, 30]

import numpy as np
from scipy import optimize
from plotly.offline import download_plotlyjs, plot, iplot
import plotly
import plotly.graph_objs as go
import math

# 1. Построим графики функций
def f(x):
    return (math.sin(x/5.)*math.exp(x/10.)+5*math.exp(-x/2.))
def h(x):
    return (int(f(x)))

x=np.arange(1,31,0.1)
trace_f=go.Scatter(
    x=x,
    y=list(map(f,x)),
    name='f(x)'
)
trace_h=go.Scatter(
    x=x,
    y=list(map(h,x)),
    name='h(x)=int(f(x))'
)

fig=go.Figure(data=[trace_f, trace_h])
iplot(fig, show_link=False)
plot(fig, filename="min_smoothness.html", show_link=False)

# 2. Попробуйте найти минимум функции h(x) с помощью BFGS
f_min_BFGS=optimize.minimize(h, 30, method='BFGS')
print ('BFGS(30):', '\n', f_min_BFGS, '\n')

# 3. Теперь попробуйте найти минимум h(x) на отрезке [1, 30] с помощью дифференциальной эволюции
bounds=[(1,30)]
f_min_diffevol=optimize.differential_evolution(h, bounds)
print ('differential_evolution(1,30):', '\n', f_min_diffevol)
