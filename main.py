from bs4 import BeautifulSoup

import requests

from collections import Counter

import json

response = requests.get("https://justbeerapp.com/guides/ca/bc/victoria/beers")

soup = BeautifulSoup(response.content, 'html.parser')

if response.status_code != 200:
    	print("Error fetching page")
else:
	content = response.content

nb_links = len(soup.find_all('a'))

print(f"There are {nb_links} links in this page")

pagespace = soup.find_all(id="section-beers-by-category")

#brewery = soup.find_all("span", attributes={"class":"pretitle"})

#name_of_beers = soup.find_all("h3") #works!!!
script = soup.find_all("script")

print(script)

from collections import Counter
all_hrefs = [a.get('href') for a in soup.find_all('a')]

#print(all_hrefs)







