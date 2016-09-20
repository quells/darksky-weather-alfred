Alfred Weather Powered by Dark Sky
==================================

A Python script to display the current weather conditions from the Dark Sky API in Alfred. You will need Alfred 3 and a free Dark Sky API key to use this.

# Installation

[Download](https://github.com/quells/darksky-weather-alfred2/blob/master/Weather.alfredworkflow?raw=true)

To install the Dark Sky Weather workflow, double click on ```Weather.alfredworkflow``` or drag the workflow to the workflow window in Alfred.

1. Use the [registration form](https://darksky.net/dev/register) to create a free Dark Sky developer account to get an API key.
2. [Find your latitude and longitude](http://stevemorse.org/jcal/latlon.php), but don’t use more than 4 decimal places.
3. Decide what units you would like to use for temperature. Options include Fahrenheit, Celsius, and Kelvin.

Next, edit the first script filter by double clicking on it. Edit the line ```print darksky(“APIKEY”, “LAT”, “LONG”, “TEMP_UNITS”)``` to fill in your Dark Sky API key, location, and unit preference. Be sure to keep these in quotes.

Example: ```print darksky(“abc123”, “52.2053”, “0.1218”, “C”)```

# How to use

Simply type ```weather``` (or whatever you configure) into Alfred. If your API access is successful, the current temperature and weather condition should appear followed by a summary of weather in the near future.

If you want more information, hit ```enter``` once the current weather has been displayed. This will open [Dark Sky](http://darksky.net) in the default browser.

# Disclaimer

The Dark Sky name and logo are wholly owned by The Dark Sky Company, LLC. Kai Wells does not own or claim to own anything related to Dark Sky.

# Version History

## 1.3 - September 20, 2016

- Updated README to reflect the change in branding from 'Forecast.io' to 'Powered by Dark Sky'.
- Changed `forecast()` to `darksky()`.
- Updated script to move away from deprecated Forecast.io API.
- Updated script to keep everything in JSON rather than converting to XML.
- Changed output formatting to emphasize weather conditions over temperature.
- Changed workflow icon from Forecast.io to Dark Sky.

## 1.2.3 - March 12, 2014

- Updated script to use Unicode "degree Fahrenheit", "degree Celsius", and "Kelvin" rather than letters in FCK() (hat tip to [jwisser](https://github.com/jwisser/darksky-weather-alfred2)). It will also accept either lowercase or uppercase letters.
- Updated script to use a dict.get() call instead of try: except KeyError: to deal with differences between US and international data sets.
- Added function documentation to forecast().

## 1.2.2 - April 15, 2013

- Added units preference for temperature.

## 1.2.1 - April 6, 2013

- Bug fix for international locations.
- Fixed method for opening Forecast.io with the location set in Alfred.

## 1.2 - April 4, 2013

- Updated script to use the new Forecast.io API rather than the Dark Sky API.
- Workflow now opens Forecast.io instead of Accuweather.com when an item is selected.
- Includes a forecast for today and tomorrow in addition to the current conditions.
- Uses Forecast.io icon instead of Dark Sky icon.

## 1.1 - February 6, 2013

- Updated script to use the JSON module instead of a bash script.
- Added Accuweather.com support.
- Added ‘Fetching Data…’ subtext while the script is running.

## 1.0 - January 25, 2013

- Commit: Initial Release
