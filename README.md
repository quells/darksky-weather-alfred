Dark Sky Weather in Alfred 2
====================

A python script to display the current weather condition from the Dark Sky API in the Alfred window. You will need Alfred Version 2 and a free Dark Sky API key to use this.

# Installation

To install the Dark Sky Weather workflow, double click on ```Dark Sky Weather.alfredworkflow``` or drag the workflow to the workflow window in Alfred.

Next, edit the first script filter by double clicking on it. Edit the line ```print forecast(“APIKEY”, “LAT”, “LONG”))``` to fill in your Dark Sky API key and location. Be sure to keep these in quotes.

Use the [registration form](https://developer.darkskyapp.com/register) to create a free Dark Sky developer account to get an API key. [Find your latitude and longitude](http://stevemorse.org/jcal/latlon.php), but don’t use more than 4 decimal places.

# How to use

Simply type ```weather``` (or whatever you configure) into Alfred. If your API access is successful, the current temperature and weather condition should appear followed by a summary of weather in the near future.

# Based upon

[Dan Palmer's reddit workflow](http://danpalmer.me/blog/articles/2013-01-12-reddit-workflow-for-alfred-20.html)

[Run BASH built-in commands in Python?](http://stackoverflow.com/questions/5460923/run-bash-built-in-commands-in-python), a question from [duanedesign](http://stackoverflow.com/users/401815/duanedesign)

# Download

[Dark Sky Weather](https://github.com/quells/darksky-weather-alfred2/blob/master/Dark%20Sky%20Weather.alfredworkflow)

# Copyright

The Dark Sky name and logo are wholly owned by The Dark Sky Company, LLC. Kai Wells does not own or claim to own anything related to Dark Sky.

# Version History

## 1.0 - January 25, 2013

- Commit: Initial Release