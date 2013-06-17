Matching against VIAF
=====================

Introduction
------------
    

The script takes an input file containing data about people and uses VIAF's API in order to find possible matches with VIAF records.

It uses VIAF's OpenSearch (http://www.oclc.org/developer/documentation/virtual-international-authority-file-viaf/request-types) with local.personalNames as the cqlQuery parameter. If a possible match is found the script then parses the xml response, extracting VIAF heading and ID from the first result in the list.

Finally, it creates an output .tsv file with the results that can be then used for manual validation of the results.

Preparing the input file
------------------------        

The input file should have the .tsv extension and contain a single line for every individual we want to match against VIAF. The general syntax for a search string in the search file should be:

[Last Name], [First Name] [Birth Year]-[Death year][NEWLINE]

e.g.:

Bellings, John Arundell 1690-1729


Based on the completeness of the local data available, it is advisable to create different search files. We will call these: Group 1, Group 2 and Group 3.

- Group 1: Last Name, First Name, Birth Year, Death Year

e.g.:

Abeille, Louis Paul 1719-1807
Adanson, Michel 1727-1806
Adhémar, Antoine Honneste 1710-1785
Allamand, Jean Nicolas Sébastien 1713-1787
Amelot de Chaillou, Antoine Jean 1732-1795
Angiviller, Charles Claude 1730-1809
Ansse de Villoison, Jean Baptiste Gaspard 1750-1805
Argenson, Marc Pierre 1696-1764

- Group 2: Last Name, First Name and either Birth Year or Death Year (if one of the dates is missing)

e.g.:

La Maillardière, Charles François -1804
Jabineau de la Voute, Pierre 1721-
Nau, François 1715-
Sauseuil, Jean Nicolas 1731-
Abercromby, David -1701
Algarotti, conte Bonomo -1776

- Group 3: Last Name, Birth Year, Death Year (if the first name is missing but we know the birth and death years)

e.g.:

Brodrick 1702-1747
Brownlow 1726-1794
Dalrymple 1750-1830
Kiverley 1738-1789
Laide 1731-1759
Leeson 1770-1819
Lloyd 1730-1810
Macartney 1660-1730
Manby 1763-1844

Based on our experience, these three combinations provide the best results. However, any other combination is possible, provided every line in the input file is one individual.

Running the script
------------------      

Once the input files are ready, open the terminal, go to the directory where the script is and run:

python VIAFpeople.py

A dialog box will appear, making it possible to select the input file you want to run the script on. The script will be then executed and you will see the progress in the terminal. At the end of the execution, the script will provided a count of the possible matches found and will create the file with the results.

This file will be created in the same directory your input file is, and it will vae the same name of the input file with "VIAFmatch" the end.

For example, if the name of your input file is "group1.tsv", the file with the results will be "group1VIAFmatch.tsv".

The file with the results is made of these columns:

- Dataset: Blank. You should enter the name of your dataset when you inspect the results. e.g. "Electronic Enlightenment"

- Search String: The data taken from your input file
e.g. "Abarca y Bolea, Pedro Pablo, conde de Aranda 1718 -1798"

- VIAF Heading: The heading of the matching VIAF Record
e.g. "Aranda, Pedro Pablo Abarca de Bolea, Conde de 1719-1798"

- VIAF ID: The matching VIAF ID
e.g.: "32053659"

- VIAF URL: The URL for the VIAF match
e.g.: "http://www.viaf.org/32053659"

- Valid?: Blank. here you will enter your assessment of the validity of the match ("yes" or "no)

- Corrected VIAF ID: Blank. In case the match generated automatically was not valid, but you have found the correct VIAF record, please enter the ID here.

- Corrected VIAF URL: Blank. In case the match generated automatically was not valid, but you have found the correct VIAF record, you can enter the URL here. However, this is not strictly necessary, since URLs can be generated automatically at the end of the validation process using the corrected VIAF ID.

- Validator (initials): Blank. Please enter your initials. when validating a record.


