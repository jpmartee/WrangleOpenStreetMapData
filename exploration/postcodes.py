from pymongo import MongoClient
import pprint

client = MongoClient()
db = client['maps']

postcodes = db.santacruz.aggregate([
        {
            '$match':{'address.postcode':{'$exists':1}}
        },
        {
            '$group':{'_id':'$address.postcode', 'count':{'$sum':1}}
        },
        {
            '$sort':{'count':-1}
        }
    ])

print "Postal codes"
for doc in postcodes:
    print doc