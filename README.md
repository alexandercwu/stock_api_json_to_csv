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