import xml.etree.cElementTree as ET
import codecs
import json
import re
from updateName import update_name
from updatePostcode import update_postcode
from updatePhone import update_phone

# Maps endings to proper edits
mapping = { 'St': 'Street',
			'St.': 'Street',
			'Rd': 'Road',
			'Ave': 'Avenue',
			'Dr': 'Drive',
			'Cedar': 'Cedar Street',
			'Chestnut': 'Chestnut Street',
			'front': 'Front Street',
			'Front': 'Front Street',
			'Merrill': 'Merrill Street',
			'Pacific': 'Pacific Avenue',
			'Seabright': 'Seabright Avenue'
		}

lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r"[=\+/&<>;\''\?%#$@\,\. \t\r\n]")

# attributes in the CREATED array should be added under a key 'created'
CREATED = ['version', 'changeset', 'timestamp', 'user', 'uid']


def shape_element(element):
	"""Function coverts element to json format"""
	node = {}
	if element.tag == 'node' or element.tag == 'way' :
		# keep track of type
		node['type'] = element.tag
		node['created'] = {}
		for key in element.attrib.keys():
			# attributes of 'node' and 'way' should be turned into
			# regular key/value pairs
			# attributes in the CREATED array should be added under a
			# key 'created'
			if key in CREATED:
				node['created'][key] = element.attrib[key]
					
			elif key not in ['lat', 'lon']:
				node[key] = element.attrib[key] 

		# attributes for latitude and longitude should be added to a
		# 'pos' array. Not all entries will have latitude and longitude
		try:
			lat = float(element.attrib['lat'])
			lon = float(element.attrib['lon'])
			node['pos'] = [lat, lon]
		except:
			pass
		
		# if second level tag 'k' value contains problematic characters,
		# it should be ignored
		for child in element:
			
			if child.tag == 'tag':   
				key = child.attrib['k']
				value = child.attrib['v']
				if re.search(problemchars, key):
					continue
				# if second level tag 'k' value starts with 'addr:', it
				# should be added to a dictionary 'address'
				if key.startswith('addr:'):
					# if there is a second ':' that separates the
					# type/direction of a street, the tag should be
					# ignored
					if re.search(lower_colon, key[5:]):
						continue
					
					# update street names using mapping if necessary
					elif key == 'addr:street':
						new_value = update_name(value, mapping)
						if 'address' in node:
							node['address']['street'] = new_value
						else:
							node['address'] = {}
							node['address']['street'] = new_value
					
					# fix postal codes
					elif key == 'addr:postcode':
						new_value = update_postcode(value)
						if 'address' in node:
							node['address']['postcode'] = new_value
						else:
							node['address'] = {}
							node['address']['postcode'] = new_value
					
					else:
						if 'address' in node:
							node['address'][key[5:]] = value
						else:
							node['address'] = {}
							node['address'][key[5:]] = value
				
				# fix phone numbers
				elif key == 'phone':
					new_value = update_phone(value)
					node['phone'] = new_value

				# if second level tag 'k' value does not start with 
				# 'addr:', but contains ':', you can process it same
				# as any other tag.
				else:
					node[key] = value
			
			# second level 'nd' tags should be made into an array
			elif child.tag == 'nd':
				if 'node_refs' in node:
					node['node_refs'].append(child.attrib['ref'])
				else:
					node['node_refs'] = []
					node['node_refs'].append(child.attrib['ref'])
				
		return node
	else:
		return None


def process_map(file_in, pretty=False):
	"""
		Function processes OSM using shape_element and writes to json file
	"""
	file_out = '{0}.json'.format(file_in)
	data = []
	with codecs.open(file_out, 'w') as fo:
		for _, element in ET.iterparse(file_in):
			node = shape_element(element)
			if node:
				data.append(node)
				if pretty:
					fo.write(json.dumps(node, indent=2)+'\n')
				else:
					fo.write(json.dumps(node) + '\n')
	return None


process_map('../santa-cruz_california.osm')