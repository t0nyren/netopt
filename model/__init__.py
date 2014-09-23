from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

DB_URI = 'mysql://networkOpt:networkOptadmin@localhost/networkOpt'
netopt_db_engine = create_engine(DB_URI + '?charset=utf8',
						   encoding         = 'utf-8',
						   convert_unicode  = True,
						   pool_size        = 5,
						   max_overflow     = 100,
						   pool_recycle     = 9,
						   echo             = True 
						   )
						   
Base = declarative_base()
Base.metadata.create_all(bind=netopt_db_engine)
conn = scoped_session(sessionmaker(bind=netopt_db_engine))

def netopt_db_query(sql_comm):
		result = None
		#conn = tupai_db_engine.connect()
		#conn = self.application.db
		try:
			result = conn.execute(sql_comm)
			rows = result.fetchall()
			return rows
		except:
				raise
		finally:
				conn.close()
		return result

def netopt_db_change(sql_comm):
		#conn = tupai_db_engine.connect()
		#conn = self.application.db
		#trans = conn.begin()
		result = None
		try:
			result = conn.execute(sql_comm)
			conn.commit()
		except:
			conn.rollback()
			raise
		finally:
				conn.close()
		return result