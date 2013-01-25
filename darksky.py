from xml.etree import ElementTree as ET
import string
from subprocess import Popen, PIPE, STDOUT
import re

def forecast(APIKEY, LAT, LONG):
	bash = '"curl -s https://api.darkskyapp.com/v1/brief_forecast/' + APIKEY + '/' + LAT + ',' + LONG + '"'
	forecast = str(Popen('bash -i -c ' + bash, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT).communicate()).split(',')
	# REGEX
	quot = re.compile("\"")
	# HARVEST
	temp = forecast[0].split(":")[2]
	condition = quot.sub("", forecast[1].split(":")[1])
	condition = condition.capitalize()
	weather = temp + "F, " + condition
	future = quot.sub("", forecast[3].split(":")[1]) + "."
	future = future.capitalize()
	xml = []
	xml.append({
		'title': weather,
		'subtitle': future,
		'arg': 'arg',
		'uid': '123456789',
		'icon': 'darksky.png'
		})
	# PLANT XML TREE
	xml_items = ET.Element('items')
	for item in xml:
		xml_item = ET.SubElement(xml_items, 'item')
		for key in item.keys():
			if key is 'uid' or key is 'arg':
				xml_item.set(key, item[key])
			else:
				child = ET.SubElement(xml_item, key)
				child.text = item[key]
	return ET.tostring(xml_items)