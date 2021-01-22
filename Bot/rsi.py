RSI_OVERBOUGHT = 65
RSI_OVERSOLD = 40

def RSI_strat(last_rsi, in_position):
    if last_rsi >= RSI_OVERBOUGHT:
        if in_position == True:
            print("rsi : sell")
            return -1
        else:
            print("rsi : nothing to do")
            return 0
    elif last_rsi <= RSI_OVERSOLD:
        if in_position == True:
            print("rsi : nothing to do")
            return 0
        else:
            print("rsi : buy")
            return 1
    else:
        print("rsi : nothing to do")    
        return 0