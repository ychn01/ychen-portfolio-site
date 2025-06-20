import datetime as dt  		  	   		  		 		  		  		    	 		 		   		 		  
import random  		  	   		  		 		  		  		    	 		 		   		 		  
import matplotlib.pyplot as plt  		  	   		  		 		  		  		    	 		 		   		 		  
import pandas as pd  		  	   		  		 		  		  		    	 		 		   		 		  
from util import get_data, plot_data  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		 
import indicators as ind
import marketsimcode as msc	 	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
def author():
    return "ychen3281"
		  	   		  		 		  		  		    	 		 		   		 		  
class ManualLearner(object):  		  	   		  		 		  		  		    	 		 		   		 		  	  		 		  		  		    	 		 		   		 		  
    # constructor  		  	   		  		 		  		  		    	 		 		   		 		  
    def __init__(self, verbose=False, impact=0.005, commission=9.95):  		  	   		  		 		  		  		    	 		 		   		 		  
        """  		  	   		  		 		  		  		    	 		 		   		 		  
        Constructor method  		  	   		  		 		  		  		    	 		 		   		 		  
        """  		  	   		  		 		  		  		    	 		 		   		 		  
        self.verbose = verbose  		  	   		  		 		  		  		    	 		 		   		 		  
        self.impact = impact  		  	   		  		 		  		  		    	 		 		   		 		  
        self.commission = commission  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   	  	   		  		 		  		  		    	 		 		   		 		  
    def trades(symbol="JPM", sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009,12,31), sv = 100000):
    
        trade = get_data([symbol], pd.date_range(sd, ed)).reset_index().rename(columns={'index': 'Date'})
        del trade['SPY']
        trade['Order'] = None
        trade.loc[0, 'Order'] = "BUY"
        trade['Hold'] = 0 
        trade.loc[0, 'Hold'] = 1000
        trade['Shares'] = 0
        trade.loc[0, 'Shares'] = 1000
        
        syms = [symbol]
        lookback_pd = sd - dt.timedelta(days=50)
        dates = pd.date_range(lookback_pd, ed)
        prices_all = get_data(syms, dates)
        prices = prices_all[syms]
        prices.fillna(method ='ffill',inplace=True)
        prices.fillna(method ='bfill',inplace=True)
        syms_normed = prices/prices.iloc[0]

        trade = pd.merge(trade, syms_normed, on='JPM', how='left')

        
        bbp_vals = ind.calc_bbp(prices)
        ema_vals = ind.calc_ema(prices)
        mom_vals = ind.calc_momentum(prices)
        rsi_vals = ind.calc_rsi(prices)
        macd_vals, sig_vals = ind.calc_macd(prices)
        
        macd_vals.loc[macd_vals['MACD'] > sig_vals['Signal'], 'ind'] = 1
        macd_vals.loc[macd_vals['MACD'] < sig_vals['Signal'], 'ind'] = -1
        
        #print(rsi_vals)
        for i, col in trade[1:].iterrows():
            today_price = col[symbol]
            prev_hold = trade.at[i-1, 'Hold']
            
            if i < len(trade) - 1:
                tmrw_price = trade.iloc[i + 1][symbol]
                bbp = bbp_vals.iloc[i]['BBP']
                ema = ema_vals.iloc[i]['EMA']
                mom = mom_vals.iloc[i]['Momentum']
                rsi = rsi_vals.iloc[i]['RSI']
                macd = macd_vals.iloc[i]['ind']
                
                if mom>=1 or rsi<=30 or bbp<=20:
                    if prev_hold == 1000:
                        trade.at[i, 'Order'] = "HOLD"
                        trade.at[i, 'Hold'] = prev_hold
                        trade.at[i, 'Shares'] = 0 
                    elif prev_hold == 0: 
                        trade.at[i, 'Order'] = "BUY"
                        trade.at[i, 'Hold'] = prev_hold + 1000
                        trade.at[i, 'Shares'] = 1000 
                    elif prev_hold == -1000:
                        trade.at[i, 'Order'] = "BUY"
                        trade.at[i, 'Hold'] = prev_hold + 2000
                        trade.at[i, 'Shares'] = 2000 
                    else:
                        pass  
                        
                elif bbp>20 and rsi>40 and mom<=-0.1:
                    if prev_hold <= -1000:
                        trade.at[i, 'Order'] = "HOLD"
                        trade.at[i, 'Hold'] = prev_hold
                        trade.at[i, 'Shares'] = 0 
                    elif prev_hold == 0:     
                        trade.at[i, 'Order'] = "SELL"
                        trade.at[i, 'Hold'] = prev_hold - 1000
                        trade.at[i, 'Shares'] = 1000 
                    elif prev_hold == 1000:
                        trade.at[i, 'Order'] = "SELL"
                        trade.at[i, 'Hold'] = prev_hold - 2000
                        trade.at[i, 'Shares'] = 2000 
                    else:
                        pass
                else:
                    trade.at[i, 'Order'] = "HOLD"
                    trade.at[i, 'Hold'] = prev_hold
                    trade.at[i, 'Shares'] = 0 

        trades_df = trade.copy()
        del trades_df["JPM"]
        del trades_df["Hold"]
        trades_df['Symbol'] = symbol
        return trades_df	  	   		  		 		  		  		    	 		 		   		 		  
                                                                                                
  		  	   		  		 		  		  		    	 		 		   		 		  
if __name__ == "__main__":  		  	   		  		 		  		  		    	 		 		   		 		  
    print("One does not simply think up a strategy")  		  	   		  		 		  		  		    	 		 		   		 		  
