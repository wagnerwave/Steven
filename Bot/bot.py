#!/usr/bin/env python3

import websocket, json, pprint, numpy, talib, math

SOCKET = "wss://stream.binance.com:9443/ws/btcusdt@kline_1m"

RSI_PERIOD = 14
RSI_OVERBOUGHT = 70
RSI_OVERSOLD = 30
TRADE_SYMBOL = 'BTCUSD'
TRADE_QUATITY = 0.05

in_position = False
closes = []

###################################################################

def RSI_strat(last_rsi):
    if last_rsi > RSI_OVERBOUGHT:
        if in_position:
            print(in_position)
            return -1
        else:   
            return 0
    if last_rsi < RSI_OVERSOLD:
        if in_position:
            return 0
        else:
            return 1
    return 0

def sma(closes_candles, n):
    res = 0
    for x in closes_candles:
        if x == numpy.nan:
            continue
        else:
            res += x
    return (res / n)

def standardDeviation(candles, n):
    deviation = 0.0
    average = sma(candles, n)
    for x in candles:
        if x == numpy.nan:
            continue
        else:
            deviation += pow(x - average, 2)
    return math.sqrt(deviation / n)

def bollinger_strat(candles, n):
    n = n - 1
    print("####################################")
    print("sma")
    x = sma(candles[-n:], n)
    print(x)
    print("std_dev")
    std_dev = standardDeviation(candles[-n:], n)
    print(std_dev)
    print("####################################")
    A1 = x + std_dev * 2
    B1 = x + std_dev
    B2 = x - std_dev
    A2 = x - std_dev * 2
    close = candles[-1]
    if (close >= B1 and close <= A1):
        return 1
    elif (close < B2 and close >= A2):
        return -1
    else:
        return 0

#################################################################

def choice(ret_value_rsi, ret_value_bollinger):
    total = ret_value_bollinger + ret_value_rsi
    if (total < 1):
        in_position = True
        print("STEVEN SAY : You need to buy, right now !")
    if (total > 0):
        print("STEVEN SAY : You need to sell, right now !")
        in_position = False
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
            print(rsi)
            last_rsi = rsi[-1]
            print("the current rsi is {}".format(last_rsi))
            ret_value_rsi = RSI_strat(last_rsi)
            ret_value_bollinger = bollinger_strat(closes, len(closes))
            print("##################")
            print("deja achete {}".format(in_position))
            print("ret_value_rsi ->", ret_value_rsi)
            print("ret_value_bollinger ->", ret_value_bollinger)
            print("##################")

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
    ws.run_forever()