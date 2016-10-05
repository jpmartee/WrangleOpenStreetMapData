from pymongo import MongoClient
import pprint

client = MongoClient()
db = client['maps']

users = db.santacruz.distinct('created.user')

top_users = db.santacruz.aggregate([
    {
        '$group': {'_id':'$created.user', 'contributions':{'$sum':1}}
    },
    {
        '$sort':{'contributions':-1}
    },
    {
        '$limit':10
    }
    ])

print 'Unique users:', len(users)
print '\nTop 10 contributing users'
for doc in top_users:
    print doc