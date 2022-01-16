#Importing the library.
from urllib.request import urlopen

#assigning a site to a variable.
oakland_county = "https://www.oakgov.com/advantageoakland/resources/Documents/OaklandCounty_EconomicOutlookSummary_2021-2023.pdf"
#Opening the site.
read_url = urlopen(oakland_county)
#Reading each line on the site
for line in read_url:
    line = line.replace("b'3","")
    print(line)