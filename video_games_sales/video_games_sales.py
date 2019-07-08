# Построение графика, гистограммы и диаграммы box plot 
#на основе файла с данными о продажах и оценках видео-игр

# Data load
import pandas as pd 
import numpy as np
df=pd.read_csv("video_games_sales.csv")
print(df.info())
# Данные есть не для всех игр, поэтому оставляем только те записи, в которых нет пропусков
df = df.dropna() 
print(df.info())
# Некоторые признаки, которые pandas считал как object, явно приведем к типам float или int
df['User_Score'] = df.User_Score.astype('float64')
df['Year_of_Release'] = df.Year_of_Release.astype('int64')
df['User_Count'] = df.User_Count.astype('int64')
df['Critic_Count'] = df.Critic_Count.astype('int64')
# Оставим только те признаки, которые будут использованы дальше 
useful_cols = ['Name','Platform', 'Year_of_Release', 'Genre', 
               'Global_Sales', 'Critic_Score', 'Critic_Count',
               'User_Score', 'User_Count', 'Rating'] 
print(df[useful_cols].head())
# Отфильтруем только нужные нам столбцы
sales_df = df[[i for i in df.columns if 'Sales' in i] + ['Year_of_Release']] 
print (sales_df)
# Посчитаем суммарные продажи по годам
sales_df=sales_df.groupby('Year_of_Release').sum() 
print (sales_df)

# Построим график
# Перед началом работы c библиотекой Plotly импортируем все необходимые модули
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly
import plotly.graph_objs as go 
init_notebook_mode

# Построим line plot с динамикой числа вышедших игр и их продаж по годам

# Посчитаем число вышедших игр и проданных копий по годам
years_df=df.groupby('Year_of_Release')[['Global_Sales']].sum().join(
         df.groupby('Year_of_Release')[['Name']].count())
years_df.columns=['Global_Sales', 'Number_of_Games']
print (years_df)         
# Cоздаем линию для числа проданных копий
trace0 = go.Scatter(
    x=years_df.index,
    y=years_df.Global_Sales,
    name='Global Sales'
)
# Cоздаем линию для числа вышедших игр
trace1=go.Scatter(
    x=years_df.index,
    y=years_df.Number_of_Games,
    name='Number of Games released'
)
# Определяем массив данных и задаем title графика в layout
data=[trace0, trace1]
layout={'title': 'Statistics of video games'}
# Cоздаем объект Figure и визуализируем его
fig = go.Figure(data=data, layout=layout)
iplot(fig, show_link=False)
# Cохраним график в виде html-файла
plotly.offline.plot(fig, filename='years_stats.html', show_link=False)

# Построим bar chart: посмотрим на рыночную долю игровых платформ, 
#рассчитанную по количеству выпущенных игр и по суммарной выручке

# Считаем число проданных и вышедших игр по платформам
platforms_df=df.groupby('Platform')[['Global_Sales']].sum().join(
    df.groupby('Platform')[['Name']].count()
)
platforms_df.columns = ['Global_Sales', 'Number_of_Games']
# Для построения гистограммы необходимо отсортировать данные от большего к меньшему
platforms_df.sort_values(by='Global_Sales', ascending=False, inplace=True)
# Создаем traces для визуализации
trace0=go.Bar(
    x=platforms_df.index,
    y=platforms_df.Global_Sales,
    name='Global_Sales'
)
trace1=go.Bar(
    x=platforms_df.index,
    y=platforms_df.Number_of_Games,
    name='Number_of_Games'
)
# Cоздаем массив с данными и задаем title для графика и оси x в layout
data=[trace0, trace1]
layout={'title':'Share of platforms', 'xaxis':{'title': 'platform'}}
# Cоздаем объект Figure и визуализируем его
fig = go.Figure(data=data, layout=layout)
iplot(fig, show_link=False)
# Cохраним гистограмму в виде html-файла
plotly.offline.plot(fig, filename='platform_stats.html', show_link=False)

# Построим box plot: рассмотрим распределения оценок критиков 
#в зависимости от жанра игры

# Создаем Box trace для каждого жанра из наших данных
data=[]
for genre in df.Genre.unique():
    data.append(
        go.Box(y=df[df.Genre==genre].Critic_Score,
        name=genre)
    )
layout= {'title':'Critical rating distributions'}
fig=go.Figure( data=data, layout=layout)
# Визуализируем данные
iplot(fig, show_link = False)
# Cохраним box plot в виде html-файла
plotly.offline.plot(fig, filename='critical_rating_distributions.html', show_link=False)