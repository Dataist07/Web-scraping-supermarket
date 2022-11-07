from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.auchan.fr/').text.encode("utf-8")
acceuil = BeautifulSoup(html_text,'lxml')
print(acceuil)