# 2025-08-09
# Create CSV of stock symbol price from API call.
# Version 1:
#   1. Create a free account with TwelveData.com and get API key.
#   2. Issue API call to get stock price.
#   3. Parse JSON response to CSV format and write file.

# This is just for proof of concept and simplicity. It's bad practice to hard
# code the API_KEY in the code and hard code the stock symbols instead of
# parameters.

import os
import requests
import csv
from datetime import datetime

API_KEY = os.environ["TWELVEDATA_API_KEY"]
STOCK_SYMBOL = 'AAPL'
CSV_FILE = 'stock_prices.csv'

def fetch_stock_price(symbol):
    url = f'https://api.twelvedata.com/quote?symbol={symbol}&apikey={API_KEY}'
    response = requests.get(url)
    data = response.json()

    print(data)
    if 'close' not in data:
        raise Exception(f"Error fetching stock data: {data.get('message', 'Unknown error')}")

    return {
        'symbol': data['symbol'],
        'close': data['close'],
        'timestamp': datetime.now().isoformat()
    }

def save_to_csv(row, filename):
    file_exists = False
    try:
        with open(filename, 'r'):
            file_exists = True
    except FileNotFoundError:
        pass

    with open(filename, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['symbol', 'close', 'timestamp'])

        if not file_exists:
            writer.writeheader()

        writer.writerow(row)

def main():
    stock_data = fetch_stock_price(STOCK_SYMBOL)
    save_to_csv(stock_data, CSV_FILE)
    print(f"Saved data: {stock_data}")

if __name__ == '__main__':
    main()