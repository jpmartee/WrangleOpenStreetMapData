from pymongo import MongoClient
import pprint

client = MongoClient()
db = client['maps']

amenity = db.santacruz.aggregate([
        {
            '$match':{'amenity':{'$exists':1}}
        },
        {
            '$group':{'_id':'$amenity', 'count':{'$sum':1}}
        },
        {
            '$sort':{'count':-1}
        },
        {
            '$limit':10
        }
    ])

print 'Top 10 Amenities'
for doc in amenity:
    print doc