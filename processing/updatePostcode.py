import re

def update_postcode(postcode):
	"""Function updates postcode to 5 digit version"""
	rePostcode = re.compile(r'([9]\d{4})')
	updated = None
	m = rePostcode.search(postcode)
	if m:
		updated = m.group()	
	return updated