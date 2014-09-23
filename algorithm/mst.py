import networkx as nx

def simple_mst(V,E):
	G=nx.Graph()
	for node in V:
		G.add_node(node[0])
	
	for edge in E:
		G.add_edge(edge[3],edge[4], delay=edge[1])
	print G.number_of_nodes()
	print G.number_of_edges()
	T=nx.minimum_spanning_tree(G,weight = 'delay')
	return (sorted(T.edges(data=True)))