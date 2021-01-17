#!/usr/bin/env python3

import websocket, json, pprint, numpy, talib

SOCKET = "wss://stream.binance.com:9443/ws/btcusdt@kline_1m"

RSI_PERIOD = 14
RSI_OVERBOUGHT = 70
RSI_OVERSOLD = 30
TRADE_SYMBOL = 'BTCUSD'
TRADE_QUATITY = 0.05

closes = []

def on_open(ws):
    print('########### OPEN CONNECTION ###########')

def on_close(ws):
    print('########### CLOSE CONNECTION ###########')
 
def on_error(ws, error):
    print(error)

def on_message(ws, message):
    in_position = False
    print('received message')
    json_message = json.loads(message)
    pprint.pprint(json_message)

    candle = json_message['k']
    
    is_close_candle = candle['c']
    close = candle['x']
    if is_close_candle:
        print("candle closed at {}".format(close))
        closes.append(float(close))
        if len(closes) > RSI_PERIOD:
            np_closes = numpy.array(closes)
            rsi = talib.RSI(np_closes, RSI_PERIOD)
            # print("all rsis calculated so far")
            # print(rsi)
            last_rsi = rsi[-1]
            print("the current rsi is {}".format(last_rsi))
            if last_rsi > RSI_OVERBOUGHT:
                if in_position:
                    print("STEVEN SAY : You need to sell, right now !")
                    in_position = False
                else:   
                    print("STEVEN SAY : Nothing to do.")
            if last_rsi < RSI_OVERSOLD:
                if in_position:
                    print("STEVEN SAY : Nothing to do.")
                else:
                    print("STEVEN SAY : You need to buy, right now !")
                    in_position = True


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
    ws.run_forever()
