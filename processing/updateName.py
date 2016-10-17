import re

def update_name(name, mapping):
	"""
	Function updates street name according to mapping

	Args:
		name(string): street name
		mapping(dict): dictionary mapping unexpected types to 
					   proper types
	Returns:
		name(string): updated street name
	"""
	street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)
	m = street_type_re.search(name)
	m = m.group()
	if m in mapping.keys():
		name = name.replace(m, mapping[m])
	return name