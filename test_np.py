import pandas as pd 
import numpy as np 
df=pd.DataFrame(np.arange(0,32,2).reshape(4,4))
df.index=['A','b','c','d']
df.columns=['q','w','e','r']
df.index.name='index'
df=df.rename( {'A':'a'}, axis=0)
print (df)
print(df.d)