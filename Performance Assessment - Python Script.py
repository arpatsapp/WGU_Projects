import bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from csv import writer

census_home = 'https://www.census.gov'

census_site = 'https://www.census.gov/programs-surveys/popest.html'

r = urlopen(census_site)

rhtml = r.read()

soup = BeautifulSoup(rhtml, 'html.parser')

link_html = soup.findAll('a', href=True)  # FIND ALL THE LINKS #

url_list = []

for link in link_html:
	if link['href'].startswith('#'):  # REMOVE LINKS REFERENCING THE CURRENT PAGE #
		pass
	elif link['href'].startswith('/'):  # MAKE RELATIVE LINKS ABSOLUTE #
		url_list.append(urljoin(census_home,link.get('href')))
	else: 								# ADD ALL LINK TYPES THAT ARE NOT REFERENCED ABOVE TO THE LIST #
		url_list.append(link['href'])

url_list_stripped = []

for url in url_list:  # FOR LOOP TO REMOVE TRAILING SYMBOLS FROM LINKS #
	url_list_stripped.append(url.rstrip('/'))		

url_no_dupes = set(url_list_stripped) # REMOVE DUPLICATE ITEMS FROM THE LIST BY CREATING A SET FROM THE LIST #	

final_url_list = list(url_no_dupes)	# MAKE THE SET BACK INTO A LIST #

with open('links.csv', 'w') as csv_file: #	WRITES THE LINKS TO A CSV FILE #
	csv_links = writer(csv_file, lineterminator='\n')
	for url in final_url_list:
		csv_links.writerow([url])