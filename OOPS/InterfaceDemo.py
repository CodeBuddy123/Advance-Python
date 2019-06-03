from abc import *

class DBInterface(ABC):
	@abstractmethod
	def connect(self):
		pass             #Techincally, there  is no concept of interfaces in python
	@abstractmethod      #An abstract class with only abstract methods can be considered as Interface
	def disconnect(self):
		pass

class Oracle(DBInterface):         #Oracle is implementing the logic in its own way
	def connect(self):
		print('Oracle database connecting...')

	def disconnect(self):
		print('Oracle database disconnecting...')

class MySql(DBInterface):          #MySql has its own implementation for the Interface
	def connect(self):
		print('MySql database connecting')
	def disconnect(self):
		print('MySql database disconnecting..')

o=Oracle()
o.connect()
o.disconnect()

m=MySql()
m.connect()
m.disconnect()