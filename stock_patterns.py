from datetime import date
import pandas as pd
import talib
from nsepy import get_history, symbols

SYMBOL = ["NIFTY","BANKNIFTY","NIFTY 50"]

df = symbols.get_symbol_list()
print(df['SYMBOL'])


"""	

    Index price history
	symbol can take these values (These indexes have derivatives as well)
	"NIFTY" or "NIFTY 50",
	"BANKNIFTY" or "NIFTY BANK",
	"NIFTYINFRA" or "NIFTY INFRA",
    "NIFTYIT" or "NIFTY IT",
    "NIFTYMID50" or "NIFTY MIDCAP 50",
    "NIFTYPSE" or "NIFTY PSE"
    nifty['High'].plot(secondary_y='Turnover')
    plt.show()
	In addition to these there are many indices
	For full list refer- http://www.nseindia.com/products/content/equities/indices/historical_index_data.htm

"""

def pattern_recognition(open, high, low, close):

    morning_star = talib.CDLMORNINGSTAR(open, high, low, close)
    print("----------------------------------------------------------------")
    print(f"MorningStar {symbol}:",morning_star[morning_star != 0])

    engulf = talib.CDLENGULFING(open, high, low, close)
    print("----------------------------------------------------------------")
    print(f"Engulfing {symbol}:",engulf[engulf != 0])

    evening_doji = talib.CDLEVENINGDOJISTAR(open, high, low, close, penetration=0)
    print("----------------------------------------------------------------")
    print(f"Evening_doji {symbol}:",evening_doji[evening_doji != 0])
    
    harami = talib.CDLHARAMI(open, high, low, close)
    print("----------------------------------------------------------------")
    print(f"Harami {symbol}:",harami[harami != 0])
    
    harami_cross = talib.CDLHARAMICROSS(open, high, low, close)
    print("----------------------------------------------------------------")
    print(f"Harami {symbol}:",harami_cross[harami_cross != 0])



for symbol in df['SYMBOL']:

    data = get_history(
                        symbol=symbol, 
                        start=date(2021,6,1), 
                        end=date(2021,8,5),
                    )

    open = data['Open']
    close = data['Close']
    high = data['High']
    low = data['Low']

    
    morning_star = talib.CDLMORNINGSTAR(open, high, low, close)
    #print(type(morning_star))
    star_df = pd.DataFrame({'date':morning_star.index, 'value':morning_star.values})
    print(star_df['value'])
    if star_df['value'].all() == 0:
        print('adasd')

    #print(print(morning_star.reset_index()))
    if star_df.loc[star_df['value'] == 0]:
        print("----------------------------------------------------------------")
        print(f"MorningStar {symbol}:",star_df['value'],star_df['date'])
    else:
        print("Nothing Found")

    # engulf = talib.CDLENGULFING(open, high, low, close)
    # if engulf[engulf!=0]:
    #     print("----------------------------------------------------------------")
    #     print(f"Engulfing {symbol}:",engulf)

    # evening_doji = talib.CDLEVENINGDOJISTAR(open, high, low, close, penetration=0)
    # if evening_doji[evening_doji != 0]:
    #     print("----------------------------------------------------------------")
    #     print(f"Evening_doji {symbol}:",evening_doji[evening_doji != 0])
    
    # harami = talib.CDLHARAMI(open, high, low, close)
    # if harami[harami!=0]:
    #     print("----------------------------------------------------------------")
    #     print(f"Harami {symbol}:",harami[harami != 0])
    
    # harami_cross = talib.CDLHARAMICROSS(open, high, low, close)
    # if harami_cross[harami_cross!=0]:
    #     print("----------------------------------------------------------------")
    #     print(f"Harami {symbol}:",harami_cross[harami_cross != 0])

    
