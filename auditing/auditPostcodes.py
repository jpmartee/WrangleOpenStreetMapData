import xml.etree.cElementTree as ET
import pprint

def is_postcode(elem):
	"""Return boolean indicating if element key is postcode"""
	return (elem.attrib['k'] == "addr:postcode")


def audit_postcodes(osmfile):
	"""
	Function parses through xml file to audit postcodes

	Args:
		osmfile(xml): OpenStreetMaps data in xml format
	Returns:
		postcodes(set): A set of postcodes in the file
	"""
	osm_file = open(osmfile, "r")
	postcodes = set()
	for event, elem in ET.iterparse(osm_file, events=("start",)):
		if elem.tag == "node" or elem.tag == "way":
			for tag in elem.iter("tag"):
				if is_postcode(tag):
					postcodes.add(tag.attrib['v'])
	return postcodes


pprint.pprint(audit_postcodes('santa-cruz_california.osm'))