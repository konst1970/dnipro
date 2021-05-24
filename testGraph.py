import itertools

import networkx as nx
import numpy.random as rnd
import matplotlib.pyplot as plt

graph = nx.MultiDiGraph()

graph.add_node('a')
graph.add_node('b')


print(graph.nodes())
graph.nodes()

def add_edge(f_item, s_item, graph=None):
  graph.add_edge(f_item, s_item)
#   graph.add_edge(s_item, f_item)

add_edge('a', 'b', graph=graph)
add_edge('b', 'a', graph=graph)


nx.draw_circular(graph,
         node_color='red',
         node_size=1000,
         with_labels=True,
         connectionstyle='arc3, rad = 0.5')

plt.show()