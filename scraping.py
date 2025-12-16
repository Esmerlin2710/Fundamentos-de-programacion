import requests
from bs4 import BeautifulSoup
import time

url = "https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all("div", class_="quote")
titulo = soup.find("div", class_="col-md-8").text
top_tags = soup.find_all("span", class_="tag-item")

print("Titulo:", titulo)

for q in quotes[1:6:3]:

    texto = q.find("span", class_="text").text.strip()
    autor = q.find("small", class_="author").text.strip()
    tags = q.find_all("a", class_="tag")

    
    print("Texto:", texto)
    print("Autor:", autor)

    for t in tags:
        print("Tag:", t.text)

    print("-" * 40)
    time.sleep(1)

for o in top_tags:
    print("Tags:", o.text)
    time.sleep(1)


