import math, numpy

def sma(closes_candles, n):
    res = 0
    for x in closes_candles:
        if x == numpy.nan:
            continue
        else:
            res += x
    return (res / n)

def standardDeviation(candles, n):
    deviation = 0.0
    average = sma(candles, n)
    for x in candles:
        if x == numpy.nan:
            continue
        else:
            deviation += pow(x - average, 2)
    return math.sqrt(deviation / n)

def bollinger_strat(candles, n):
    n = n - 1
    print("####################################")
    print("sma")
    x = sma(candles[-n:], n)
    print(x)
    print("std_dev")
    std_dev = standardDeviation(candles[-n:], n)
    print(std_dev)
    print("####################################")
    A1 = x + std_dev * 2
    B1 = x + std_dev
    B2 = x - std_dev
    A2 = x - std_dev * 2
    close = candles[-1]
    if (close >= B1 and close <= A1):
        print("bollinger: buy")
        return 1
    elif (close < B2 and close >= A2):
        print("bollinger: sell")
        return -1
    else:
        print("bollinger : nothing to do")
        return 0