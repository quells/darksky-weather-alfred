from xml.etree import ElementTree as ET
import urllib, urllib2
import json

def formatTemp(t, f):
	"""
	Input: temp float in Fahrenheit, format string (F, C, K)
	Returns: formatted temp string
	"""
	if f == 'C':
		return str(int((t-32)/1.8*100)/100) + 'C'
	elif f == 'K':
		return str(int(((t-32)/1.8+273.15)*100)/100) + 'K'
	else:
		return str(int(t*100)/100) + 'F'

def forecast(APIKEY, LAT, LONG, FCK):
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
		'title': formatTemp(item[u'currently'][u'temperature'], FCK) + ', ' + currentsummary.capitalize(),
		'subtitle': item[u'hourly'][u'summary'].capitalize(),
		'arg': LAT + ',' + LONG,
		'icon': 'icon.png'
	})
	xml.append ({
		'title': 'Today: ' + formatTemp(item[u'daily'][u'data'][0][u'temperatureMin'], FCK) + ' - ' + formatTemp(item[u'daily'][u'data'][0][u'temperatureMax'], FCK),
		'subtitle': item[u'daily'][u'data'][0][u'summary'].capitalize(),
		'arg': LAT + ',' + LONG,
		'icon': 'icon.png'
	})
	xml.append ({
		'title': 'Tomorrow: ' + formatTemp(item[u'daily'][u'data'][1][u'temperatureMin'], FCK) + ' - ' + formatTemp(item[u'daily'][u'data'][1][u'temperatureMax'], FCK),
		'subtitle': item[u'daily'][u'data'][1][u'summary'].capitalize(),
		'arg': LAT + ',' + LONG,
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