from bs4 import BeautifulSoup
import requests


url = 'https://www.ghanaweb.com/'

req = requests.get(url)
soup = BeautifulSoup(req.text,'html')
print(soup.prettify())


