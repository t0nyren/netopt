from model import *

def topology_insert(item):
	sql = 'insert into Topology(from_node,to_node)\
			 values(%d, \'%d\') \
		  ' % (item[0],item[1])
	#print sql
	return netopt_db_change(sql)

def topology_update(id, item):
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
			
	sql = 'update Topology set %s where id=%d' % (ops, id)
	#print sql 
	return netopt_db_change(sql)
	
def topology_delete(id):
    return netopt_db_change('delete from Topology where id=%d' % id)
	
def get_topology():
	return netopt_db_query('select * from Topology')
	
def delete_topology():
	return netopt_db_change('truncate Topology')
	
def save_topology(T):
	for t in T:
		topology_insert(t)
