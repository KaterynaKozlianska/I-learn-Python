# ЗАДАНИЕ:
# Анализ текста комментариев на одном из форумах. 
# Разбивка комментариев на категории.
# Визуализация распределения тональности комментариев в зависимости от категории.
# Анализ графика


import pandas as pd 
# Подгрузим дата-сет
df=pd.read_excel("YouScan_test_task.xlsx", sheet_name='Згадування')
print (df.info())

# Отфильтруем по колонке "Источник" по значению "red-forum.com" и
#колонках "Текст", "Тональность"
useful_col=df[df.Источник=='red-forum.com'][['Tекст','Тональность']]

useful_col=useful_col[0:10]

useful_col.reset_index(inplace=True)
useful_col.drop(['index'],axis=1, inplace=True)
print (useful_col.info())
print (useful_col.head()) 

# Добавим cтолбец с категориями. 
#Присвоим каждому комментарию название категории
category=[]
for index, row in useful_col.iterrows():
    print (row[0])
    category.append(input("Присвоить категорию:"))
    useful_col['Категория']=pd.Series(category)
print (useful_col.head())


# Построим bar chart (штабелированную гистограмму/линейчатую с накоплением ): 
#посмотрим на распределение комментариев и их тональностей по категориям
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly
import plotly.graph_objs as go 
init_notebook_mode

# Строим сводную таблицу:
#считаем количество комментариев в каждой категории и 
#количество комментариев по тональности в каждой категории. 
category_share=useful_col.pivot_table(
    index=['Категория'], 
    columns=['Тональность'],
    aggfunc='count',
    margins=True
) 

# Для построения гистограммы необходимо отсортировать данные 
#от большего к меньшему количеству комментариев в каждой категории,
#выраженные в процентах
category_share.columns=category_share.columns.droplevel(level=0)
category_share=category_share.sort_values(by='All', ascending=False)
category_share=round(category_share/(category_share.All.sum()/2)*100,2)
print (category_share)

#Создаём traces для визуализации
# trace0=go.Bar(
#     x=category_share.index,
#     y=category_share.Негативная,
#     name='Негативная'
# )
# trace1=go.Bar(
#     x=category_share.index,
#     y=category_share.Нейтральная,
#     name='Нейтральная'
# )
# trace2=go.Bar(
#     x=category_share.index,
#     y=category_share.Позитивная,
#     name='Позитивная'
# )
# data=[trace0, trace1, trace2]

data=[]
# tonality=0
# ['Негативная', 'Нейтральная'] , 'Позитивная'
for tonality in category_share.columns[0:-1]:
    data.append(
        go.Bar(
            x=category_share.index,
            y=category_share[tonality],
            name=str(category_share.columns[tonality])
        )
    )
    # tonality+=1



# Cоздаём массив с данными и 
#задаём название и тип графика
layout={'title':'Тональность категорий комментариев','barmode':'stack'}

# Cоздаём объект Figure и визуализируем его
fig=go.Figure(data=data, layout=layout)
iplot(fig, show_link=False)

# Сохраним гистограмму в виде html-файла
plot(fig, filename='category_share.html', show_link=False)



# #Сохраним файл в формате Excel
# df.to_excel('Comment tonality analysis.xlsx', 
#     sheet_name='Comment tonality analysis', index=None) #######сохранить изменения