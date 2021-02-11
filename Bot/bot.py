from binance.client import Client
from binance.websockets import BinanceSocketManager
from binance.enums import *
from func_init import init_period, init_pair_trade
from log import *
from rsi import RSI_strat, RSI_OVERBOUGHT, RSI_OVERSOLD
from bollinger import bollinger_strat
from config import API_KEY, API_SECRET_KEY

import json, pprint, numpy, math
import datetime

class Bot:
    def __init__(self, period, symbol, quatity):
        self._tradeSymbol = symbol
        self._tradeQuatity = quatity
        self._pair_trade = init_pair_trade(self._tradeSymbol)
        self._period = init_period(period)
        self._position = False
        try:
            self._client = Client(API_KEY, API_SECRET_KEY, tld='us')
        except:
            print("Error: Cannot connect client (check your API KEY)")
            exit(1)
        self._closes = []
        self._rsiPeriod = 14
        self._socket = BinanceSocketManager(self._client)

    def _connection_test(self):
        status = self._client.get_system_status()
        if self._client.ping() == False:
            print("Error: ping client doesn't work.")
            exit(1)
            if status['status'] != 0:
                print("Error: System maintenance.")
                exit(1)
        else :
            print("#####################################")
            print("SERVER : Connection is okay and server status is", status['msg'])
            print("#####################################")

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
        if (rsi_val == 1):
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
        elif (rsi_val == -1):
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
        if (bollinger == 1):
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
        elif (bollinger == -1):
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

    def _process_message(self, msg):
        json_message = msg
        pprint.pprint(json_message) #
        candle = json_message['k']
        candle_price_close = candle['c']
        close = candle['x']
        if close:
            Log_candle_close(candle_price_close, self._tradeSymbol)
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
        Log_start()
        self._connection_test()
        Log_status(client=self._client)
        Log_parameter(symbol=self._pair_trade ,quantity=self._tradeQuatity, period=self._period)
        self._socket.start_kline_socket(symbol=self._pair_trade, callback=self._process_message, interval=self._period)
        #self._socket.start_kline_socket(symbol=self._pair_trade, callback=self._process_message, interval=self._period)
        self._socket.start()