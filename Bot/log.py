
def Log_nothing_to_do():
    print("[{}] STEVEN : Nothing to do...".format((str(datetime.datetime.now()))))

def Log_buy(symbol, quantity):
    print("[{}}] STEVEN : Buy {} For {} quantities...".format((str(datetime.datetime.now())), symbol, quantity))

def Log_sell(symbol, quantity):
    print("[{}}] STEVEN : Sell {} For {} quantities...".format((str(datetime.datetime.now())), symbol, quantity))

def Log_big_error():
    print("[{}] BIG ERROR: cannot sell !!!")
    exit(1) 

def Log_status(client):
    BTC = client.get_asset_balance(asset='BTC')
    ETH = client.get_asset_balance(asset='ETH')
    USDC = client.get_asset_balance(asset='USDC')
    XMR = client.get_asset_balance(asset='XMR')
    print("[{}] CRYPTO STATUS : ".format((str(datetime.datetime.now()))))
    print("\t\t Bitcoin [BTC] : {}".format(BTC))
    print("\t\t Etherium [ETH]: {}".format(ETH))
    print("\t\t USDC [$$$] : {}".format(USDC))
    print("\t\t XMR [Monero] : {}".format(XMR))

def Log_candle_close(candle_price_close, symbol):
    print("[{}] {} candle close : {}".format((str(datetime.datetime.now())), symbol, candle_price_close))