from utils.geocoding import geocode

command = input("What do you want to do? ")

if command == 'hello':
	name = input('What is your name? ')
	print('Hello', name)
elif command == 'geocode':
	location = input('What is your location? ')
	print('Geocoding \"', location, '\"...', sep = "")
	result = geocode(location)
	print(result)
elif command == 'help':
	print(geocode.__name__)
	print(geocode.__doc__)
else:
	print("Sorry, I don't know how to respond to", command)
