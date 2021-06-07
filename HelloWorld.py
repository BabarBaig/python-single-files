import bottle
import pymongo

# This is the handler for the root address of the web server
@bottle.route('/')
def index():
	from pymongo import Connection
	connection = Connection('localhost',27017)	#Get a connection to db
	db = connection.test	#Attach to test db
	names=db.names			#Get a handle for the names collection
	item=names.find_one()	#Find single item from names
	return '<b>Hello %s!<b>' % item['name']

bottle.run(host='localhost',port=8082)
