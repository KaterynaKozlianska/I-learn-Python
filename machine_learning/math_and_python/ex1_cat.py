### Задание 1: 
## Найти два предложения, которые ближе всего по смыслу к расположенному в самой первой строке. 
# В качестве меры близости по смыслу мы будем использовать косинусное расстояние.
## Дан набор предложений, скопированных с Википедии. Каждое из них имеет "кошачью тему" в одном из трех смыслов:
# кошки (животные)
# UNIX-утилита cat для вывода содержимого файлов
# версии операционной системы OS X, названные в честь семейства кошачьих

import pandas as pd
import numpy as np
from scipy import spatial

#1. Скачайте файл с предложениями (sentences.txt).
with open('ex1_cat_sentences.txt','r') as file:
    text=file.readlines()
sentences=text.copy()

#2. Каждая строка в файле соответствует одному предложению.
# Считайте их, приведите каждую к нижнему регистру.
#3. Произведите токенизацию, то есть разбиение текстов на слова.
# Для этого можно воспользоваться регулярным выражением, которое считает разделителем любой символ, не являющийся буквой
# Не забудьте удалить пустые слова после разделения

#весь текст без разделения по предложениям
text_all=text
text_all=str(text_all).lower().strip()
import re
text_all=re.split(r'[^a-z]', text_all)
for elem in range(len(text_all)):
    if text_all[elem]=='n':
       text_all[elem]=text_all[elem].replace('n', '')
text_all=list(filter(None, text_all))
# print ('text_all:', '\n', text_all, '\n')

#текст по предложениям
for line in range(len(text)):
    text[line]=text[line].lower().strip()
    text[line]=re.split(r'[^a-z]', text[line])
    text[line]=list(filter(None, text[line]))
# print ('text:', '\n', text,'\n')

#4. Составьте список всех слов, встречающихся в предложениях. 
# Сопоставьте каждому слову индекс от нуля до (d - 1), где d — число различных слов в предложениях.
# Для этого удобно воспользоваться структурой dict.

#весь текст_словарь без разделения по предложениям
text_all_dict={}
for elem in text_all:
    if elem not in text_all_dict:
        text_all_dict[elem]=1
    else:
        text_all_dict[elem]=text_all_dict[elem]+1
# print ('text_all_dict:', '\n', text_all_dict, '\n')

#текст_словарь по предложениям
text_dict=[]
for line in range(len(text)):
    name=line
    text_dict_name={}
    for elem in text[line]:
        if elem not in text_dict_name:
            text_dict_name[elem]=1
        else:
            text_dict_name[elem]=text_dict_name[elem]+1
    text_dict.append(text_dict_name)
# print ('text_dict:', '\n', text_dict, '\n')

#5. Создайте матрицу размера n * d, где n — число предложений. 
# Заполните ее: элемент с индексом (i, j) в этой матрице должен быть равен количеству вхождений j-го слова в i-е предложение. 
# У вас должна получиться матрица размера 22 * 254.

matrix=np.zeros((len(text_dict), len(text_all_dict)))
for line in range(len(text_dict)):
    s=0
    for elem in text_all_dict:
        matrix[line][s]=text_dict[line].get(elem)
        s+=1
# print (matrix,'\n')

matrix_df=pd.DataFrame(matrix)
matrix_df.columns=text_all_dict
matrix_df.fillna(0, inplace=True)
# print (matrix_df,'\n')

#6. Найдите косинусное расстояние от предложения в самой первой строке (In comparison to dogs, cats have not undergone...) 
# до всех остальных с помощью функции scipy.spatial.distance.cosine. 
# Какие номера у двух предложений, ближайших к нему по этому расстоянию (строки нумеруются с нуля)? 
# Эти два числа и будут ответами на задание. Само предложение (In comparison to dogs, cats have not undergone... ) имеет индекс 0.

distances={}
first_sentence=matrix_df.iloc[0]
for i in range(len(text_dict)):
    other_sentence=matrix_df.iloc[i]
    distances[i]=spatial.distance.cosine(first_sentence, other_sentence)

distances_df=pd.DataFrame.from_dict(distances, orient='index')
distances_df.columns=['distance'] 
distances_df['sentence']=sentences
distances_df.index=range(0,len(matrix_df),1)
distances_df.sort_values(by='distance', inplace=True)
print (distances_df[:5])