
#### pip install requests
#### pip install scipy

import json
import requests
import sys
import re

import networkx as nx
import matplotlib.pyplot as plt





#f = open('foo.txt', 'r')
f = open('x.csv', 'r')
l_file = f.readlines()
f.close()




l_file2 = [s for s in l_file if 'amount' in s]

l01=[]
for xxx in l_file2:
  ll=xxx.split(",")
  l01.append(ll[3]+","+ll[5])

l02=[]
l02 = sorted(set(l01), key=l01.index)

l03=[] # org of txList
l04=[] #        txList
d01={}
for xxx in l02:
  ll=xxx.split(",")
  l03.append([ll[0],ll[1]])
  adr_from = ll[0][:4]
  adr_to   = ll[1][:4]
  l04.append([adr_from,adr_to])

  if adr_from not in d01:
    d01[adr_from] = [adr_to]
  else:
    d01[adr_from].append(adr_to)

#for xxx in l04:
#  print(xxx)

'''
for k, v in d01.items():
  print("key:" + k)
  print(v)
  print("")
'''



l05=[] # for add_node tmp
txList=[]
for xxx in l04:
  l05.append(xxx[0])
  l05.append(xxx[1])




l06=[] ## for add_node
l06 = sorted(set(l05), key=l05.index)

#print("######################################")
#for xxx in l04:
#  print(xxx)

def find_path(graph, start, end, path=[]):
    # 現在のノードをpathに追加
    path = path + [start]

    # ベースケース：現在のノードが終了ノードである場合、pathを返す
    if start == end:
        return path

    # 開始ノードから到達可能なノードを取得
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            # 深さ優先探索で、終了ノードが見つかるまで再帰的に探索を続ける
            new_path = find_path(graph, node, end, path)
            if new_path:
                return new_path

    # 終了ノードが見つからなかった場合、Noneを返す
    return None

def find_all_paths(graph, start, end, path=[]):
    # 現在のノードをpathに追加
    path = path + [start]

    # ベースケース：現在のノードが終了ノードである場合、pathを返す
    if start == end:
        return [path]

    # 開始ノードから到達可能なノードを取得
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            # 深さ優先探索で、終了ノードが見つかるまで再帰的に探索を続ける
            new_paths = find_all_paths(graph, node, end, path)
            for new_path in new_paths:
                paths.append(new_path)

    # 全てのパスを返す
    return paths



l_path = find_path(d01, 'GDS7', 'GDGV')
print(l_path)
l_path = find_path(d01, 'GDS7', 'GDPY')
print(l_path)
l_path = find_path(d01, 'GDS7', 'GALI')
print(l_path)
l_path = find_path(d01, 'GDS7', 'GC6G')
print(l_path)
l_path = find_path(d01, 'GDS7', 'GAHP')
print(l_path)



'''
l_paths = find_all_paths(d01, 'GDS7', 'GDGV')
for xxx in l_paths:
  print(xxx)
print("length of pathes ... "+str(len(l_paths)))
'''








'''
# グラフオブジェクトの作成
G = nx.DiGraph()

## add node
for xxx in l06:
  G.add_node(xxx)

# add edge
for xxx in l04:
  G.add_edge(xxx[0],xxx[1])
  print(xxx[0],"->",xxx[1])

# レイアウトの設定
pos = nx.spring_layout(G)


node_attributes = {  'node_size': 1200, 'node_color': 'lightblue', 'node_shape': 's', 'linewidths': 1, 'edgecolors': 'blue', 'alpha': 0.5}


# 矢印の長さを調整する
arrowsize = 30
edge_attributes = {'alpha': 0.5, 'width': 2, 'arrowstyle': '->', 'arrowsize': arrowsize, 'connectionstyle': 'arc3,rad=.25'}




# 図の描画
#plt.figure(figsize=(8, 4))  # 2:1の比率にするために、図のサイズを指定
plt.figure(figsize=(150, 150))

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

'''