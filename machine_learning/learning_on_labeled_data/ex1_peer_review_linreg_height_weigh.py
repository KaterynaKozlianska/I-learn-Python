### Задание 1. Первичный анализ данных
# peer_review_linreg_height_weigh

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import optimize

# from plotly.offline import iplot, plot
# import plotly
# import plotly.graph_objs as go

# 1. Посстроим гистограммы для визуальной оценки данных
data=pd.read_csv("weights_heights.csv", index_col='Index')
print (data.info())
print (data.head())

print (data.plot(y='Height', kind='hist', color='red', title='Height (inch.) distribution'))
print (data.plot(y='Weight', kind='hist', color='green', title='Weight (pounds) distribution'))

# 2. Отображение попарных зависимостей признаков. Также добавим признак Индекс массы тела (BMI)
data['BMI']=data.Weight/((data.Height)**2)*703
print (data.head())
print (sns.pairplot(data))

# 3. Постройте «ящик с усами» (boxplot) (зависимость какого-то количественного признака от категориального),
#  демонстрирующий зависимость роста от весовой категории
weight_category=[]
for elem in data['Weight']:
    if elem < 120:
        weight_category.append(1)
    elif elem >=150:
        weight_category.append(3)
    else:
        weight_category.append(2)
data['weight_category']=weight_category      
print (data.head())

weight_category_and_Height=sns.boxplot(data=data, x='weight_category', y='Height')
weight_category_and_Height.set(ylabel ='Рост', xlabel ='Весовая категория')
print (weight_category_and_Height)

# 4.Постройте scatter plot зависимости роста от веса

Weight_and_Height=data.plot(kind='scatter', x='Weight', y='Height', title='Зависимость роста от веса')
print (Weight_and_Height)

### Задание 2. Минимизация квадратичной ошибки
# Задача восстановления регрессии решается минимизацией квадратичной функции ошибки:
# как через облако точек, соответсвующих наблюдениям в нашем наборе данных, в пространстве признаков "Рост" и "Вес" 
# провести прямую линию так, чтобы минимизировать функционал

#1. Напишите функцию, которая по двум параметрам w_0 и w_1 вычисляет квадратичную ошибку приближения 
# зависимости роста y от веса x прямой линией y = w_0 + w_1 * x: 
# error(w_0, w_1) = sum_{i=1}^n {(y_i - (w_0 + w_1 * x_i))}^2

def get_y(w0, w1,x):
    return(w0+w1*x)
def get_error(w0,w1):
    return (sum(map(lambda x,y: (get_y(w0, w1,x)-y)**2, data.Weight, data.Height)))

# 2. Отобразим хоть какие-то прямые и убедимся, что они плохо передают зависимость роста от веса
def make_model_plot(w_values):
    data.plot(kind='scatter', x='Weight', y='Height', title='Зависимость роста от веса')
    x_range=np.linspace(40,200,100)
    colors=['red', 'orange']
    for w0, w1 in w_values:
        y=list(map(lambda x: get_y(w0, w1,x), x_range))
        color = colors.pop()
        plt.plot(x_range, y, color=color, lw=2)
print (make_model_plot([(60, 0.05), (50, 0.16)]))

# #3. Постройте график зависимости функции ошибки, от параметра w_1 при w_0 = 50. Подпишите оси и график.
# w0=50
# w1=np.linspace(-5,5,100)
# error=map(lambda p: get_error(w0,p), w1)
# plt.plot(w0, w1)

#4. Найдем минимум функционала для w0=50, w1 в диапазоне [-5;5].
# Построим на графике зависимости рост-вес прямую, с параметрами w0 и полученное оптимальное значение w1
w0=50
w1_opt=optimize.minimize_scalar(lambda x: get_error(w0,x), [-5,5]).x
print (w1_opt)
print (make_model_plot([(w0, w1_opt)]))

# 5. Найдем минимум функции для w0 в диапазоне [-100,100]  и для w1 в диапазоне [-5;5] с помощью метода оптимизации L-BFGS-B 
# Начальная точка – (w0, w1) = (0, 0)

def get_error_opt(w):
    return get_error(w[0], w[1])

w0_opt, w1_opt = optimize.minimize(get_error_opt, (0,0), bounds = [(-100, 100), (-5, 5)], method = 'L-BFGS-B').x
print (w0_opt, w1_opt)
make_model_plot([(w0_opt, w1_opt)])