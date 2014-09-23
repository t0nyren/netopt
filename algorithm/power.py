import networkx as nx
from networkx.algorithms.mst import prim_mst_edges
from heapq import heappop, heappush
from itertools import count


def simple_power(V,E):
	print 'simple power algorithm...'
	G=nx.Graph()
	for node in V:
		G.add_node(node[0], bandwidth=node[1])
	
	for edge in E:
		G.add_edge(edge[3],edge[4], delay=edge[1])
	print G.number_of_nodes()
	print G.number_of_edges()
	T = nx.Graph(power_generator(G))
	print (T.edges(data=True))
	
def power_generator(G, data=True):
	push = heappush
	pop = heappop
	data=True
	nodes = G.nodes()
	c = count()
	
	while nodes:
		u = nodes.pop(0)
		frontier = []
		visited = [u]
		for u, v in G.edges(u):
			print G.node[u]['bandwidth']/G[u][v]['delay']
			push(frontier, (-G.node[u]['bandwidth']/G[u][v]['delay'], next(c), u, v))
		while frontier:
			W, _, u, v = pop(frontier)
			if v in visited or G.node[u]['bandwidth'] <= 0:
				continue
			visited.append(v)
			nodes.remove(v)
			G.node[u]['bandwidth'] = G.node[u]['bandwidth'] -1
			for v, w in G.edges(v):
				if not w in visited:
					push(frontier, (-G.node[u]['bandwidth']/G[u][v]['delay'], next(c), v, w))
			if data:
				yield u, v, G[u][v]
			else:
				yield u, v