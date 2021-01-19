#!/usr/bin/env python3

import websocket, json, pprint, numpy, talib

SOCKET = "wss://stream.binance.com:9443/ws/btcusdt@kline_1m"

RSI_PERIOD = 14
RSI_OVERBOUGHT = 70
RSI_OVERSOLD = 30
TRADE_SYMBOL = 'BTCUSD'
TRADE_QUATITY = 0.05

global in_position
closes = []

def on_open(ws):
    print('########### OPEN CONNECTION ###########')

def on_close(ws):
    print('########### CLOSE CONNECTION ###########')
 
def on_error(ws, error):
    print(error)

def on_message(ws, message):
    print('received message')
    json_message = json.loads(message)
    pprint.pprint(json_message)
    candle = json_message['k']
    candle_price_close = candle['c']
    close = candle['x']
    if close:
        print("candle closed at {}".format(candle_price_close))
        closes.append(float(candle_price_close))
        if len(closes) > RSI_PERIOD:
            np_closes = numpy.array(closes)
            rsi = talib.RSI(np_closes, RSI_PERIOD)
            last_rsi = rsi[-1]
            print("lenght of rsi -> ", len(rsi))
            print("rsi ->", rsi)
            print("the current rsi is {}".format(last_rsi))
            if last_rsi > RSI_OVERBOUGHT:
                if in_position:
                    print("STEVEN SAY : You need to sell, right now !")
                    in_position = False
                else:   
                    print("STEVEN SAY : It is overbought, you have already sell, Nothing to do.")
            if last_rsi < RSI_OVERSOLD:
                if in_position:
                    print("STEVEN SAY : It is oversold, you have already buy, Nothing to do.")
                else:
                    print("STEVEN SAY : You need to buy, right now !")
                    in_position = True

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
    ws.run_forever()
g