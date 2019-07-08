#  TASK:
# Text analysis on one of the forums. 
# Set the category to comments.
# Visualization category share tonality.
# Chart analysis


# Data load
import pandas as pd 
df=pd.read_excel("Reference_to_Monobank_task.xlsx", sheet_name='Reference')
print (df.info())
print (df.head())

# Filter by site "red-forum.com" and columns "Text" and "Tonality"
useful_col=df[df.Site=='red-forum.com'][['Text','Tonality']]
print (useful_col.info())
print (useful_col.head()) 

# Add the column "Category". 
#Set the category, based by the content in the column "Text"
category=[]
category_index=[]
for index, row in useful_col.iterrows():
    print (row[0])
    category.append(input("Set the category:"))
    category_index.append(row.name)
    useful_col['Category']=pd.Series(category, index=category_index)
print (useful_col.head())

# Pivot table:
#the number of comments in each category and
#the number of comments by tonality in each category
category_share=useful_col.pivot_table(
    index=['Category'], 
    columns=['Tonality'],
    aggfunc='count',
    margins=True
) 

# Sort the data from a larger to a smaller percentage of comments in each category
category_share.columns=category_share.columns.droplevel(level=0)
category_share=category_share.sort_values(by='All', ascending=False)
print (category_share)
category_share=round(category_share/(category_share.All.sum()/2)*100,2)
print (category_share)


# Build the accumulation Bar chart: 
from plotly.offline import plot, iplot  
import plotly.graph_objs as go 

# Set the array for visualization, title and type of the Bar chart
layout={'title':'Category Share Tonality','barmode':'stack'}
data=[]
for tonality in category_share.columns[0:-1]:
    data.append(
        go.Bar(
            x=category_share.index,
            y=category_share[tonality],
            name=category_share[tonality].name
        )
    )

# Set the object and visualize it
fig=go.Figure(data=data, layout=layout)
iplot(fig, show_link=False)

# Save the Bar chart as html file
plot(fig, filename='Category_Share_Tonality.html', show_link=False)


# Chart analysis and save changes to Excel file
df=pd.concat([df, useful_col.Category], axis=1)
analysis=pd.Series([input('Write comments:')], name="Analysis")
print (analysis)
writer = pd.ExcelWriter('Category_share_tonality_analysis.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Category_share_tonality', index=None)
analysis.to_excel(writer, sheet_name='Analysis', index=None)
writer.save()