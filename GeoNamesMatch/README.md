# Matching toponyms against GeoNames


## Introduction
    

The script takes an input file containing toponyms and uses the GeoNames search webservice (http://www.geonames.org/export/geonames-search.html) to find possible matches with GeoNames records.

The following parameters are passed to the webservice:
- name_equals: the toponym
- featureClass: P (Populated Place Features: http://www.geonames.org/export/codes.html)
- country: the ISO-3166 country code associated to the place name
- maxRows: 10

If a possible match is found the script then parses the xml response, extracting from GeoNames the toponym and the ID.

Finally, it creates an output .tsv file that can be then used for manual validation of the results.

## Preparing the input file

The input file should be a .tsv containing a single line for every place name we want to match against GeoNames. The syntax for a search string in the search file should be:

`[Place Name][TAB][IS-3166 Country Code][NEWLINE]`

_e.g._:

> Abbeville	FR
> Aberdeen	UK
> Agenvillers	FR
> Aire	CH
> Aix-en-Provence	FR
> Alassio	IT
> Almaty	KZ

IS0-3166 Country codes can be found at: http://www.iso.org/iso/home/standards/country_codes/country_names_and_code_elements.htm

The use of this codes significantly helps disambiguating the same toponyms in different Countries and narrow down the result set.

## Running the script

In order to use the script, a personal and free account on GeoNames should be created first, registering at http://www.geonames.org/login

This makes it possible to have 30,000 credits a day with an hourly limit of 2000 credits. A credit is a web service request hit for most services. In other words it means that the script can be used by a registered user to match up to 30,000/day - 2,000/hour toponyms against GeoNames.

Once the registration is complete, the username has been created, and the input .tsv file with the toponyms and country codes is ready, go to the directory where the script is and run:

`python geonamesmatch.py`

Enter your username in the console and hit return. A dialog box will appear, making it possible to select your input file. The script will be then executed and you will see the progress in the terminal. At the end of the execution, the script will provide counts of the possible matches found and it will create the file with the results.

This file will be created in the same directory your input file is, and it will have the same name of the input file with "GeoNamesMatch" at the end. For example, if the name of your input file is "toponyms.tsv", the file with the results will be "toponymsGeoNamesMatch.tsv".

The file with the results has the following columns:

**Search Toponym**: The toponym from your input file
e.g. "Abbeville"

**Search Country**: The ISO-3166 Country code from your input file
e.g. "FR"

**GeoNames Toponym**: The matching GeoNames toponym
e.g.: "Abbéville-la-Rivière"

**GeoNames ID**: The GeoNames ID associated with the toponym
e.g.: "3038786"

**GeoNames Feature Code**: The GeoNames feature code within the class P associated with the toponym (for a list, see: http://www.geonames.org/export/codes.html)
e.g.: "PPL"

**GeoNames URL**: The webpage where the toponym can be checked:
e.g. "http://www.geonames.org/3038786"

**GeoNames Latitude**: The latitude of the place:
e.g. "48.34683"

**GeoNames Longitude**: The longitude of the toponym:
e.g. "2.16594"

**Valid?**: Blank. Here you will enter your assessment of the validity of the match ("yes" or "no)

**Corrected GeoNames ID**: Blank. In case the match generated automatically is not valid, but you have found the correct GeoNames record, please enter the ID here.

**Corrected GeoNames URL**: Blank. In case the match generated automatically is not valid, but you have found the correct GeoNames record, you can enter the URL here. This is not strictly necessary, since URLs can be generated automatically at the end of the validation process using the corrected GeoNames ID.

**Validator (initials)**: Blank. Please enter your initials. when validating a record.