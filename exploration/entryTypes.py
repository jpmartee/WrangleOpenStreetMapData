from pymongo import MongoClient
import pprint

client = MongoClient()
db = client['maps']

docs = db.santacruz.find().count()
nodes = db.santacruz.find({'type':'node'}).count()
ways = db.santacruz.find({'type':'way'}).count()

print 'Number of documents:', docs
print '\nNumber of nodes:', nodes
print '\nNumber of ways:', ways