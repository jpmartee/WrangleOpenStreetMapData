from pymongo import MongoClient
import pprint

client = MongoClient()
db = client['maps']

db.santacruz.update_one(
    {'address.street':'245'},
    {'$set':{'address':
                {'housenumber':'245',
                'street':'Mount Hermon Road',
                'unit':'A',
                'city':'Scotts Valley',
                'state':'CA',
                'postcode':'95066'}
               }
    }
)

updated_entry = db.santacruz.find({'id':'2610436134'})

pprint.pprint(list(updated_entry))