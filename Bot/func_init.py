# GET FROM CLIENT ON BINANCE LIBRARY
KLINE_INTERVAL_1MINUTE = '1m'
KLINE_INTERVAL_3MINUTE = '3m'
KLINE_INTERVAL_5MINUTE = '5m'
KLINE_INTERVAL_15MINUTE = '15m'
KLINE_INTERVAL_30MINUTE = '30m'
KLINE_INTERVAL_1HOUR = '1h'
KLINE_INTERVAL_2HOUR = '2h'
KLINE_INTERVAL_4HOUR = '4h'
KLINE_INTERVAL_6HOUR = '6h'
KLINE_INTERVAL_8HOUR = '8h'
KLINE_INTERVAL_12HOUR = '12h'
KLINE_INTERVAL_1DAY = '1d'
KLINE_INTERVAL_3DAY = '3d'
KLINE_INTERVAL_1WEEK = '1w'
KLINE_INTERVAL_1MONTH = '1M'

def init_period(period):
    if (period != "short" and period != "medium" and period != "long" and period != "day" and period != "veryshort"):
        print("Error: {} period is not allowed...".format(period))
        exit(1)
    else :
        if (period == "short"):
            return KLINE_INTERVAL_1HOUR
        elif (period == "veryshort"):
            return KLINE_INTERVAL_1MINUTE
        elif (period == "medium"):
            return KLINE_INTERVAL_1WEEK
        elif (period == "long"):
            return KLINE_INTERVAL_1MONTH
        elif (period == "day"):
            return KLINE_INTERVAL_1DAY
        else:
            print("Error: cannot find the right socket...")
            exit(1)

def init_pair_trade(symbol):
    if (symbol == "ETH"):
        return "ETHBUSD"
    elif (symbol == "BTC"):
        return "BTCBUSD"
    elif (symbol == "XMR"):
        return "XMRBUSD"
    else:
        print("Error: cannot find the right pair for trade...")
        exit(1)

def init_tradeAlgorithm(tradeAlgo):
    if (tradeAlgo == "RSI"):
        return "rsi"
    elif (tradeAlgo == "BOL"):
        return "bolinger"
    elif (tradeAlgo == "RSIBOL" or tradeAlgo == "BOLRSI"):
        return "rsi_bolinger"
    else:
        return "error"