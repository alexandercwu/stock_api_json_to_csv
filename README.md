# Pull stock data from API and save to CSV
Pull stock info from API, convert JSON payload to CSV.
2025-08-10

## General Summary
Create a program to pull stock data from an API and store in a CSV file. The payload from the API will be in JSON format.


## Setup API Environment
First you need to create an account with API access to pull stock data. You should **never hardcode your API key into your code nor should you push your key into the code repository**.
1. Create free account at [TwelveData](https://TwelveData.com).
2. Get the API key.
3. Store the API key as an environment variable. In macOS replace **YOUR_API_KEY** with the actual key and execute the following:
    `echo "export TWELVEDATA_API_KEY='YOUR_API_KEY'" >> ~/.zshrc`
4. Reload your shell so the new environment variable is loaded.
    `source ~/.zshrc`
5. Confirm the new environment variable **TWELVEDATA_API_KEY** is correct.
    `echo $TWELVEDATA_API_KEY`
6. In the python code, import the environment variable by adding these lines:
    ```python
    import os

    API_KEY = os.environ["TWELVEDATA_API_KEY"]
    ```

## Python Program
As an initial step, we'll create a python program that will do the following:
1. Call the TwelveData API for a single hardcoded stock "AAPL".
2. Display the JSON payload to console.
3. Write a subset of fields to a CSV with hardcoded name: **stock_prices.csv**.
4. Run the program with: `python stock_api_to_csv_v1.py`

Here is the source code:
[stock_api_to_csv_v1.py](https://github.com/alexandercwu/stock_api_json_to_csv/blob/731c71693a6783a7240ddc24a9773718337fd662/stock_api_to_csv_v1.py#L1C1-L19C30)

### Output
You should see an output called **stock_prices.csv** as well as console output:
```
usuari@MacBookPro stock_api_json_to_csv % python stock_api_to_csv_v1.py 
{'symbol': 'AAPL', 'name': 'Apple Inc.', 'exchange': 'NASDAQ', 'mic_code': 'XNGS', 'currency': 'USD', 'datetime': '2025-08-08', 'timestamp': 1754659800, 'last_quote_at': 1754659800, 'open': '220.83000', 'high': '231', 'low': '219.25', 'close': '229.35001', 'volume': '113696100', 'previous_close': '220.029999', 'change': '9.32001', 'percent_change': '4.23579', 'average_volume': '75158350', 'is_market_open': False, 'fifty_two_week': {'low': '169.21001', 'high': '260.10001', 'low_change': '60.14000', 'high_change': '-30.75000', 'low_change_percent': '35.54163', 'high_change_percent': '-11.82238', 'range': '169.210007 - 260.100006'}}
Saved data: {'symbol': 'AAPL', 'close': '229.35001', 'timestamp': '2025-08-10T19:46:08.814168'}
```

The formatted JSON console output would be:
```json
{'symbol': 'AAPL', 'name': 'Apple Inc.', 'exchange': 'NASDAQ', 'mic_code': 'XNGS', 'currency': 'USD', 'datetime': '2025-08-08', 'timestamp': 1754659800, 'last_quote_at': 1754659800, 'open': '220.83000', 'high': '231', 'low': '219.25', 'close': '229.35001', 'volume': '113696100', 'previous_close': '220.029999', 'change': '9.32001', 'percent_change': '4.23579', 'average_volume': '75158350', 'is_market_open': False, 'fifty_two_week': {'low': '169.21001', 'high': '260.10001', 'low_change': '60.14000', 'high_change': '-30.75000', 'low_change_percent': '35.54163', 'high_change_percent': '-11.82238', 'range': '169.210007 - 260.100006'}}
Saved data: {'symbol': 'AAPL', 'close': '229.35001', 'timestamp': '2025-08-10T19:46:08.814168'}
```

## Version 2
Let's expand the program to process a list of stock symbols instead of just one. Reading documentation for the TwelveData API, it seems you can just pass a comma-separated list in the API call.

Let's try changing this line:
```python
STOCK_SYMBOL = 'AAPL'
```

to this

```python
STOCK_SYMBOL = 'AAPL,NVDA'
```

### Ugh! Error! What happened?
```python
{'AAPL': {'symbol': 'AAPL', 'name': 'Apple Inc.', 'exchange': 'NASDAQ', 'mic_code': 'XNGS', 'currency': 'USD', 'datetime': '2025-08-11', 'timestamp': 1754919000, 'last_quote_at': 1754919000, 'open': '227.92000', 'high': '229.56000', 'low': '224.76241', 'close': '227.17999', 'volume': '60533346', 'previous_close': '229.35001', 'change': '-2.17001', 'percent_change': '-0.94615800', 'average_volume': '77425885', 'is_market_open': False, 'fifty_two_week': {'low': '169.21001', 'high': '260.10001', 'low_change': '57.96999', 'high_change': '-32.92001', 'low_change_percent': '34.25919', 'high_change_percent': '-12.65668', 'range': '169.210007 - 260.100006'}}, 'NVDA': {'symbol': 'NVDA', 'name': 'NVIDIA Corporation', 'exchange': 'NASDAQ', 'mic_code': 'XNGS', 'currency': 'USD', 'datetime': '2025-08-11', 'timestamp': 1754919000, 'last_quote_at': 1754919000, 'open': '182.16000', 'high': '183.84000', 'low': '180.25', 'close': '182.059998', 'volume': '137802961', 'previous_close': '182.70000', 'change': '-0.63999939', 'percent_change': '-0.35030071', 'average_volume': '160882566', 'is_market_open': False, 'fifty_two_week': {'low': '86.62000', 'high': '183.88000', 'low_change': '95.43999', 'high_change': '-1.82001', 'low_change_percent': '110.18240', 'high_change_percent': '-0.98977990', 'range': '86.620003 - 183.880005'}}}
Traceback (most recent call last):
  File "/Users/usuari/Documents/programming/stock_api_json_to_csv/stock_api_to_csv_v2.py", line 54, in <module>
    main()
    ~~~~^^
  File "/Users/usuari/Documents/programming/stock_api_json_to_csv/stock_api_to_csv_v2.py", line 49, in main
    stock_data = fetch_stock_price(STOCK_SYMBOL)
  File "/Users/usuari/Documents/programming/stock_api_json_to_csv/stock_api_to_csv_v2.py", line 24, in fetch_stock_price
    raise Exception(f"Error fetching stock data: {data.get('message', 'Unknown error')}")
Exception: Error fetching stock data: Unknown error
```
As we can see from the console, the returned payload is not as we expected before. Formerly it was a dictionary, now it's a nested dictionary.

Let's look at the keys.

```python
for ticker,detail in data.items():
    print(ticker)
```

And the output is:
```
AAPL
NVDA
````

Let's take a look at the detail entries:

```python
for ticker,detail in data.items():
    for field in detail:
        print(field + ':', detail[field])
    print('***********************')
```

We see the following output:

```
symbol: AAPL
name: Apple Inc.
exchange: NASDAQ
mic_code: XNGS
currency: USD
datetime: 2025-08-11
timestamp: 1754919000
last_quote_at: 1754919000
open: 227.92000
high: 229.56000
low: 224.76241
close: 227.17999
volume: 60533346
previous_close: 229.35001
change: -2.17001
percent_change: -0.94615800
average_volume: 77425885
is_market_open: False
fifty_two_week: {'low': '169.21001', 'high': '260.10001', 'low_change': '57.96999', 'high_change': '-32.92001', 'low_change_percent': '34.25919', 'high_change_percent': '-12.65668', 'range': '169.210007 - 260.100006'}
***********************
symbol: NVDA
name: NVIDIA Corporation
exchange: NASDAQ
mic_code: XNGS
currency: USD
datetime: 2025-08-11
timestamp: 1754919000
last_quote_at: 1754919000
open: 182.16000
high: 183.84000
low: 180.25
close: 182.059998
volume: 137802961
previous_close: 182.70000
change: -0.63999939
percent_change: -0.35030071
average_volume: 160882566
is_market_open: False
fifty_two_week: {'low': '86.62000', 'high': '183.88000', 'low_change': '95.43999', 'high_change': '-1.82001', 'low_change_percent': '110.18240', 'high_change_percent': '-0.98977990', 'range': '86.620003 - 183.880005'}
***********************
```

### Why is there an error?
Since the output to the console is fine, the issue seems to be when we write to the console. Indeed, the exception we check for is if the field 'close' exists in the payload and if not, error out.

```python
    if 'close' not in data:
        raise Exception(f"Error fetching stock data: {data.get('message', 'Unknown error')}")
```

We can update this exception handling code to loop through the nested dictionary and if any entry for a stock symbol is missing the field **close** then error out.

```python
for ticker,detail in data.items():
    if 'close' not in detail:
        raise Exception(f"Error fetching stock data: {data.get('message', 'Unknown error')}")
```

We also need to update what the function `fetch_stock_price()` returns since it will be multiple rows now. Also, update the CSV write section to use `writer.writerows(rows)` instead of `writer.writerow(row)`.

Now re-run the program and we see the expected output. The v2a file is the initial version 2 program with an error and the v2b file is the working version 2 program.