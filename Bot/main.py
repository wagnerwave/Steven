#!/usr/bin/env python3

from binance.client import Client
from binance.enums import *
from rsi import RSI_strat
from bollinger import bollinger_strat
from config import API_KEY, API_SECRET_KEY

import websocket, json, pprint, numpy, talib, math
import datetime

SOCKET = "wss://stream.binance.com:9443/ws/ethusdt@kline_1m"

client = Client(API_KEY, API_SECRET_KEY, tld='us')

RSI_PERIOD = 14
RSI_OVERBOUGHT = 65
RSI_OVERSOLD = 40
TRADE_SYMBOL = 'ETHUSD'
TRADE_QUATITY = 0.001

closes = []
in_position = False

#################################################################

def buy_crypto(symbol, quatity):
    try:
        order = client.create_order(symbol=symbol, side=SIDE_BUY, type=ORDER_TYPE_MARKET, quatity=quatity)
        print("Order complete: {}".format(order))
    except Exception as e:
        print("Error to buy: {}".format(e))
        return False
    return True

def sell_crypto(symbol, quatity):
    try:
        order = client.create_order(symbol=symbol, side=SIDE_SELL, type=ORDER_TYPE_MARKET, quatity=quatity)
        print("Order complete: {}".format(order))
    except Exception as e:
        print("Error to sell: {}".format(e))
        return False
    return True

def choice(ret_value_rsi, ret_value_bollinger):
    global in_position
    total = ret_value_bollinger + ret_value_rsi
    if (total != 0):
        if (total == 1):
                print("STEVEN SAY : nothing to do")
        if (total > 1):
            if in_position == False:
                print("STEVEN SAY : I'm gonna buy", TRADE_SYMBOL, " for ", TRADE_QUATITY," quantities!")
                buy_success = buy_crypto(TRADE_SYMBOL, TRADE_QUATITY)
                if (buy_success):
                    in_position = True
                else:
                    in_position = False
                    print("BIG ERROR: cannot buy !!!!")
                    exit(84) 
            else:
                print("STEVEN SAY : nothing to do")
        if (total < 0):
            if in_position == True:
                print("STEVEN SAY : I'm gonna sell", TRADE_SYMBOL, " for ", TRADE_QUATITY," quantities!")
                sell_success = sell_crypto(TRADE_SYMBOL, TRADE_QUATITY)
                if (sell_success):
                    in_position = False
                else:
                    in_position = True
                    print("BIG ERROR: cannot sell !!!!")
                    exit(84) 
            else:
                print("STEVEN SAY : nothing to do")
    else:
        print("STEVEN SAY : nothing to do")


################################################################

def on_open(ws):
    print('########### OPEN CONNECTION ###########')

def on_close(ws):
    print('########### CLOSE CONNECTION ###########')
 
def on_error(ws, error):
    print(error)

def on_message(ws, message):
    global in_position
    #print('received message')
    json_message = json.loads(message)
    #pprint.pprint(json_message)
    candle = json_message['k']
    candle_price_close = candle['c']
    close = candle['x']
    if close:
        print("candle closed at {}".format(candle_price_close))
        closes.append(float(candle_price_close))
        print(len(closes))
        if len(closes) > RSI_PERIOD:
            np_closes = numpy.array(closes)
            rsi = talib.RSI(np_closes, RSI_PERIOD)
            print("##################")            
            print(rsi)
            last_rsi = rsi[-1]
            print("the current rsi is {}".format(last_rsi))
            ret_value_rsi = RSI_strat(last_rsi, in_position)
            ret_value_bollinger = bollinger_strat(closes, len(closes))
            print("##################")
            print("deja achete {}".format(in_position))
            print("ret_value_rsi ->", ret_value_rsi)
            print("ret_value_bollinger ->", ret_value_bollinger)
            print("##################")
            print(str(datetime.datetime.now()))
            choice(ret_value_rsi ,ret_value_bollinger)
            print("##################")

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
    ws.run_forever()