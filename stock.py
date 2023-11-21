import requests
import time 
import smtplib
import ssl 
#Email sender 
smtp_port= 587
smtp_server = "smtp.gmail.com"

#To and from emails
email_from= "ecueva003@gmail.com"
email_to= "ecueva003@gmail.com"

pw=""
        
simple_email_context = ssl.create_default_context()
#Stock tracker 

#Choosing the specific stock using the 3-4 letters
ticker = input(f"Choose a stock to follow: ")
msg= f"Check the stock{ticker}"
api_key = "71959a3173904d4cb215fe33857b2665"


#Basic information about the stock
def get_stock_price(ticker_symbol,api):
    url=f"https://api.twelvedata.com/price?symbol={ticker}&apikey={api}"
    url2=f"https://api.twelvedata.com/quote?symbol={ticker}&apikey={api}"
    response =requests.get(url).json()
    price = response['price']
    print("$" + price + " per share for " + ticker_symbol)
get_stock_price(ticker, api_key)
def get_stock_price(ticker_symbol,api):
    url2=f"https://api.twelvedata.com/quote?symbol={ticker}&apikey={api}"    
    response2 = requests.get(url2).json()
    low_price=response2['low']
    high_price=response2['high']
    open_price = response2['open']
    close_price=response2['close']
         
    if open_price != close_price: 
        try:
            TIE_server = smtplib.SMTP(smtp_server, smtp_port)
            TIE_server.starttls(context=simple_email_context)
            TIE_server.login(email_from, pw)
     
            print (f"Sending email to {email_to}")
            TIE_server.sendmail(email_from, email_to, msg)
            print(f"Sent email to {email_to}:")

        except Exception as e:
            print(f"Dumbass failed lmao{e}")

        finally:
            TIE_server.quit()
