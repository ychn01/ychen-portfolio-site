import datetime as dt
import pandas as pd
from util import get_data, plot_data  		  	   		  		 		  		  		    	 		 		   		 		  
    
def author():
        return "ychen3281"

def benchmark(symbol="AAPL", sd=dt.datetime(2010, 1, 1), ed=dt.datetime(2011,12,31), sv = 100000):
    price = get_data([symbol], pd.date_range(sd, ed)).reset_index().rename(columns={'index': 'Date'})
    del price['SPY']
    price['Order'] = "HOLD"
    price.loc[0, 'Order'] = "BUY"
    price['Shares'] = 0
    price.loc[0, 'Shares'] = 1000

    bm_df = price.copy()
    bm_df["Symbol"] = symbol
    del bm_df[symbol]
    
    return bm_df

def trades(symbol="AAPL", sd=dt.datetime(2010, 1, 1), ed=dt.datetime(2011,12,31), sv = 100000):
    price = get_data([symbol], pd.date_range(sd, ed)).reset_index().rename(columns={'index': 'Date'})
    del price['SPY']
    price['Order'] = None
    price.loc[0, 'Order'] = "BUY"
    price['Hold'] = 0 
    price.loc[0, 'Hold'] = 1000
    price['Shares'] = 0
    price.loc[0, 'Shares'] = 1000

    for i, col in price[1:].iterrows():
        today_price = col[symbol]
        prev_hold = price.at[i-1, 'Hold']
        
        if i < len(price) - 1:
            tmrw_price = price.iloc[i + 1][symbol]
            if tmrw_price > today_price:
                if prev_hold == 1000:
                    price.at[i, 'Order'] = "HOLD"
                    price.at[i, 'Hold'] = prev_hold
                    price.at[i, 'Shares'] = 0 
                elif prev_hold == 0: 
                    price.at[i, 'Order'] = "BUY"
                    price.at[i, 'Hold'] = prev_hold + 1000
                    price.at[i, 'Shares'] = 1000 
                elif prev_hold == -1000:
                    price.at[i, 'Order'] = "BUY"
                    price.at[i, 'Hold'] = prev_hold + 2000
                    price.at[i, 'Shares'] = 2000 
                    
            elif tmrw_price < today_price:
                if prev_hold <= -1000:
                    price.at[i, 'Order'] = "HOLD"
                    price.at[i, 'Hold'] = prev_hold
                    price.at[i, 'Shares'] = 0 
                elif prev_hold == 0:     
                    price.at[i, 'Order'] = "SELL"
                    price.at[i, 'Hold'] = prev_hold - 1000
                    price.at[i, 'Shares'] = 1000 
                elif prev_hold == 1000:
                    price.at[i, 'Order'] = "SELL"
                    price.at[i, 'Hold'] = prev_hold - 2000
                    price.at[i, 'Shares'] = 2000 
        else:
            price.at[i, 'Order'] = "HOLD"
            price.at[i, 'Hold'] = prev_hold
            price.at[i, 'Shares'] = 0 

    trades_df = price.copy()
    trades_df["Symbol"] = "JPM"
    del trades_df["JPM"]
    del trades_df["Hold"]
    return trades_df

def testPolicy(symbol="AAPL", sd=dt.datetime(2010, 1, 1), ed=dt.datetime(2011,12,31), sv = 100000):
    price = get_data([symbol], pd.date_range(sd, ed)).reset_index().rename(columns={'index': 'Date'})
    del price['SPY']
    price['Order'] = None
    price.loc[0, 'Order'] = "BUY"
    price['Hold'] = 0 
    price.loc[0, 'Hold'] = 1000
    price['Shares'] = 0
    price.loc[0, 'Shares'] = 1000

    for i, col in price[1:].iterrows():
        today_price = col[symbol]
        prev_hold = price.at[i-1, 'Hold']
        
        if i < len(price) - 1:
            tmrw_price = price.iloc[i + 1][symbol]
            if tmrw_price > today_price:
                if prev_hold == 1000:
                    price.at[i, 'Order'] = "HOLD"
                    price.at[i, 'Hold'] = prev_hold
                    price.at[i, 'Shares'] = 0 
                elif prev_hold == 0: 
                    price.at[i, 'Order'] = "BUY"
                    price.at[i, 'Hold'] = prev_hold + 1000
                    price.at[i, 'Shares'] = 1000 
                elif prev_hold == -1000:
                    price.at[i, 'Order'] = "BUY"
                    price.at[i, 'Hold'] = prev_hold + 2000
                    price.at[i, 'Shares'] = 2000 
                    
            elif tmrw_price < today_price:
                if prev_hold <= -1000:
                    price.at[i, 'Order'] = "HOLD"
                    price.at[i, 'Hold'] = prev_hold
                    price.at[i, 'Shares'] = 0 
                elif prev_hold == 0:     
                    price.at[i, 'Order'] = "SELL"
                    price.at[i, 'Hold'] = prev_hold - 1000
                    price.at[i, 'Shares'] = -1000 
                elif prev_hold == 1000:
                    price.at[i, 'Order'] = "SELL"
                    price.at[i, 'Hold'] = prev_hold - 2000
                    price.at[i, 'Shares'] = -2000 
        else:
            price.at[i, 'Order'] = "HOLD"
            price.at[i, 'Hold'] = prev_hold
            price.at[i, 'Shares'] = 0 

    testpolicy = price[['Date', 'Shares']].copy()
    testpolicy.set_index('Date', inplace=True)
    return testpolicy