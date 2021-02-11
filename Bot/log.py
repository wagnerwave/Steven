from get_wallet_data import *
import datetime

def Log_nothing_to_do():
    print("[{}] STEVEN : Nothing to do...".format((str(datetime.datetime.now()))))

def Log_start():
    print("[{}] Start server...".format((str(datetime.datetime.now()))))

def Log_parameter(symbol, quantity, period):
    print("[{}] PARAMETRE : ".format((str(datetime.datetime.now()))))
    print("\t Symbol : {}".format(symbol))
    print("\t Quantity : {}".format(quantity))
    print("\t Period : {}".format(period))

def Log_buy(symbol, quantity):
    print("[{}}] STEVEN : Buy {} For {} quantities...".format((str(datetime.datetime.now())), symbol, quantity))

def Log_sell(symbol, quantity):
    print("[{}}] STEVEN : Sell {} For {} quantities...".format((str(datetime.datetime.now())), symbol, quantity))

def Log_big_error():
    print("[{}] BIG ERROR: cannot sell !!!".format((str(datetime.datetime.now()))))
    exit(1) 

def Log_socket_error():
    print("[{}] ERROR: socket error.".format((str(datetime.datetime.now()))))
    exit(1) 

def Log_status(client):
    print("[{}] WALLET STATUS : ".format((str(datetime.datetime.now()))))
    getAllWallet()

def Log_candle_close(candle_price_close, symbol):
    print("[{}] {} candle close : {}".format((str(datetime.datetime.now())), symbol, candle_price_close))