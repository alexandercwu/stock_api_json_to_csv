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

Here is the source code:
https://github.com/alexandercwu/stock_api_json_to_csv/blob/996ddfde4a694eee47faaec04cf47ccc431b5ad5/stock_api_to_csv_v1.py#L1-L6
