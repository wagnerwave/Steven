# Websocket for Ethirum 

WS_ETH_SHORT = "wss://stream.binance.com:9443/ws/ethusdt@kline_1m" # Don't forget to change 1m for 1h
WS_ETH_MEDIUM = "wss://stream.binance.com:9443/ws/ethusdt@kline_1w"
WS_ETH_LONG = "wss://stream.binance.com:9443/ws/ethusdt@kline_1m"

# Websocket for Bitcoin

WS_BTC_SHORT = ""
WS_BTC_MEDIUM = ""
WS_BTC_LONG = ""

# Websocket for Monero

WS_XMR_SHORT = ""
WS_XMR_MEDIUM = ""
WS_XMR_LONG = ""


def getSocket(period, symbol):
    if (period != "short" and period != "medium" and period != "long"):
        print("Error: {} period is not allowed...".format(period))
        exit(1)
    else :
        if (symbol == "ETH"):
            if (period == "short"):
                return WS_ETH_SHORT
            elif (period == "medium"):
                return WS_ETH_MEDIUM
            elif (period == "long"):
                return WS_ETH_LONG
            else:
                print("Error: cannot find the right socket...")
                exit(1)
        elif (symbol == "BTC"):
            if (period == "short"):
                return WS_BTC_SHORT
            elif (period == "medium"):
                return WS_BTC_MEDIUM
            elif (period == "long"):
                return WS_BTC_LONG
            else:
                print("Error: cannot find the right socket...")
                exit(1)
        elif (symbol == "XMR"):
            if (period == "short"):
                return WS_XMR_SHORT
            elif (period == "medium"):
                return WS_XMR_MEDIUM
            elif (period == "long"):
                return WS_XMR_LONG
            else:
                print("Error: cannot find the right socket...")
                exit(1)
        else:
            print("Error: sectioned symbol is not allowed...")
            exit(1)