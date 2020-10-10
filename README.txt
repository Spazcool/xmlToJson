Seatmap Availability Exercise:

Write a python script that parses the example seatmap response (OTA_AirSeatMapRS.xml) and return a JSON object that lists the seats with the next properties:
	- Type (Seat, Kitchen, Bathroom, etc)
	- Seat id (17A, 18A)
	- Seat price
	- Cabin class
	- Availability

Please avoid the use of xml to json libraries/tools such as xmltodict, objectify and the like.

And any other properties you might find interesting or useful.

The output json format is not defined, so feel free to choose whatever you think best represents the information

Areas to improve:
* seatMap is defined relative to the root as opposed to being key based
* triple nested for loops (O*n^5) work fine with small data but, if this function were to be used outside of this context a more elegant solution would be required
* if an outside library we allowed, i suspect the above concerns would be addressed
