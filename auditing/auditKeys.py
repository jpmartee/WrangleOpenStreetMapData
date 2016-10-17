import xml.etree.cElementTree as ET
import pprint

def audit_keys(osmfile):
	"""
	Function parses through xml file to count key types for nodes 
	and ways

	Args:
		osmfile(xml): OpenStreetMaps data in xml format
	Returns:
		keys(dict): A dictionary of keys/counts in the file
	"""
	osm_file = open(osmfile, 'r')
	keys = dict()
	for event, elem in ET.iterparse(osm_file, events=("start",)):
		if elem.tag == 'node' or elem.tag == 'way':
			for tag in elem.iter('tag'):
				key = tag.attrib['k']
				if key in keys:
					keys[key] += 1
				else:
					keys[key] = 1
	return keys

keys_dict = audit_keys('../santa-cruz_california.osm')
print 'Unique keys', len(keys_dict)
pprint.pprint(keys_dict) 