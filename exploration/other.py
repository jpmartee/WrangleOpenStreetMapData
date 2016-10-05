from pymongo import MongoClient
import pprint

client = MongoClient()
db = client['maps']

cuisine = db.santacruz.aggregate([
        {
            '$match':{'cuisine':{'$exists':1}}
        },
        {
            '$group':{'_id':'$cuisine', 'count':{'$sum':1}}
        },
        {
            '$sort':{'count':-1}
        },
        {
            '$limit':5
        }
    ])


religion = db.santacruz.aggregate([
        {
            '$match':{'religion':{'$exists':1}}
        },
        {
            '$group':{'_id':'$religion', 'count':{'$sum':1}}
        },
        {
            '$sort':{'count':-1}
        }
        
    ])


denomination = db.santacruz.aggregate([
        {
            '$match':{'religion':'christian','denomination':{'$exists':1}}
        },
        {
            '$group':{'_id':'$denomination', 'count':{'$sum':1}}
        },
        {
            '$sort':{'count':-1}
        }
    ])


print 'Most popular cuisine'
for doc in cuisine:
    print doc
    
print '\nReligions'
for doc in religion:
    print doc
    
print '\nChristian denominations'
for doc in denomination:
    print doc