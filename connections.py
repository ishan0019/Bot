import 
import os

class SearchHistory:
	def __init__(self, user, id):
		self.user = user
		self.userId = id
		self.connection = None
		self.cursor = None

	def connectionStart(self):
		con = psycopg2.connect(user = "postgres",
                                  password = os.environ['DB_PASS'],
                                  host = os.environ['HOST'],
                                  port = "5432",
                                  database = "database-1")
		
		return con

	def connectionClose(self):
		if self.connection:
			self.cursor.close()
			self.connection.close()
			print("PostgreSQL connection is closed")

	def setMessage(self, log):
		if log:
			try:
				self.connection = self.connectionStart()
				self.cursor = self.connection.cursor()		
				timestamp = ''
				query = "INSERT INTO BotHistory (userId, username, log) VALUES (%s,%s,%s)"
				# print(self.userId)
				# print(self.user)
				record = (self.userId, str(self.user), str(log))
				self.cursor.execute(query, record)
				self.connection.commit()
				print ("Record inserted successfully")

			except (Exception, psycopg2.Error) as error :
			    if(self.connection):
			        print("Failed to insert record into BotHistory table", error)

			finally:
				self.connectionClose()
			        

	def getMessage(self, key):
		try:
			self.connection = self.connectionStart()
			self.cursor = self.connection.cursor()
			query = "select log from BotHistory where userId=%s and log like %s"
			self.cursor.execute(query, (self.userId, str(key)))
			record = self.cursor.fetchone()
			# print(record)
			return record
		except (Exception, psycopg2.Error) as error :
		    if(self.connection):
		        print("Failed to fetch record from BotHistory table", error)

		finally:
			self.connectionClose()
