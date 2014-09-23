from model.netopt_node import *
from model.netopt_edge import *
from model.netopt_topology import *
from model.gen_random_topology import *
from algorithm.mst import simple_mst
from algorithm.power import simple_power
def main():
	#node = dict(id=6, bandwidth=223.23, workload=0.22)
	#node2 = dict(id=2, bandwidth=223.24, workload=0.24)
	#node_insert(node)
	#node_update(2, node2)
	delete_graph()
	gen_random_graph(10) 
	nodes = get_all_nodes()
	edges = get_all_edges()
	#print nodes
	#print edges
	#T = simple_mst(nodes, edges)
	simple_power(nodes,edges)
	#save_topology(T)


if  __name__ =='__main__':main()