from model import *

def edge_insert(item):
	sql = 'insert into Edge(latency,throughput,from_node,to_node)\
			 values(%f, \'%f\', \'%d\', \'%d\') \
		  ' % (item['latency'],item['throughput'],item['from_node'],item['to_node'])
	#print sql
	return netopt_db_change(sql)

def edge_update(id, item):
	ops = ''
	for k,v in item.items():
		if type(v) == type(1):
			op = '%s=%d' %(k, v)
		elif type(v) == type(1.0):
			op = '%s=\'%f\'' %(k, v)
		else:
			op = '%s=\'%s\'' %(k,str(v))
			
		if ops == '':
			ops = ops + op
		else:
			ops = ops + ', ' + op
			
	sql = 'update Edge set %s where id=%d' % (ops, id)
	#print sql
	return netopt_db_change(sql)
	
def edge_delete(id):
    return netopt_db_change('delete from Edge where id=%d' % id)
	
def get_edge(id):
	return netopt_db_query('select * from Edge where id=%d' % id)
	
def get_all_edges():
	return netopt_db_query('select * from Edge')
	
def delete_all_edges():
	return netopt_db_change('truncate Edge')
