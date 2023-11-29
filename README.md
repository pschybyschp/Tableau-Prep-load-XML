# Tableau-Prep-load-XML
Currently Tableau Prep doesnt offer the option to load XML data. 
With the following script you can load XML data from a file located on your desktop.
Prerequisite:
- TabPy server is installed
- Analytics Extension in Tableau is configurated properly

1) Please place the XML-file on your desktop. 
I have used following path: /Users/XYZ/Desktop/pegelstaende_neu.xml
The XML file was extracted from following website: https://www.pegelonline.wsv.de/svgz/pegelstaende_neu.xml

2) Please place the python script 'readxml_pegel.py' file also on your desktop.

3) Open Tableau Prep and connect to the dummy excel file as first step.
4) Add as second step the Script step and select the python script on your desktop and finally run the function 'Get_XML_Data'

The data types of the output table are all set to string but can be adjusted to boolean, number etc.
