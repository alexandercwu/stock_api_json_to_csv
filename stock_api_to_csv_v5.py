# 2025-08-14
# Create CSV of stock symbols prices from API call.
# https://twelvedata.com/docs#quickstart

# Let's try this again but reading the TwelveData API documentation first.
# This one only displays to console.

# Expected output in the format:
# Symbol: AAPL
# Close Price: 232.78000
# Timestamp: 1755178200
# ------------------------------
# Symbol: NVDA
# Close Price: 182.02000
# Timestamp: 1755178200
# ------------------------------
# Symbol: MSFT
# Close Price: 522.47998
# Timestamp: 1755178200
# ------------------------------

import os
from twelvedata import TDClient

# Replace with your actual Twelve Data API key
api_key = apikey=os.environ['TWELVEDATA_API_KEY']

# Initialize the client
td = TDClient(apikey=api_key)

# List of stock symbols (can be one or many)
symbols = ["AAPL"]  # Try changing this to ["AAPL", "NVDA", "MSFT"]
symbol_str = ",".join(symbols)

# Get batch quote
quotes = td.quote(symbol=symbol_str).as_json()

# Debug print to inspect the structure (optional)
# import json
# print(json.dumps(quotes, indent=2))

# Normalize the response to always be a dictionary keyed by symbol
# If only one symbol is returned, wrap it to mimic the multi-symbol structure
if isinstance(quotes, dict) and "symbol" in quotes:
    # Single symbol case — wrap into a dict keyed by symbol name
    quotes = {quotes["symbol"]: quotes}

# Safely handle the response
for symbol in symbols:
    quote = quotes.get(symbol)

    # Ensure we got a valid dictionary for each symbol
    if isinstance(quote, dict):
        symbol_val = quote.get("symbol")
        close_price = quote.get("close")
        timestamp = quote.get("timestamp") or quote.get("datetime")

        print(f"Symbol: {symbol_val}")
        print(f"Close Price: {close_price}")
        print(f"Timestamp: {timestamp}")
        print("-" * 30)
    else:
        print(f"⚠️ Could not retrieve data for {symbol}. Response: {quote}")
        print("-" * 30)

