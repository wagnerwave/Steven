#!/usr/bin/env python3

import sys
from bot import Bot

def Usage():
    print("python3 main.py [Period] [Symbol] [Quantity]")
    print()
    print("Exemple : python3 main.py short BTC 0.001")
    print()
    print("Period : Short - Medium - Long")
    print("\t Short : 1 hour")
    print("\t Day : 1 day")
    print("\t Medium : 1 week")
    print("\t Long : 1 mouth")
    print()
    print("Symbol : BTC - ETH - XMR")
    print("\t BTC : Bitcoin")
    print("\t ETH : Etherium ")
    print("\t XMR : Monero")
    print()
    print("Quatity : the quantities of money for your trading bot")
    print("\t Exemple : 0.650")


def parsing_period(arg):
    if (arg == "Short" or arg == "short" or arg == "SHORT" or arg == 'S' or arg == 's'):
        return "short"
    elif (arg == "Medium" or arg == "medium" or arg == "MEDIUM" or arg == 'M' or arg == 'm'):
        return "medium"
    elif (arg == "Long" or arg == "long" or arg == "LONG" or arg == 'L' or arg == 'l'):
        return "long"
    elif (arg == "Day" or arg == "day" or arg == "DAY" or arg == "D" or arg == 'd')
        return "day"
    else:
        Usage()
        exit(1)

def parsing_symbol(arg):
    if (arg == "BTC" or arg == "btc"):
        return "BTC"
    elif (arg == "ETH" or arg == "eth"):
        return "ETH"
    elif (arg == "XMR" or arg == "xmr"):
        return "XMR"
    else:
        Usage()
        exit(1)

def parsing_quantity(arg):
    try:
        return float(arg)
    except:
        Usage()
        exit(1)

if __name__ == "__main__":
    if (len(sys.argv) == 4):
        period = parsing_period(sys.argv[1])
        symbol = parsing_symbol(sys.argv[2])
        quantity = parsing_quantity(sys.argv[3])
        Steven = Bot(period=period, symbol=symbol, quatity=quantity)
        Steven.Start()
    else:
        Usage()
        exit(0)