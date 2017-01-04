import requests
from bs4 import BeautifulSoup


def crawler(max_pages):
    page = 1
    while page < max_pages:
        url = "https://ultimatenotes.herokuapp.com/semester"+str(page)+".html"
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        for link in soup.findAll('a', {'class': 'item-name'}):
            href = 'https://ultimatenotes.herokuapp.com/'+link.get('href')
            title = link.string
            print(href)
            print(title)
        page += 1


def crawler2(max_pages):
    page = 1
    while page < max_pages:
        url = "https://www.flipkart.com/"
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        title = soup.string
        print(title)
        page += 1

crawler2(5)

