import requests
from bs4 import BeautifulSoup

url = "https://steamcommunity.com/market/listings/730/Fracture%20Case"
response = requests.get(url)
bs = BeautifulSoup(response.text, "lxml")
items = bs.findAll(id='searchResultsRows')
print("items", items)
