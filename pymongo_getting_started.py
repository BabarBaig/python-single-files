
import pymongo

from pymongo import Connection
connection=Connection('localhost',27017)

db=connection.test
names=db.names		#var names=db.names collection
item=names.find_one()	#item gets an item from collection names
print item['name']	#print value corresponding to item: name

