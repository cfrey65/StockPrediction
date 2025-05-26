import alpaca_trade_api as tradeapi
import alpaca
import requests

ak = "PKD2OQF1B2K8JJEZZUGT"
sk = "spXoTzlk0fHQSGWJZetxAltiX405eZM8a41qpLC0"

base_url = 'https://paper-api.alpaca.markets'

# instantiate REST API
api = tradeapi.REST(ak, sk, base_url, api_version='v2')

# obtain account information
account = api.get_account()
print(account)