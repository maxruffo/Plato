"""
@author: Max Ruffo
@version: Beta 0.0
@description: Scrapes information about a publicly traded company given its ticker symbol. Returns a Pandas DataFrame containing information such as
company name, sector, market cap, P/E ratio, dividend yield, etc
"""

import yfinance as yf
import json
import os
import pandas as pd

global ticker
ticker = ""



class data_scraper():

    def __init__(self,_ticker_):
        self.ticker = _ticker_

    def get_ticker_obj(self):
        stock = yf.Ticker(self.ticker)
        self.stock = stock
        return stock

    
    def save_json(self):
        # Ordner erstellen, falls er nicht vorhanden ist
        if not os.path.exists("data"):
            os.makedirs("data")

# Datei im JSON-Format speichern
        with open("data/stock_info.json", "w") as file:
            json.dump(self.stock.info, file)


    def get_quarterly_financials_yahoo(self):
        # Abrufen der Quartalszahlen von Yahoo Finance
    
        quarterly_financials = self.stock.quarterly_financials

        # Umwandeln der Daten in ein DataFrame
        df = pd.DataFrame(quarterly_financials)

        # Sortieren der Daten nach Datum
        df['date'] = pd.to_datetime(df['endDate'])
        df = df.sort_values(by='date', ascending=False)

        # Rückgabe der letzten vier Quartalszahlen
        return df.head(4)


scraper = data_scraper("AAPL")
stock = scraper.get_ticker_obj()
scraper.save_json()
a=scraper.get_quarterly_financials_yahoo()
print(a)

print(type(stock.info))