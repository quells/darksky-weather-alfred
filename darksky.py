from xml.etree import ElementTree as ET
import urllib, urllib2
import json

def forecast(APIKEY, LAT, LONG):
	# GET JSON DATA
	url = 'https://api.darkskyapp.com/v1/brief_forecast/' + APIKEY + '/' + LAT + ',' + LONG
	response = urllib2.urlopen(url)
	response_items = response.read()
	item = json.loads(response_items)
	# PARSE ITEMS
	xml = []
	xml.append ({
		'title': str(item[u'currentTemp']) + 'F, ' + item[u'hourSummary'].capitalize(),
		'subtitle': item[u'daySummary'].capitalize() + '.',
		'arg': "'" + LAT + ',' + LONG + "'",
		'uid': str(item[u'checkTimeout']),
		'icon': 'icon.png'
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