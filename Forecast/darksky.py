from xml.etree import ElementTree as ET
import urllib, urllib2
import json

def formatTemp(t, f):
	"""
	Input: temperature float in Fahrenheit, format string ('F', 'C', or 'K')
	Returns: formatted temp string
	"""
	f = f.lower()
	if f == 'f':
		return '%i'%t + u'\u2109'
	if f == 'c':
		return '%i'%((t-32)/1.8) + u'\u2103'
	if f == 'k':
		return '%i'%((t-32)/1.8+273.2) + u'\u212A'
	return 'TEMPERATURE FORMAT ERROR'

def forecast(APIKEY, LAT, LONG, FCK):
	"""
	Input: api key string, signed latitude float string, signed longitude float string, temperature format string
	Returns: XML data formatted for Alfred
	"""
	# GET JSON DATA
	url = 'https://api.forecast.io/forecast/' + APIKEY + '/' + LAT + ',' + LONG
	response = urllib2.urlopen(url)
	response_items = response.read()
	item = json.loads(response_items)
	# PARSE ITEMS
	xml = []
	# WEATHER DATA OUTSIDE THE U.S. DOES NOT HAVE MINUTELY DATA
	currentdata = item.get(u'minutely', u'currently')
	currentsummary = currentdata[u'summary']
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
