# 2025-08-11
# Create CSV of stock symbols prices from API call.
# Version 2:
#   1. Create a free account with TwelveData.com and get API key.
#   2. Issue API call to get stock price from multiple stock symbols.
#   3. Parse JSON response to CSV format and write file.

import os
import requests
import csv
from datetime import datetime

API_KEY = os.environ['TWELVEDATA_API_KEY']
STOCK_SYMBOL = 'AAPL'
CSV_FILE = 'stock_prices2.csv'

def fetch_stock_price(symbol):
    url = f'https://api.twelvedata.com/quote?symbol={symbol}&apikey={API_KEY}'
    response = requests.get(url)
    data = response.json()

    for ticker,detail in data.items():
        if 'close' not in detail:
            raise Exception(f"Error fetching stock data: {data.get('message', 'Unknown error')}")

    # Prepare the data rows by flattening the JSON structure.
    # Only select fields symbol, close, timestamp, discarding rest.
    rows = []
    for symbol, detail in data.items():
        row = {
            'symbol': detail['symbol'],
            'close': detail['close'],
            'timestamp': datetime.fromtimestamp(detail['timestamp']).isoformat()
        }
        rows.append(row)
        print(row)

    return rows

def save_to_csv(rows, filename):
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

        writer.writerows(rows)

def main():
    stock_data = fetch_stock_price(STOCK_SYMBOL)
    save_to_csv(stock_data, CSV_FILE)
    print(f"Saved data: {stock_data}")

if __name__ == '__main__':
    main()