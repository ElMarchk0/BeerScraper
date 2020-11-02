from bs4 import BeautifulSoup

import requests

from collections import Counter


response = requests.get("https://justbeerapp.com/guides/ca/bc/victoria/beers")

soup = BeautifulSoup(response.content, 'html.parser')

if response.status_code != 200:
    	print("Error fetching page")
else:
	content = response.content

nb_links = len(soup.find_all('a'))

print(f"There are {nb_links} links in this page")

print(soup.get_text())



print(soup.title)


