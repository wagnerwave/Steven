#!/usr/bin/env python3

import websocket, json
import pprint

SOCKET = "wss://stream.binance.com:9443/ws/btcusdt@trade"

def on_open(ws):
    print('########### OPEN CONNECTION ###########')

def on_close(ws):
    print('########### CLOSE CONNECTION ###########')
 
def on_error(ws, error):
    print(error)

def on_message(ws, message):
    print('received message:', message)
    json_message = json.loads(message)
    pprint.pprint(json_message)

    # candle = json_message['k']
    
    # is_close_candle = candle['c']
    # close = candle['x']
    # if is_close_candle:
    #     print("candle closed at {}".format(close))
    #     closes.append(float(close))
    #     print("closes")
    #     print(closes)


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
    ws.run_forever()
