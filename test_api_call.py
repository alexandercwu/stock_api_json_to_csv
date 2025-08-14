import os
import requests
import json

API_KEY = os.environ["TWELVEDATA_API_KEY"]
STOCK_SYMBOL = 'AAPL,NVDA'

url = f'https://api.twelvedata.com/quote?symbol={STOCK_SYMBOL}&apikey={API_KEY}'
response = requests.get(url)
data = response.json()

print('Using TwelveData API to retrieve stock information for the following stock symbols:')
print(json.dumps(data,indent=4))
