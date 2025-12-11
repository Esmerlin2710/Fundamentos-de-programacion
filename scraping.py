import requests
from bs4 import BeautifulSoup
import time

url = "https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all("div", class_="quote")

for q in quotes:
    texto = q.find("span", class_="text").text.strip()
    autor = q.find("small", class_="author").text.strip()
    tags = q.find_all("a", class_="tag")

    print("Texto:", texto)
    print("Autor:", autor)

    for t in tags:
        print("Tag:", t.text)

    print("-" * 40)
    time.sleep(1)


