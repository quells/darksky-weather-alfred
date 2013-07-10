Forecast.io in Alfred 2
===============

A Python script to display the current weather conditions from the Forecast.io API in the Alfred window. You will need Alfred 2 and a free Forecast.io API key to use this.

# Installation

To install the Forecast.io Weather workflow, double click on ```Forecast.alfredworkflow``` or drag the workflow to the workflow window in Alfred.

1. Use the [registration form](https://developer.forecast.io/register) to create a free Forecast.io developer account to get an API key.
2. [Find your latitude and longitude](http://stevemorse.org/jcal/latlon.php), but don’t use more than 4 decimal places.
3. Decide what units you would like to use for temperature. Options include Fahrenheit, Celsius, and Kelvin.

Next, edit the first script filter by double clicking on it. Edit the line ```print forecast(“APIKEY”, “LAT”, “LONG”, “FCK”)``` to fill in your Forecast.io API key, location, and unit preference. Be sure to keep these in quotes.

Example: ```print forcast(“APIKEY”, “52.2053”, “0.1218”, “C”)```

# How to use

Simply type ```weather``` (or whatever you configure) into Alfred. If your API access is successful, the current temperature and weather condition should appear followed by a summary of weather in the near future.

If you want more information, hit ```enter``` once the current weather has been displayed. This will open [Forecast.io](http://forecast.io) in Safari.

# Based upon

[Dan Palmer's reddit workflow](http://danpalmer.me/blog/articles/2013-01-12-reddit-workflow-for-alfred-20.html)

An Alfred v1 extension for the Dark Sky API on [Hack / Make](http://hackmake.org/2012/11/dark-sky-alfred-extension)

# Download

[Forecast.alfredworkflow](https://github.com/quells/darksky-weather-alfred2/blob/master/Forecast.alfredworkflow?raw=true)

# Disclaimer

The Forecast and Dark Sky names and logos are wholly owned by The Dark Sky Company, LLC. Kai Wells does not own or claim to own anything related to Forecast or Dark Sky.

# Version History

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