####################################################################################
#
# Script for matching individual names and birth/death dates with people contained
# in VIAF through VIAF's search web service.
#
# Author: Glauco Mantegari
# Project: Mapping the Republic of Letters, Stanford University
# License: MIT
#
####################################################################################

# -*- coding: utf-8 -*-

import urllib
import urllib2
from xml.dom import minidom
from Tkinter import Tk
from tkFileDialog import askopenfilename

# Show an "Open" dialog box and return the path to the selected input file
Tk().withdraw()
searchFile = askopenfilename(title='Please select the file with the data to be matched to VIAF')

# Set the parameters of the URL for VIAF's search web service.
baseUrl = "http://viaf.org/viaf/"
service = "search?query=local.personalNames+all+"
params = "+&maximumRecords=1&startRecord=1&sortKeys=holdingscount&httpAccept=text/xml"

# Open the people file
peopleFile = open(searchFile, 'r')
peopleEntry = peopleFile.readlines()

# Initialize the counters to be displayed in the terminal once the script finishes its execution
people = 0
match = 0
noMatch = 0

# Initialize the output
output = ""

# Open the output tsv file. If the file does not exist it will be created.
outputFileName = searchFile[:-4] + 'VIAFmatch.tsv'
print outputFileName
outputFile = open(outputFileName, 'w')

# Create the headings of the tsv file.
outputFile.write("Dataset\tSearch String\tVIAF Heading\tVIAF ID\tVIAF URL\tValid?\tCorrected VIAF ID\tCorrected VIAF URL\tValidator (Initials)\n")

# Try a match for every entry in the file.
# The script currently saves on the file the first heading and ID given by VIAF's web service if a match is found.
for line in peopleEntry:
	people += 1
	nameToSearch = line
	nameToSearchEncoded = urllib.quote(nameToSearch)
	url = baseUrl + service + nameToSearchEncoded + params
	xmldoc = minidom.parse(urllib2.urlopen(url))

	print "Working on: " + nameToSearch[:-1]

	# Retrieve VIAF IDs
	idList = xmldoc.getElementsByTagName('ns2:viafID')

	# Retrieve VIAF heading
	textList = xmldoc.getElementsByTagName('ns2:text') 
	
	if idList:
		output += "\t" + unicode(nameToSearch[:-1], 'utf-8') + "\t" + unicode(textList[0].firstChild.nodeValue) + "\t" + unicode(idList[0].firstChild.nodeValue) + "\thttp://viaf.org/" + unicode(idList[0].firstChild.nodeValue) + "\t\t\t" + "\n"
		match += 1
	else:
		output += "\t" + unicode(nameToSearch[:-1], 'utf-8') + "\tno headings found\tno ID found\t\t\t\t\t" + "\n"
		noMatch += 1

print "-------------------------------------"
print "Total people: " + str(people)
print "Possible matches found: " + str(match)
print "No matches found: " + str(noMatch)
print "-------------------------------------"

peopleFile.close()
outputFile.write(output.encode('UTF-8'))
outputFile.close()

