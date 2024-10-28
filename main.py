from keys import api, secret
import pandas as pd
from time import sleep
from binance.error import ClientError
from binance.spot import Spot

spot = Spot()

# basic data from client
print(spot.klines('BTCUSDT', '1m', limit=1))

# user data
client = Spot(api_key = api, api_secret=secret)

try :
    account = client.account()
    print(account)
    for elem in account:
        if elem['asset'] == 'USDT':
            print("balance", elem["balance"])
except ClientError as error:
    print(
        "Found error. Status: {}, error code: {}, error message: {}".format(error.status_code, error.error_code, error.error_message)
    )