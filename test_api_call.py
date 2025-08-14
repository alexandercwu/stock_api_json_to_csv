import os
import requests
from datetime import datetime

API_KEY = os.environ["TWELVEDATA_API_KEY"]
STOCK_SYMBOL = 'AAPL'

url = f'https://api.twelvedata.com/quote?symbol={STOCK_SYMBOL}&apikey={API_KEY}'
response = requests.get(url)
data = response.json()

print('Using TwelveData API to retrieve stock information for the following stock symbols:')
print(data.keys())