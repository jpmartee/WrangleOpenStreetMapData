import xml.etree.cElementTree as ET
import pprint

def is_amenity(elem):
	"""Return boolean indicating if element key is postcode"""
	return (elem.attrib['k'] == 'amenity')


def audit_amenities(osmfile):
	"""
	Function parses through xml file to count amenities for nodes 
	and ways

	Args:
		osmfile(xml): OpenStreetMaps data in xml format
	Returns:
		amenities(dict): A count dictionary of amenities in the file
	"""
	osm_file = open(osmfile, 'r')
	amenities = dict()
	for event, elem in ET.iterparse(osm_file, events=('start',)):
		if elem.tag == 'node' or elem.tag == 'way':
			for tag in elem.iter('tag'):
				if is_amenity(tag):
					amenity = tag.attrib['v']
					if amenity in amenities:
						amenities[amenity] += 1
					else:
						amenities[amenity] = 1
	return amenities

amenities_dict = audit_amenities('../santa-cruz_california.osm')
print 'Unique amenities', len(amenities_dict)
pprint.pprint(amenities_dict) 