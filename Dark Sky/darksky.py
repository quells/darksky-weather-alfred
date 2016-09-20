#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

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
		return '%.1f'%((t-32)/1.8+273.2) + u'\u212A'
	return 'TEMPERATURE FORMAT ERROR'

def darksky(APIKEY, LAT, LONG, TEMP_UNITS):
	"""
	Input: api key string, signed latitude float string, signed longitude float string, temperature format string
	Returns: JSON data formatted for Alfred
	"""
	# GET JSON DATA
	url = 'https://api.darksky.net/forecast/' + APIKEY + '/' + LAT + ',' + LONG
	response = urllib2.urlopen(url)
	response_items = response.read()
	item = json.loads(response_items)
	latlongarg = LAT + ',' + LONG
	# PARSE ITEMS
	currentData = item.get(u'currently')
	currentText = 'Now: ' + formatTemp(currentData[u'temperature'], TEMP_UNITS) + ', ' + currentData[u'summary'].capitalize()
	
	todayData = item.get(u'daily').get(u'data')[0]
	todayText = 'Today: ' + todayData.get(u'summary').capitalize()
	todaySubtitle = formatTemp(todayData.get(u'temperatureMin'), TEMP_UNITS) + u' – ' + formatTemp(todayData.get(u'temperatureMax'), TEMP_UNITS)
	
	tmrwData = item.get(u'daily').get(u'data')[1]
	tmrwText = 'Tomorrow: ' + tmrwData.get(u'summary').capitalize()
	tmrwSubtitle = formatTemp(tmrwData.get(u'temperatureMin'), TEMP_UNITS) + u' – ' + formatTemp(tmrwData.get(u'temperatureMax'), TEMP_UNITS)
	
	response = {'items': [{
		'uid': 'currentWeather',
		'title': currentText,
		'arg': latlongarg
	},{
		'uid': 'todayWeather',
		'title': todayText,
		'subtitle': todaySubtitle,
		'arg': latlongarg
	},{
		'uid': 'tomorrowWeather',
		'title': tmrwText,
		'subtitle': tmrwSubtitle,
		'arg': latlongarg
	}]}
	
	return json.dumps(response)