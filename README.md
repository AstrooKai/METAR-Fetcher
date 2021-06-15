## METAR Fetcher
This repository provides python scripts that fetch METAR data from an airport and logs them in the terminal or console, METAR data are fetched from <a href="https://checkwx.com">CheckWX API</a>.

**Currently Supported Country Scripts**
1. Philippines

## About METAR
METAR also known as Meteorological Terminal Air Report is a format of weather information report used in aviation, METAR is used by pilots to know the condition of the weather before taking off or landing. A typical METAR contains data for the temperature, dew point, wind direction and speed, precipitation, cloud cover and heights, visibility, and barometric pressure. A METAR may also contain information on precipitation amounts, lightning, and other information that would be of interest to pilots or meteorologists such as a pilot report or PIREP, colour states and runway visual range (RVR).

## Setup
The setup is easy, literally. You just put your API Key inside the value of the `apiKey` variable
```py
apiKey = "API KEY HERE"
```
