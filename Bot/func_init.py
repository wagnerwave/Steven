def init_period(period):
    if (period != "short" and period != "medium" and period != "long"):
        print("Error: {} period is not allowed...".format(period))
        exit(1)
    else :
        if (period == "short"):
            return "1h"
        elif (period == "medium"):
            return "1w"
        elif (period == "long"):
            return "1m"
        elif (period == "day"):
            retrun "1d"
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
