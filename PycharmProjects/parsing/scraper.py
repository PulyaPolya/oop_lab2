import requests
from bs4 import BeautifulSoup
def get_weather():
    url = 'https://www.unian.ua/pogoda/85486-kijiv'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    temperature = soup.find_all('div', class_='info-now__c')
    for elem in temperature:
        return elem.text
def get_how_it_feels():
    url = 'https://www.unian.ua/pogoda/85486-kijiv'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    temperature = soup.find_all('div', class_='hidden-xs')
    for elem in temperature:
        return elem.text
