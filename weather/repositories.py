# repositories.py

from django.conf import settings
import pymongo

class WeatherRepository:

	collection = ''
	
	def __init__(self, collectionName) -> None:
			self.collection = collectionName
			
	def getConnection(self):
		stringConnection = getattr(settings, "MONGO_CONNECTION_STRING")
		database = getattr(settings, "MONGO_DATABASE_NAME")
		client = pymongo.MongoClient(stringConnection)
		connection = client[database]
		return connection
			
	def getCollection(self):
		connection = self.getConnection()
		collection = connection[self.collection]
		return collection
			
	# CRUD
	
	def getById(self, id):
		document = self.getCollection().find_one({"_id": id})
		return document
    
	def getAll(self):
		documents = self.getCollection().find({})
		return documents
    
	def getByAttribute(self, attribute, value):
		documents = self.getCollection().find({attribute: value})
		return documents
    
	def insert(self, document):
		self.getCollection().insert_one(document)

	def delete(self, id):
		self.getCollection().delete_one({"_id": id})

	def deleteAll(self):
		self.getCollection().delete_many({})