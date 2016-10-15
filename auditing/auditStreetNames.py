import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

OSMFILE = 'santa-cruz_california.osm'
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)

# Acceptable street types
expected = ['Street', 'Avenue', 'Boulevard', 'Drive', 'Court', 'Place', 
            'Square', 'Lane', 'Road', 'Trail', 'Parkway', 'Commons', 'Way']

def audit_street_type(street_types, street_name):
    """
    Function adds unexpected street endings to a dictionary where key is
    last word and value is full street name

    Args:
        street_types(dict): keys are unexpected street types and values
                            are full street names of that type
        street_name(string): street name to be analyzed
    Returns:
        None
    """
    # Search for street ending
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        # Add to dictionary if not expected
        if street_type not in expected:
            street_types[street_type].add(street_name)

def is_street_name(elem):
    """Return boolean indicating if element key is street"""  
    return (elem.attrib['k'] == 'addr:street')

def audit_street_names(osmfile):
    """
    Function parses through xml file to audit street names using
    audit_street_type funtion

    Args:
        osmfile(xml): OpenStreetMaps data in xml format
    Returns:
        street_types(dict): keys are unexpected street types and values
                            are full street names of that type
    """
    osm_file = open(osmfile, 'r')
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=('start',)):

        if elem.tag == 'node' or elem.tag == 'way':
            for tag in elem.iter('tag'):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])

    return street_types

st_types = audit_street_names(OSMFILE)
print 'Unexpected endings:', len(st_types)
pprint.pprint(dict(st_types))
