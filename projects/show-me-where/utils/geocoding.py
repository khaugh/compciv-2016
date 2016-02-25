import requests

def geocode(location):
	"""
	Geocodes a location with the Mapzen search API

	What it expects:
	-Expects a string representing a location
	-Expects the CREDS_FILE variable to point to a file that contains
	a Mapzen search API key

	What it does:
	-Opens and reads the CREDS_FILE to get the API key
	-Calls the Mapzen search with an HTTP request using the given
	search key and location string
	-Deserializes the data returned from Mapzen into JSON format
	-Creates a dictionary of this deserialized information	
	
	What it returns:
	Returns a dictionary with key value pairs as listed below:
	- query_text: the `location` string provided by the user
    	- label: the string label that Mapzen provides in describing the found location
    	- confidence: a float representing the confidence value that Mapzen has in its result.
    	- latitude: a float representing the latitude coordinate
    	- longitude: a float representing the longitude coordinate
    	- status: "OK", a string that indicates a result was found. Else, None	
	"""
	raw_string = fetch_mapzen_response(location)
	#location_dict = parse_mapzen_response(raw_string)
	#return location_dict
	return raw_string

def fetch_mapzen_response(location):
	"""
	`location` is a string that will be passed onto Mapzen API for geocoding.
	Returns a text string containing JSON-formatted data from Mapzen.
	"""

	url = 'https://search.mapzen.com/v1/search?'
	myparams = {'text' : location, 'api_key' : read_mapzen_credentials()}
	resp = requests.get(url, params = myparams)
	return resp.text

def read_mapzen_credentials():
	return open('creds_mapzen.txt').read().strip()
