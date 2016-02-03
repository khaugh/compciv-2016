# About the dataset
The San Francisco Department of Public Works has a spreadsheet of food truck permits given. It is updated daily, and includes the vendor's name, the permit number, location, description of the food, and much more.


# Basic facts
-Source: <a href = "http://www.sfdpw.org">SF Department of Public Works</a>
-Landing page: <a href="https://data.sfgov.org/Economy-and-Community/Mobile-Food-Schedule/jjew-r69b">Mobile Food Schedule</a>
-Direct link to data:
-Data format: CSV
-Rows: 1080


# Data fields

### DayOrder
integer - the number corresponding to the day of the week the permit is valid for (0 = Sunday, 1 = Monday, etc)

### starttime
string - the opening time the permit is valid for (i.e. "9AM")

### endtime
string - the closing time the permit is valid for

### permit
string - permit number (i.e. "15MFF-0149")

### PermitLocation
string - address of the food truck

### optionaltext
string - description of the food items sold

### locationid
integer - location id of the food truck

### start24
string - opening time in 24 hour format (i.e. "15:00")

### end24
string - closing time in 24 hour format

### Applicant
string - name of the permit holder (i.e. "Sun Rise Catering")

### Latitude
float - latitude of the food truck's address

### Longitude
float - longitude of the food truck's address


# Data wrangling
-Food trucks often have many permits for different days and time slots. All of the permits for the same food truck have the same permit id, but it will be a challenge to group them all together to not get duplicates
-I want to be able to filter only for food trucks that are open at the time of the search. This will probably require converting the openi
ng/closing time strings into another format
-I also am thinking about filtering by type of food, so if the user inputs "indian food" it will print the closest few trucks whose description have "indian food" in it. This will probably take some tricky string manipulation
