import MySQLdb
class Database:
	host='localhost'
	user='root'
	password='123'
	db='test'
	def __init__(self):
		self.connection=MySQLdb.connect(self.host,self.user,self.password,self.db)
		self.cursor=self.connection.cursor()
	def insert(self,query):
		try:
			self.cursor.execute(query)
			self.connection.commit()
		except:
			self.connection.rollback()
	def query(self,query):
		cursor=self.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute(query)
		return cursor.fetchall()
	def __del__(self):
		self.connection.close()
obj=Database()
del_query="DELETE FROM basic_python_database"
obj.insert(del_query)
query="""INSERT INTO basic_python_database ('name','age') VALUES ('Saqib',21),('Naushin',12)"""
obj.query(query)
obj.insert(query)
select_query="""SELECT * FROM basic_python_database WHERE age=21"""
people=obj.query(select_query)
for person in people:
	print "Found %s" %person['name']