import requests
from bs4 import BeautifulSoup
'''
url = 'https://rp5.ua/%D0%9F%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0_%D0%B2_%D0%9A%D0%B8%D1%94%D0%B2%D1%96'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
items = soup.find_all('div', class_="t_0")
#quotes = soup.find_all('span', class_='text')
for item in items:
    print(item.text)
'''

url = 'https://meteo.gov.ua/ua/33345'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

#quotes = soup.find_all('span', class_='text')
print(soup)