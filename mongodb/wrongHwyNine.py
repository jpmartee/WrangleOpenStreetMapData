from pymongo import MongoClient
import pprint

client = MongoClient()
db = client['maps']

wrong_hwy_nine = db.santacruz.find({'address.street':{'$in':['Hwy 9', 'Hwy. 9']}})

pprint.pprint(list(wrong_hwy_nine))