from pymongo import MongoClient
import pprint

client = MongoClient()
db = client['maps']

db.santacruz.update_one(
    {
        'address.postcode':'1982'
    },
    {
        '$set':{'address.postcode':'95060'}
    }
)

updated_entry = db.santacruz.find({'id':'2830369542'})
pprint.pprint(list(updated_entry))