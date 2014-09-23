from model import *
from model.netopt_node import *
from model.netopt_edge import *
from model.netopt_topology import *
import random

def gen_random_graph(num_nodes):
	for i in range(num_nodes):
		node = dict(id = i, bandwidth = random.uniform(1, 5), workload = random.random())
		node_insert(node)
	for i in range(num_nodes):
		for j in range(num_nodes):
			if j > i:
				latency_ij = random.uniform(10, 300)
				throughput_ij = random.uniform(1,10)
				edge_ij = dict(latency = latency_ij, throughput = throughput_ij, from_node = i, to_node = j)
				edge_ji = dict(latency = latency_ij, throughput = throughput_ij, from_node = j, to_node = i)
				edge_insert(edge_ij)
				edge_insert(edge_ji)
				
def delete_graph():
	print 'deleting topology'
	delete_all_nodes()
	delete_all_edges()
	delete_topology()

