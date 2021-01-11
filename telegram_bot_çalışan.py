# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 18:18 2021
@author: Devran
"""
import requests
import time
import schedule
import datetime
from pandas_datareader import data as pdr
import yfinance as yf
from yahoo_fin import stock_info as si

APItoken = "1518192781:AAEWHkRHa5V1DvrcXQPKuMl4x6DdejslStU"
idno = "384343823"

def telegram_bot_sendtext(bot_message):
    bot_token= APItoken
    bot_chatID= idno
    send_text='https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response=requests.get(send_text)
    return response.json()
test=telegram_bot_sendtext("Selam Kızlar :)) \nBazı Fiyatları size göstermeye çalışacağım. \nBir süre bana ve sahibim Cihan'a katlanın lütfen :) ")
print(test)

fiyat1= si.get_live_price("ETH-USD")
print(fiyat1)

price=''

def anlıkFiat():
     bot_token= APItoken
     bot_chatID= idno
     response= "Let me fetch Latest quote ford you \n"
     symbol='XU100.IS'
     aapl= si.get_live_price(symbol)
     
     price= aapl
     price=str(price)
     price=" Anlık fiyatımız BORSA İSTANBUL "+ symbol + " için "+ price
     price=str(price.encode('utf-8','ignore'),errors='ignore')
     send_text='https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + price
     response=requests.get(send_text)
     print(response)

def anlıkFiat2():
     bot_token= APItoken
     bot_chatID= idno
     response= "Let me fetch Latest quote ford you \n"
     symbol='BTC-USD'
     aapl= si.get_live_price(symbol)
     
     price= aapl
     price=str(price)
     price=" Anlık fiyat Bitcoin "+symbol+ " için "+ price
     price=str(price.encode('utf-8','ignore'),errors='ignore')
     send_text='https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + price
     response=requests.get(send_text)
     print(response)



while True:
    anlıkFiat()
    anlıkFiat2()
    time.sleep(60)
