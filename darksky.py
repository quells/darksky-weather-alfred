from xml.etree import ElementTree as ET
import urllib, urllib2
import json

def forecast(APIKEY, LAT, LONG):
	# GET JSON DATA
	url = 'https://api.forecast.io/forecast/' + APIKEY + '/' + LAT + ',' + LONG
	response = urllib2.urlopen(url)
	response_items = response.read()
	item = json.loads(response_items)
	# PARSE ITEMS
	xml = []
	while True:
		try:
			currentsummary = item[u'minutely'][u'summary']
			break
		except KeyError:
			currentsummary = item[u'currently'][u'summary']
			break
	xml.append ({
		'title': str(int(item[u'currently'][u'temperature']*100)/100) + 'F, ' + currentsummary.capitalize(),
		'subtitle': item[u'hourly'][u'summary'].capitalize(),
		'arg': LAT + ',' + LONG,
		'uid': str(int(item[u'hourly'][u'data'][0][u'time'])),
		'icon': 'icon.png'
	})
	xml.append ({
		'title': 'Today: ' + str(int(item[u'daily'][u'data'][0][u'temperatureMin']*100)/100) + 'F - ' + str(int(item[u'daily'][u'data'][0][u'temperatureMax']*100)/100) + 'F',
		'subtitle': item[u'daily'][u'data'][0][u'summary'].capitalize(),
		'arg': LAT + ',' + LONG + ',' + str(int(item[u'daily'][u'data'][0][u'time'])),
		'uid': str(int(item[u'daily'][u'data'][0][u'time'])),
		'icon': 'icon.png'
	})
	xml.append ({
		'title': 'Tomorrow: ' + str(int(item[u'daily'][u'data'][1][u'temperatureMin']*100)/100) + 'F - ' + str(int(item[u'daily'][u'data'][1][u'temperatureMax']*100)/100) + 'F',
		'subtitle': item[u'daily'][u'data'][1][u'summary'].capitalize(),
		'arg': LAT + ',' + LONG + ',' + str(int(item[u'daily'][u'data'][1][u'time'])),
		'uid': str(int(item[u'daily'][u'data'][1][u'time'])),
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