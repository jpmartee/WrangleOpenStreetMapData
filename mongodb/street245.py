from pymongo import MongoClient
import pprint

client = MongoClient()
db = client['maps']

strange_street = db.santacruz.find({'address.street':'245'})
pprint.pprint(list(strange_street))