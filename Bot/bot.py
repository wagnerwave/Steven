from binance.client import Client
from binance.enums import *
from getSocket import * 
from log import log
from rsi import RSI_strat, RSI_OVERBOUGHT, RSI_OVERSOLD
from bollinger import bollinger_strat
from config import API_KEY, API_SECRET_KEY

import websocket, json, pprint, numpy, talib, math
import datetime

class Bot:
    def __init__(self, period, symbol, quatity):
        self._tradeSymbol = symbol
        self._tradeQuatity = quatity
        self._period = period
        self._position = False
        self._client = Client(API_KEY, API_SECRET_KEY, tld='us')
        self._closes = []
        self._rsiPeriod = 14
        self._socket = getSocket(self._period, self._tradeSymbol)

    def __buy(self):
        try:
            order = client.create_order(symbol=self._tradeSymbol, side=SIDE_BUY, type=ORDER_TYPE_MARKET, quatity=self._tradeQuatity)
            print("Order complete: {}".format(order))
        except Exception as e:
            print("Error to buy: {}".format(e))
            return False
        return True

    def __sell(self):
        try:
            order = client.create_order(symbol=self._tradeSymbol, side=SIDE_SELL, type=ORDER_TYPE_MARKET, quatity=self._tradeQuatity)
            print("Order complete: {}".format(order))
        except Exception as e:
            print("Error to sell: {}".format(e))
            return False
        return True

    def _strategie_rsi_bollinger(self, ret_value_rsi, ret_value_bollinger):
        total = ret_value_bollinger + ret_value_rsi
        if (total != 0):
            if (total == 1):
                Log_nothing_to_do()
            if (total > 1):
                if self._position == False:
                    Log_buy(self._tradeSymbol, self._tradeQuatity)
                    buy_success = self.__buy(self._tradeSymbol, self._tradeQuatity)
                    if (buy_success):
                        self._position = True
                    else:
                        self._position = False
                        Log_big_error()
                else:
                    Log_nothing_to_do()
            if (total < 0):
                if self._position == True:
                    Log_sell(self._tradeSymbol, self._tradeQuatity)
                    sell_success = self.__sell(self._tradeSymbol, self._tradeQuatity)
                    if (sell_success):
                        self._position = False
                    else:
                        self._position = True
                        Log_big_error()
                else:
                    Log_nothing_to_do()
        else:
            Log_nothing_to_do()

    def _strategie_rsi(self, ret_value_rsi):
        rsi_val = ret_value_rsi
        if (rsi_val == 1)
            if self._position == False:
                Log_buy(self._tradeSymbol, self._tradeQuatity)
                buy_success = self.__buy(self._tradeSymbol, self._tradeQuatity)
                if (buy_success):
                    self._position = True
                else:
                    self._position = False
                    Log_big_error()
            else:
                Log_nothing_to_do()
        elif (rsi_val == -1)
            if self._position == True:
                Log_sell(self._tradeSymbol, self._tradeQuatity)
                sell_success = self.__sell(self._tradeSymbol, self._tradeQuatity)
                if (sell_success):
                    self._position = False
                else:
                    self._position = True
                    Log_big_error()
            else:
                Log_nothing_to_do()
        else:
            Log_nothing_to_do()

    def _strategie_bollinger(self, ret_value_bollinger):
        bollinger = ret_value_bollinger
        if (rsi_val == 1)
            if self._position == False:
                Log_buy(self._tradeSymbol, self._tradeQuatity)
                buy_success = self.__buy(self._tradeSymbol, self._tradeQuatity)
                if (buy_success):
                    self._position = True
                else:
                    self._position = False
                    Log_big_error()
            else:
                Log_nothing_to_do()
        elif (rsi_val == -1)
            if self._position == True:
                Log_sell(self._tradeSymbol, self._tradeQuatity)
                sell_success = self.__sell(self._tradeSymbol, self._tradeQuatity)
                if (sell_success):
                    self._position = False
                else:
                    self._position = True
                    Log_big_error()
            else:
                Log_nothing_to_do()
        else:
            Log_nothing_to_do()

    def __onOpen(ws):
        print('########### OPEN CONNECTION ###########')

    def __onClose(ws):
        print('########### CLOSE CONNECTION ###########')
 
    def __onError(ws, error):
        print(error)

    def __onMessage(ws, message):
        json_message = json.loads(message)
        #pprint.pprint(json_message) # 
        candle = json_message['k']
        candle_price_close = candle['c']
        close = candle['x']
        if close:
            print("candle closed at {}".format(candle_price_close))
            self._closes.append(float(candle_price_close))
            print(len(self._closes))
            if len(self._closes) > self._rsiPeriod:
                np_closes = numpy.array(closes)
                rsi = talib.RSI(np_closes, RSI_PERIOD)
                print("##################")            
                #print(rsi)
                last_rsi = rsi[-1]
                print("the current rsi is {}".format(last_rsi))
                ret_value_rsi = RSI_strat(last_rsi, self._position)
                ret_value_bollinger = bollinger_strat(closes, len(closes))
                #print("##################")
                #print("deja achete {}".format(self._position))
                print("ret_value_rsi ->", ret_value_rsi)
                print("ret_value_bollinger ->", ret_value_bollinger)
                #print("##################")
                #self._choice(ret_value_rsi ,ret_value_bollinger)
                self._strategie_bollinger(ret_value_bollinger)
                Log_status(self._client)
                print("##################")

    def Start(self):
        websocket.enableTrace(True)
        ws = websocket.WebSocketApp(self._socket, on_open=self.__onOpen, on_close=self.__onClose, on_message=self.__onMessage)
        ws.run_forever()

