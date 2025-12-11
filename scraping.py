import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

quote = soup.find_all("div", class_="quote")


for q in quote:
    print(q.text)

