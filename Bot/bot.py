from binance.client import Client
from binance.websockets import BinanceSocketManager
from binance.enums import *
from func_init import init_period, init_pair_trade, init_tradeAlgorithm
from log import *
from rsi import RSI_strat, RSI_OVERBOUGHT, RSI_OVERSOLD
from bollinger import bollinger_strat
from config import API_KEY, API_SECRET_KEY

import json, pprint, numpy, math
import datetime

class Bot:
    def __init__(self, period, symbol, quatity, tradeAlgo):
        self._tradeSymbol = symbol
        self._tradeQuatity = quatity
        self._pair_trade = init_pair_trade(self._tradeSymbol)
        self._period = init_period(period)
        self._position = False
        self._tradingAlgorithm = init_tradeAlgorithm(tradeAlgo)
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
        # Get message
        json_message = msg
        # pprint.pprint(json_message) / Function for print message 
        # Get information on json message
        candle = json_message['k']
        candle_price_close = candle['c']
        close = candle['x']
        # Check if candle is closed
        if close:
            # Print log 
            Log_candle_close(candle_price_close, self._tradeSymbol)
            self._closes.append(float(candle_price_close))
            print(len(self._closes))
            # Check is the lenght of closes is > to the rsi period
            if len(self._closes) > self._rsiPeriod:
                np_closes = numpy.array(closes)
                # Function RSI
                rsi = talib.RSI(np_closes, RSI_PERIOD)
                print("##################")
                # Get the last RSI
                last_rsi = rsi[-1]
                print("the current rsi is {}".format(last_rsi))
                ret_value_rsi = RSI_strat(last_rsi, self._position)
                ret_value_bollinger = bollinger_strat(closes, len(closes))
                print("ret_value_rsi ->", ret_value_rsi)
                print("ret_value_bollinger ->", ret_value_bollinger)
                if (self._tradingAlgorithm == "rsi"):
                    self._strategie_rsi(ret_value_rsi)
                elif (self._tradingAlgorithm == "bolinger"):
                    self._strategie_bollinger(ret_value_bollinger)
                elif (self._tradingAlgorithm == "rsi_bolinger"):
                    self._strategie_rsi_bollinger(ret_value_rsi, ret_value_bollinger)
                else:
                    Log_error("no trading algorithm found")
                    exit(1)
                Log_status(self._client)
                print("##################")

    def Start(self):
        Log_start()
        self._connection_test()
        Log_status(client=self._client)
        Log_parameter(symbol=self._pair_trade ,quantity=self._tradeQuatity, period=self._period)
        self._socket.start_kline_socket(symbol=self._pair_trade, callback=self._process_message, interval=self._period)
        self._socket.start()