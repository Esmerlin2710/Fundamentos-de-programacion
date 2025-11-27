import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

titulo = soup.find_all("div", class_="tags")


for i in titulo:
    print(i.text)
    
