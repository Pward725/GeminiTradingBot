# Docs: https://docs.gemini.com/rest-api/v2
import json, requests
import pandas as pd

def run():
    base_url = "https://api.sandbox.gemini.com"
    response = requests.get(base_url + "/symbols")
    symbols = pd.DataFrame(response.json())
    symbols.tail()

    response = requests.get(base_url + "/ticker/btcusd")
    btc_data = response.json()
    #get some price data
    #plug that into model
     
if __name__ == "__main__":
    run()