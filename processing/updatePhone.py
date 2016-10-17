import re

def update_phone(phoneNumber):
	"""Function updates phone number to xxx-xxx-xxxx format"""
	rePhone = re.compile(r'(\d{3})(\D*)(\d{3})(\D*)(\d{4})')
	m = rePhone.search(phoneNumber)
	phone = None
	if m:
		phone = m.group()
		phone = phone.replace(' ', '').replace('-','').replace(')','')
		phone = phone[0:3] + '-' + phone[3:6] + '-' + phone[6:]
	return phone