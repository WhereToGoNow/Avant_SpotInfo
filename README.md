# SpotInfo

Script for getting spots' information from Google Places API

### Usage
- `python search.py -i input -o output -k api_key`
- Default value of `input` & `output`: `input.txt`, `output.json`
- Example: `$ python search.py -i input.txt -o output.json -k Alza...ff`

### Requirements
- Python 2.X (Currently: Not work in python 3.X)

### Dependencies
- [Python Client for Google Maps Services](https://github.com/googlemaps/google-maps-services-python)

### Currently extracted information
Attributes marked with \* can be `null`.
- Website\*
- Rating\*
- UTC offset
- Place ID
- Phone number\*
- Address
- Types
- Icon (URL form)
- Name (Exact name used in Google Maps API)
- URL (in Google Maps API)
- Opening hours\*
- Vicinity
- Location (Latitude & longitude)

