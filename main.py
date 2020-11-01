from bs4 import BeautifulSoup

soup = BeautifulSoup(response.content, 'html.parser')

from selenium import webdriver

from urllib.request import urlopen

url = "https://justbeerapp.com/guides/ca/bc/victoria/beers"

page = urlopen(url)

html_bytes = page.read()

html = html_bytes.decode("utf-8")

print(html)
