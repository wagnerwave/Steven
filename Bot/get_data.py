from binance.client import Client
from datetime import datetime
import config
import csv

client = Client(config.API_KEY, config.API_SECRET_KEY)


def connection_test():
    status = client.get_system_status()
    if client.ping() == False:
        print("Error: ping client doesn't work.")
        exit(84)
    if status['status'] != 0:
        print("Error: System maintenance.")
        exit(84)
    print("#####################################")
    print("SERVER : Connection is okay and server status is", status['msg'])
    print("#####################################")


# prices = client.get_all_tickers()
# for price in prices:
#     print(price)
#candles = client.get_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_1MINUTE)
#for candlestick in candles:
#    print(candlestick)
#    candlestick_writer.writerow(candlestick)

connection_test()
print(client.get_exchange_info())