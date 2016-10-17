import xml.etree.cElementTree as ET
import pprint

def is_phone(elem):
	"""Return boolean indicating if element key is phone"""
	return (elem.attrib['k'] == 'phone')


def audit_phonenumbers(osmfile):
	"""
	Function parses through xml file to audit phone numbers

	Args:
		osmfile(xml): OpenStreetMaps data in xml format
	Returns:
		phonenumbers(set): A set of phone numbers
		in the file
	"""
	osm_file = open(osmfile, 'r')
	phonenumbers = set()
	for event, elem in ET.iterparse(osm_file, events=('start',)):
		if elem.tag == 'node' or elem.tag == 'way':
			for tag in elem.iter('tag'):
				if is_phone(tag):
					phonenumbers.add(tag.attrib['v'])
	return phonenumbers


pprint.pprint(audit_phonenumbers('../santa-cruz_california.osm'))