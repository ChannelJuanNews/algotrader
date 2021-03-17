import alpaca_trade_api as tradeapi
import application
import os

api_key = os.environ.get('ALPACA_API_KEY_ID')
api_secret = os.environ.get('ALPACA_API_SECRET')
api_version = 'v2'
api_base_url = "https://paper-api.alpaca.markets"

api = tradeapi.REST(api_key, api_secret,
                    api_version=api_version, base_url=api_base_url)
