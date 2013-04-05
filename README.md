Forecast.io in Alfred 2
===============

A Python script to display the current weather conditions from the Forecast.io API in the Alfred window. You will need Alfred 2 and a free Forecast.io API key to use this.

# Installation

To install the Dark Sky Weather workflow, double click on ```Forecast.alfredworkflow``` or drag the workflow to the workflow window in Alfred.

Use the [registration form](https://developer.forecast.io/register) to create a free Forecast.io developer account to get an API key. [Find your latitude and longitude](http://stevemorse.org/jcal/latlon.php), but don’t use more than 4 decimal places.

Next, edit the first script filter by double clicking on it. Edit the line ```print forecast(“APIKEY”, “LAT”, “LONG”))``` to fill in your Forecast.io API key and location. Be sure to keep these in quotes.

# How to use

Simply type ```weather``` (or whatever you configure) into Alfred. If your API access is successful, the current temperature and weather condition should appear followed by a summary of weather in the near future.

If you want more information, hit ```enter``` once the current weather has been displayed. This will open [Forecast.io](http://forecast.io) in Safari.

# Based upon

[Dan Palmer's reddit workflow](http://danpalmer.me/blog/articles/2013-01-12-reddit-workflow-for-alfred-20.html)

An Alfred v1 extension for the Dark Sky API on [Hack / Make](http://hackmake.org/2012/11/dark-sky-alfred-extension)

# Download

[Forecast.alfredworkflow](https://github.com/quells/darksky-weather-alfred2/blob/master/Forecast.alfredworkflow?raw=true)

# Copyright

The Forecast name and logo are wholly owned by The Dark Sky Company, LLC. Kai Wells does not own or claim to own anything related to Dark Sky.

# Version History

## 1.2 - April 4, 2013

- Updated script to use the new Forecast.io API rather than the Dark Sky API.
- Workflow now opens Forecast.io instead of Accuweather.com when an item is selected.
- Includes a forecast for today and tomorrow in addition to the current conditions.

## 1.1 - February 6, 2013

- Updated script to use the JSON module instead of a bash script.
- Added Accuweather.com support.
- Added ‘Fetching Data…’ subtext while the script is running.

## 1.0 - January 25, 2013

- Commit: Initial Release