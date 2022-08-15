import pandas as pd
import numpy as np
from pyecharts.charts import Sankey
from pyecharts import options as opts


df = pd.read_excel('site') #the position of your excel with the '.xls'
df.head(0)

nodes = []

for i in range(3):
    values = df.iloc[:,i].unique()
    for value in values:
        dic = {}
        dic['name'] = value
        nodes.append(dic)
nodes

#print(nodes)

first = df.groupby(['Sample','Virusfamily'])['Number'].sum().reset_index()
second = df.iloc[:,1:]
second = df.groupby(['VirusFamily','Host'])['Number'].sum().reset_index()
first.columns = ['source','target','value']
second.columns = ['source','target','value']
result = pd.concat([first,second])
result.head(0)


linkes = []
for i in result.values:
    dic = {}
    dic['source'] = i[0]
    dic['target'] = i[1]
    dic['value'] = i[2]
    linkes.append(dic)

linkes

#print(linkes)


pic = (
    Sankey(
    init_opts=opts.InitOpts(
        width='8000px',
        height='10000px'  

    )
).add(
             '',  
             nodes,  
             linkes, 
             #orient = 'vertical',
  
             linestyle_opt = opts.LineStyleOpts(opacity = 0.5, curve = 0.5, color = "source"),

             label_opts = opts.LabelOpts(position = "right",font_size = 0),

             node_gap = 70,
             node_align= 30,
             node_width= 300,

             )
        .set_global_opts(title_opts = opts.TitleOpts(title = '1'))

)

pic.render('name.html')







