### Задание 3. Min smooth functions
# f(x) = sin(x / 5) * exp(x / 10) + 5 * exp(-x / 2), на промежутке [1, 30]

import numpy as np
from scipy.optimize import minimize
from plotly.offline import download_plotlyjs, plot, iplot
import plotly
import plotly.graph_objs as go
import math

#1. Попробуйте найти минимум, используя стандартные параметры в функции scipy.optimize.minimize 
# (т.е. задав только функцию и начальное приближение). 
# Попробуйте менять начальное приближение и изучить, меняется ли результат

def f(x):
    return (math.sin(x/5.)*math.exp(x/10.)+5*math.exp(-x/2.))

f_min1=minimize(f,30)
print ('x=30:', f_min1, '\n')

# 2. Укажите в scipy.optimize.minimize в качестве метода BFGS (один из самых точных в большинстве случаев градиентных методов оптимизации), 
# запустите из начального приближения x=2. 
# Градиент функции при этом указывать не нужно – он будет оценен численно. 
f_min2=minimize(f,2, method = 'BFGS')
print ('x=2:',f_min2, '\n')

# 3. Теперь измените начальное приближение на x=30. 
f_min3=minimize(f,30, method = 'BFGS')
print ('x=30:',f_min3,'\n')

# 4. Построение графика

x=np.arange(1,31,0.1)
trace=go.Scatter(
    x=x,
    y=list(map(f,x))
)
fig=go.Figure(data=[trace])
iplot(fig, show_link=False)
plot(fig, filename="min_smoothness.html", show_link=False)