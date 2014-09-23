from model import *

def node_insert(item):
	sql = 'insert into Node(id,bandwidth,workload)\
			 values(%d, \'%f\', \'%f\') \
		  ' % (item['id'],item['bandwidth'],item['workload'])
	#print sql
	return netopt_db_change(sql)

def node_update(id, item):
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
			
	sql = 'update Node set %s where id=%d' % (ops, id)
	#print sql
	return netopt_db_change(sql)
	
def node_delete(id):
    return netopt_db_change('delete from Node where id=%d' % id)
	
def get_node(id):
	return netopt_db_query('select * from Node where id=%d' % id)
	
def get_all_nodes():
	return netopt_db_query('select * from Node')
	
def delete_all_nodes():
	return netopt_db_change('truncate Node')