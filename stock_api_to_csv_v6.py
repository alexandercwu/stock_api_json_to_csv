# 2025-08-14
# Create CSV of stock symbols prices from API call.
# https://twelvedata.com/docs#quickstart

import csv
from twelvedata import TDClient
import os
from datetime import datetime

# Replace with your actual Twelve Data API key
api_key = apikey=os.environ['TWELVEDATA_API_KEY']

# Initialize the client
td = TDClient(apikey=api_key)

# List of stock symbols (can be one or many)
symbols = ["AAPL", "NVDA", "MSFT"]
symbol_str = ",".join(symbols)

# Fetch batch quote data
quotes = td.quote(symbol=symbol_str).as_json()

# Normalize the response to always be a dictionary keyed by symbol
# If only one symbol is returned, wrap it to mimic the multi-symbol structure
if isinstance(quotes, dict) and "symbol" in quotes:
    # Single symbol case — wrap into a dict keyed by symbol name
    quotes = {quotes["symbol"]: quotes}

# Prepare list to hold rows
data_rows = []

# Process each symbol
for symbol in symbols:
    quote = quotes.get(symbol)

    if isinstance(quote, dict):
        symbol_val = quote.get("symbol")
        close_price = quote.get("close")
        timestamp = quote.get("timestamp") or quote.get("datetime")

        # Convert to ISO format if timestamp is valid - note we're putting it to local time but technically UTC is preferred.
        try:
            iso_timestamp = datetime.fromtimestamp(timestamp).isoformat()
        except Exception:
            iso_timestamp = "Invalid Timestamp"

        # Add row to data list
        data_rows.append([symbol_val, close_price, iso_timestamp])
    else:
        # Add row with error info if API didn't return expected data
        data_rows.append([symbol, "N/A", "N/A"])

# Write to CSV
csv_file = "stock_data.csv"

with open(csv_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    # Write header
    writer.writerow(["Symbol", "Close Price", "Timestamp (ISO 8601)"])
    # Write data rows
    writer.writerows(data_rows)

print(f"✅ Data saved to {csv_file}")
