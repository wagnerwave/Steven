RSI_OVERBOUGHT = 65
RSI_OVERSOLD = 40

def RSI_strat(last_rsi, in_position):
    if last_rsi >= RSI_OVERBOUGHT:
        if in_position == True:
            #("rsi : sell")
            return -1
        else:
            #("rsi : nothing to do")
            return 0
    elif last_rsi <= RSI_OVERSOLD:
        if in_position == True:
            #("rsi : nothing to do")
            return 0
        else:
            #("rsi : buy")
            return 1
    else:
        #("rsi : nothing to do")    
        return 0