import requests
import time 

ticker = "NDAQ"
api_key = "71959a3173904d4cb215fe33857b2665"

def get_stock_price(ticker_symbol,api):
    url=f"https://api.twelvedata.com/price?symbol={ticker}&apikey={api}"
    url2=f"https://api.twelvedata.com/quote?symbol={ticker}&apikey={api}"
    response =requests.get(url).json()
    price = response['price']
    response2 = requests.get(url2).json()
    low_price=response2['low']
    high_price=response2['high']
    if low_price>high_price:
        print("Dumbass lol ")



    print("$" + price + " per share for " + ticker_symbol)   
    print()



get_stock_price(ticker, api_key)   