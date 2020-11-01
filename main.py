from bs4 import BeautifulSoup

import requests

response = requests.get("https://justbeerapp.com/guides/ca/bc/victoria/beers")

soup = BeautifulSoup(response.content, 'html.parser')

print(soup.get_text())


