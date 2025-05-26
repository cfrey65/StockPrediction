import requests
from bs4 import BeautifulSoup

"""
This function takes in a list of stock tags.
It will then search through the finviz website to find the current prices of those stocks.
"""

def scrape(stocks):
    for stock in stocks:
        url = "https://finviz.com/quote.ashx?t=" + stock +"&p=d"
        response = requests.get(url, headers = {'User-Agent':'Mozilla/5.0'})
        if (response.status_code == 200):
            soup = BeautifulSoup(response.text, 'html.parser')
            price = soup.find('strong', {'class': "quote-price_wrapper_price"})
            print(price.text)

if __name__ == '__main__':
    scrape(["NVDA", "BA"])