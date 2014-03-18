####################################################################################
#
# Script for matching toponyms against GeoNames through geoNames search web service
#
# Author: Glauco Mantegari
# Project: Mapping the Republic of Letters, Stanford University
# License: MIT
#
####################################################################################

# -*- coding: utf-8 -*-

import sys
import urllib
import urllib2
from xml.dom import minidom
from Tkinter import Tk
from tkFileDialog import askopenfilename

# Enter the GeoNames username
username = raw_input('Enter your username on GeoNames: ')
if username == "":
	print "---------------------------------------------------------------------------------------------------------------"
	print "You need to have an username on GeoNames in order to run this script"
	print "Please register at: http://www.geonames.org/login and then run the script again, specifying your username"
	print "---------------------------------------------------------------------------------------------------------------"	
	sys.exit(0)

# Build the url to call the GeoNames search web service.
baseUrl = " http://api.geonames.org/"
service = "search?name_equals="
featureClass = "&featureClass=P"
country = "&country="
params = "&maxRows=10&username="

# Open the file with place names.
Tk().withdraw()
searchFile = askopenfilename(title='Please select the file with the data to be matched to GeoNames')

# The file should contain a line specyfying a search string for every place name, in the form:
# Place name [tab] Country code
# The country code has to be compliant with the ISO 3166 specification
placesFile = open(searchFile, 'r')
placesEntry = placesFile.readlines()

# Initialize the counters to be displayed in the terminal once the script finishes its execution
places = 0
singleMatch = 0
multipleMatch = 0
noMatch = 0

# Initialize the output
output = ""
outputFileName = searchFile[:-4] + 'GeoNamesMatch.tsv'
outputFile = open(outputFileName, 'w')

# Create the headings of the tsv file.
outputFile.write("Search Toponym\tSearch Country\tGeoNames Toponym\tGeoNames ID\tGeoNames Feature Code\tGeoNames URL\tGeoNames Latitude\tGeoNames Longitude\tGeoNames Coordinates\tValid?\tCorrected GeoNamesID\tCorrected GeoNames URL\tValidator (Initials)\n")

#Try a match for every entry in the file
for line in placesEntry:
	places += 1
	placeParams = line.partition("\t")
	cityName = placeParams[0]
	countryCode = placeParams[2][:-1]
	cityNameEncoded = urllib.quote(cityName)

	url = baseUrl + service + cityNameEncoded + featureClass + country + countryCode + params + username
	
	xmldoc = minidom.parse(urllib2.urlopen(url))

	#Retrieve Geonames Toponym Name
 	toponymList = xmldoc.getElementsByTagName('toponymName')
	#Retrieve Geonames Latitude
	latList = xmldoc.getElementsByTagName('lat')
	#Retrieve Geonames Longitude
	lonList = xmldoc.getElementsByTagName('lng') 	
	#Retrieve Geonames ID
	idList = xmldoc.getElementsByTagName('geonameId') 	
 	#Retrieve Geonames Feature Code
	codeList = xmldoc.getElementsByTagName('fcode')  		  	

	searchToponym = unicode(cityName, 'utf-8')
 	
 	if toponymList:
 		toponymCount = 0
		print ""
 		print "###### " + searchToponym + " (" + countryCode + ")"
 		for toponym in toponymList:
 			toponymCount += 1
 			toponymFound = unicode(toponymList[toponymCount - 1].firstChild.nodeValue)
 			latFound = unicode(latList[toponymCount - 1].firstChild.nodeValue)
 			lonFound = unicode(lonList[toponymCount - 1].firstChild.nodeValue)
 			coordinatesFound = latFound + "," + lonFound
 			codeFound = unicode(codeList[toponymCount - 1].firstChild.nodeValue)
	 		IDfound = unicode(idList[toponymCount - 1].firstChild.nodeValue)
 			URLfound = "http://www.geonames.org/" + IDfound
 				
			print "Found: " + toponymFound
 			output += searchToponym + "\t" + countryCode + "\t" + toponymFound + "\t" + IDfound + "\t" + codeFound + "\t" + URLfound + "\t" + latFound + "\t" + lonFound + "\t" + coordinatesFound + "\t\t\t\t\n"

 		if toponymCount > 1:
 			multipleMatch +=1
 		else:
 			singleMatch += 1
  	else:
		print ""
 		print "###### " + searchToponym + " (" + countryCode + ")"
 		print "Not found"
 		
 		output += searchToponym + "\t" + countryCode + "\tnothing found\tnothing found\tnothing found\tnothing found\tnothing found\tnothing found\t\t\t\t\n"
 		
 		noMatch += 1

print "" 		
print "-------------------------------------"
print "Total places searched: " + str(places)
print "Places with single match: " + str(singleMatch)
print "Places with multiple matches: " + str(multipleMatch)
print "No matches found: " + str(noMatch)
print "-------------------------------------"
print ""
print "The file with the results has been created at:"
print outputFileName
print ""

placesFile.close()
outputFile.write(output.encode('UTF-8'))
outputFile.close()