from pymongo import MongoClient
import pprint

client = MongoClient()
db = client['maps']

streetnames = db.santacruz.aggregate([
        {
            '$match':{'address.street':{'$exists':1}}
        },
        {
            '$group':{'_id':'$address.street', 'count':{'$sum':1}}
        },
        {
            '$sort':{'count':-1}
        },
        {
            '$limit':15
        }
    ])

print "Street names"
for doc in streetnames:
    print doc