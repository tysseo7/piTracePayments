
#### pip install requests
#### pip install scipy

import json
import requests
import sys
import re

import networkx as nx
import matplotlib.pyplot as plt





#f = open('foo.txt', 'r')
#f = open('x.csv', 'r')
#l_file = f.readlines()
#f.close()

l_in=[
  ['GDS7', 'GDTY', 'GAIH', 'GDZG', 'GDMV', 'GCGT', 'GBSR', 'GB6E', 'GDGV'],
  ['GDS7', 'GDTY', 'GAIH', 'GDZG', 'GDWF', 'GCGT', 'GB6E', 'GDGV'],
  ['GDS7', 'GDTY', 'GAIH', 'GDZG', 'GDWF', 'GCGT', 'GAQO', 'GB6E', 'GDGV'],
  ['GDS7', 'GDTY', 'GAIH', 'GDZG', 'GDWF', 'GCGT', 'GBUK', 'GB6E', 'GDGV'],
  ['GDS7', 'GDTY', 'GAIH', 'GDZG', 'GDWF', 'GCGT', 'GAIU', 'GB6E', 'GDGV'],
  ['GDS7', 'GDTY', 'GAIH', 'GDZG', 'GDWF', 'GCGT', 'GAKN', 'GB6E', 'GDGV'],
  ['GDS7', 'GDTY', 'GAIH', 'GDZG', 'GDWF', 'GCGT', 'GAYT', 'GB6E', 'GDGV'],
  ['GDS7', 'GDTY', 'GAIH', 'GDZG', 'GDWF', 'GCGT', 'GD3Y', 'GB6E', 'GDGV'],
  ['GDS7', 'GDTY', 'GAIH', 'GDZG', 'GDWF', 'GCGT', 'GBSR', 'GB6E', 'GDGV'],
  ['GDS7', 'GDTY', 'GAIH', 'GDZG', 'GDWF', 'GCGT', 'GATP', 'GB6E', 'GDGV'],
  ['GDS7', 'GDTY', 'GAIH', 'GDZG', 'GDWF', 'GCGT', 'GDNX', 'GB6E', 'GDGV'],
  ['GDS7', 'GDTY', 'GAIH', 'GDZG', 'GDWF', 'GCGT', 'GBXA', 'GB6E', 'GDGV'],
  ['GDS7', 'GDTY', 'GAIH', 'GDZG', 'GDWF', 'GCGT', 'GBSR', 'GB6E', 'GDGV'],
  ['GDS7', 'GDTY', 'GAIH', 'GDZG', 'GCKL', 'GCGT', 'GB6E', 'GDGV'],
  ['GDS7', 'GDTY', 'GAIH', 'GDZG', 'GCKL', 'GCGT', 'GAQO', 'GB6E', 'GDGV'],
  ['GDS7', 'GDTY', 'GAIH', 'GDZG', 'GCKL', 'GCGT', 'GBUK', 'GB6E', 'GDGV'],
  ['GDS7', 'GDTY', 'GAIH', 'GDZG', 'GCKL', 'GCGT', 'GAIU', 'GB6E', 'GDGV'],
  ['GDS7', 'GDTY', 'GAIH', 'GDZG', 'GCKL', 'GCGT', 'GAKN', 'GB6E', 'GDGV'],
  ['GDS7', 'GDTY', 'GAIH', 'GDZG', 'GCKL', 'GCGT', 'GAYT', 'GB6E', 'GDGV'],
  ['GDS7', 'GDTY', 'GAIH', 'GDZG', 'GCKL', 'GCGT', 'GD3Y', 'GB6E', 'GDGV'],
  ['GDS7', 'GDTY', 'GAIH', 'GDZG', 'GCKL', 'GCGT', 'GBSR', 'GB6E', 'GDGV'],
  ['GDS7', 'GDTY', 'GAIH', 'GDZG', 'GCKL', 'GCGT', 'GATP', 'GB6E', 'GDGV'],
  ['GDS7', 'GDTY', 'GAIH', 'GDZG', 'GCKL', 'GCGT', 'GDNX', 'GB6E', 'GDGV'],
  ['GDS7', 'GDTY', 'GAIH', 'GDZG', 'GCKL', 'GCGT', 'GBXA', 'GB6E', 'GDGV'],
  ['GDS7', 'GDTY', 'GAIH', 'GDZG', 'GCKL', 'GCGT', 'GBSR', 'GB6E', 'GDGV']
]

l_in=[
  ['GDS7', 'GDTY', 'GAIH', 'GDZG', 'GDMV', 'GCGT', 'GBSR', 'GB6E', 'GDGV'],
  ['GDS7', 'GDTY', 'GAIH', 'GDZG', 'GDWF', 'GCGT', 'GB6E', 'GDGV'],
  ['GDS7', 'GDTY', 'GAIH', 'GDZG', 'GDWF', 'GCGT', 'GAQO', 'GB6E', 'GDGV']
]


l_in=[
  ['GDS7', 'GDTY', 'GAIH', 'GDZG', 'GDMV', 'GCGT', 'GBSR', 'GB6E', 'GDGV'],
  ['GDS7', 'GDTY', 'GAIH', 'GDZG', 'GDWF', 'GCGT', 'GB6E', 'GDGV'],
  ['GDS7', 'GDTY', 'GAIH', 'GDZG', 'GDWF', 'GCGT', 'GAQO', 'GB6E', 'GDGV'],
  ['GDS7', 'GDTY', 'GAIH', 'GDZG', 'GDWF', 'GCGT', 'GBSR', 'GB6E', 'GDGV'],
  ['GDS7', 'GDTY', 'GAIH', 'GDZG', 'GCKL', 'GCGT', 'GB6E', 'GDGV'],
  ['GDS7', 'GDTY', 'GAIH', 'GDZG', 'GCKL', 'GCGT', 'GBXA', 'GB6E', 'GDGV'],
  ['GDS7', 'GDTY', 'GAIH', 'GDZG', 'GCKL', 'GCGT', 'GBSR', 'GB6E', 'GDGV']
]

d01={}
l04=[]
for l1 in l_in:
 for ii in range(1,len(l1)):
   l04.append([l1[ii-1],l1[ii]])










# グラフオブジェクトの作成
G = nx.DiGraph()

## add node
#for xxx in l06:
#  G.add_node(xxx)

# add edge
for xxx in l04:
  G.add_edge(xxx[0],xxx[1])
  #print(xxx[0],"->",xxx[1])

# レイアウトの設定
pos = nx.spring_layout(G)


node_attributes = {  'node_size': 1200, 'node_color': 'lightblue', 'node_shape': 's', 'linewidths': 1, 'edgecolors': 'blue', 'alpha': 0.5}


# 矢印の長さを調整する
arrowsize = 30
edge_attributes = {'alpha': 0.5, 'width': 2, 'arrowstyle': '->', 'arrowsize': arrowsize, 'connectionstyle': 'arc3,rad=.25'}




# 図の描画
#plt.figure(figsize=(8, 4))  # 2:1の比率にするために、図のサイズを指定
#plt.figure(figsize=(150, 150))
plt.figure(figsize=(8, 8))

# ノードのラベルを表示するための辞書
labels = {}
for node in G.nodes():
    labels[node] = node

# 四角形の大きさをラベルに合わせて自動調整するためのレイアウト
pos = nx.spring_layout(G, k=0.8, seed=123)

# ノードの四角形の大きさをラベルに合わせて自動調整
node_sizes = [len(str(labels[node])) * 300 for node in G.nodes()]

# 図の描画
nx.draw_networkx_nodes(G, pos, **node_attributes)
#nx.draw_networkx_edges(G, pos, alpha=0.5, width=2, arrowstyle="->", arrowsize=30)
nx.draw_networkx_edges(G, pos, **edge_attributes)
nx.draw_networkx_labels(G, pos, labels, font_size=12, font_family='sans-serif')
plt.axis('off')
plt.show()

