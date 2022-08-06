import pandas as pd
import numpy as np
from pyecharts.charts import Sankey
from pyecharts import options as opts


df = pd.read_excel('G:\\data\\sankey\\7.11\\xijun-1.xls')
df.head(0)

nodes = []

for i in range(2):
    values = df.iloc[:,i].unique()
    for value in values:
        dic = {}
        dic['name'] = value
        nodes.append(dic)
nodes

#print(nodes)

first = df.groupby(['Bacteria','Sample'])['Number'].sum().reset_index()
second = df.iloc[:,1:]
#second = df.groupby(['VirusFamily','Sample'])['Number'].sum().reset_index()
first.columns = ['source','target','value']
#second.columns = ['source','target','value']
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
             '',  # 图例名称
             nodes,  # 传入节点数据
             linkes,  # 传入边和流量数据
             #orient = 'vertical',
             # 设置透明度、弯曲度、颜色
             linestyle_opt = opts.LineStyleOpts(opacity = 0.5, curve = 0.5, color = "source"),
             # 标签显示位置
             label_opts = opts.LabelOpts(position = "right",font_size = 0),
             # 节点之前的距离
             node_gap = 70,
             node_align= 30,
             node_width= 300,

             )
        .set_global_opts(title_opts = opts.TitleOpts(title = '1'))

)

pic.render('未抽平细菌7.12-1.html')







