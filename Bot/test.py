#!/usr/bin/env python3

from config import API_KEY, API_SECRET_KEY
from binance.client import Client
from binance.websockets import BinanceSocketManager
from binance.enums import *

def process_message(msg):
    print("message type: {}".format(msg['e']))
    print(msg)

if __name__ == "__main__":
    client = Client(API_KEY, API_SECRET_KEY)
    socket = BinanceSocketManager(client)
    socket.start_kline_socket('BNBBTC', process_message)
    socket.start()