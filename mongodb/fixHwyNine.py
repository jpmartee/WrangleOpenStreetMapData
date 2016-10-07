from pymongo import MongoClient
import pprint

client = MongoClient()
db = client['maps']

db.santacruz.update_many(
    {
        'address.street':{'$in':['Hwy 9', 'Hwy. 9']}
    },
    {
        '$set':{'address.street':'Highway 9'}
    }
)

# look up entries to double check work
updated_entries = db.santacruz.find({'id':{'$in':['2338593307', '2371463445']}})
pprint.pprint(list(updated_entries))
