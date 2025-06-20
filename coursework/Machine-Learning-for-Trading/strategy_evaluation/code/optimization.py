""""""  		  	   		  		 		  		  		    	 		 		   		 		  
"""MC1-P2: Optimize a portfolio.  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		  		 		  		  		    	 		 		   		 		  
Atlanta, Georgia 30332  		  	   		  		 		  		  		    	 		 		   		 		  
All Rights Reserved  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
Template code for CS 4646/7646  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		  		 		  		  		    	 		 		   		 		  
works, including solutions to the projects assigned in this course. Students  		  	   		  		 		  		  		    	 		 		   		 		  
and other users of this template code are advised not to share it with others  		  	   		  		 		  		  		    	 		 		   		 		  
or to make it available on publicly viewable websites including repositories  		  	   		  		 		  		  		    	 		 		   		 		  
such as github and gitlab.  This copyright statement should not be removed  		  	   		  		 		  		  		    	 		 		   		 		  
or edited.  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
We do grant permission to share solutions privately with non-students such  		  	   		  		 		  		  		    	 		 		   		 		  
as potential employers. However, sharing with other current or future  		  	   		  		 		  		  		    	 		 		   		 		  
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		  		 		  		  		    	 		 		   		 		  
GT honor code violation.  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
-----do not edit anything above this line---  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
Student Name: Yu-Xi Chen 		  	   		  		 		  		  		    	 		 		   		 		  
GT User ID: ychen3281"	  	   		  		 		  		  		    	 		 		   		 		  
GT ID: 903566160 		  	   		  		 		  		  		    	 		 		   		 		  
"""  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
import datetime as dt  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
import numpy as np  		  	   		  		 		  		  		    	 		 		   		 		 
import scipy.optimize as spo  		  	   		  		 		  		  		    	 		 		   		 		  
import matplotlib.pyplot as plt  		  	   		  		 		  		  		    	 		 		   		 		  
import pandas as pd  		  	   		  		 		  		  		    	 		 		   		 		  
from util import get_data, plot_data  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
 		  	   		  		 		  		  		    	 		 		   		 		  
        
        
# This is the function that will be tested by the autograder  		  	   		  		 		  		  		    	 		 		   		 		  
# The student must update this code to properly implement the functionality  		  	   		  		 		  		  		    	 		 		   		 		  
def optimize_portfolio(  		  	   		  		 		  		  		    	 		 		   		 		  
    sd=dt.datetime(2010, 1, 1),  		  	   		  		 		  		  		    	 		 		   		 		  
    ed=dt.datetime(2010, 12, 31),  		  	   		  		 		  		  		    	 		 		   		 		  
    syms=["GOOG", "AAPL", "GLD", "XOM"],  		  	   		  		 		  		  		    	 		 		   		 		  
    gen_plot=True,  		  	   		  		 		  		  		    	 		 		   		 		  
):  		  	   		  		 		  		  		    	 		 		   		 		  
    
    # Read in adjusted closing prices for given symbols, date range  		  	   		  		 		  		  		    	 		 		   		 		  
    dates = pd.date_range(sd, ed)  		  	   		  		 		  		  		    	 		 		   		 		  
    prices_all = get_data(syms, dates)  # automatically adds SPY  		  	   		  		 		  		  		    	 		 		   		 		  
    prices = prices_all[syms]  # only portfolio symbols  		  	   		  		 		  		  		    	 		 		   		 		  
    prices_SPY = prices_all["SPY"]  # only SPY, for comparison later  		  	   		  		 		  		  		    	 		 		   		 		  

    # find the allocations for the optimal portfolio  		  	   		  		 		  		  		    	 		 		   		 		  
    # note that the values here ARE NOT meant to be correct for a test case  		  	   		  		 		  		  		    	 		 		   		 		  
    
    
    init_allocs = np.array(len(syms) * [1/len(syms)])   # add code here to find the allocations  		  	   		  		 		  		  		    	 		 		   		 		  
    
    rets = np.log(prices/prices.shift(1))

    
    def stats(init_allocs):
        normed = prices/prices.iloc[0]
        alloc = init_allocs * normed
        portval = alloc.sum(axis=1)
        dr = portval.pct_change()[1:]
        adr = dr.mean()
        sdr = dr.std()
        sr = (dr.mean()/dr.std()) * np.sqrt(252)
        return adr, sdr, sr
        
    #minimize negative sr 
    def min_sr(init_allocs):
        return -stats(init_allocs)[2] 
        
    c = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
    b = tuple((0, 1) for x in init_allocs)
    opts = spo.minimize(min_sr, init_allocs, method='SLSQP', bounds=b, constraints=c)
    
    allocs = opts['x']

    
    #stats
#     cr, adr, sddr, sr = [  		  	   		  		 		  		  		    	 		 		   		 		  
#         0.25,  		  	   		  		 		  		  		    	 		 		   		 		  
#         0.001,  		  	   		  		 		  		  		    	 		 		   		 		  
#         0.0005,  		  	   		  		 		  		  		    	 		 		   		 		  
#         2.1,  		  	   		  		 		  		  		    	 		 		   		 		  
#     ]  # add code here to compute stats  		  	   		  		 		  		  		    	 		 		   		 		  

    rfr = 0
    sf = 252
    
    syms_normed = prices/prices.iloc[0]
    alloced = syms_normed * allocs
    port_val = alloced.sum(axis=1)
    
    
    dr = port_val.pct_change()[1:]
    
    #print('dr:', dr)
    adr = dr.mean()
    cr = (prices.iloc[-1]/prices.iloc[0])-1
    sddr = dr.std()
    sr = (adr-rfr)/(sddr-rfr) * np.sqrt(sf)
    
    
    # add code here to compute daily portfolio values  		  	   		  		 		  		  		    	 		 		   		 		  
    spy_normed = prices_SPY/prices_SPY.iloc[0]  
    
   	  	   		  		 		  		  		    	 		 		   		 		  
    # Compare daily portfolio value with SPY using a normalized plot  		  	   		  		 		  		  		    	 		 		   		 		 
    if gen_plot == True:
        # add code to plot here  		  	   		  		 		  		  		    	 		 		   		 		  
        df_temp = pd.concat(  		  	   		  		 		  		  		    	 		 		   		 		  
            [port_val, spy_normed], keys=["Portfolio", "SPY"], axis=1  		  	   		  		 		  		  		    	 		 		   		 		  
            )
        
        fig = df_temp.plot(title = 'Normalized Daily Portfolio Value vs. Normalized SPY', grid=True).get_figure()
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.margins(x=0)
        fig.savefig('Figure_1.png')
    
        
        pass  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
    return allocs, cr, adr, sddr, sr  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 	  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		  	   		  		 		  		  		    	 		 	 		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
def test_code():  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    This function WILL NOT be called by the auto grader.  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
    start_date = dt.datetime(2008, 6, 1)  		  	   		  		 		  		  		    	 		 		   		 		  
    end_date = dt.datetime(2009, 6, 1)  		  	   		  		 		  		  		    	 		 		   		 		  
    symbols = ['IBM', 'X', 'GLD', 'JPM']  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
    # Assess the portfolio  		  	   		  		 		  		  		    	 		 		   		 		  
    allocations, cr, adr, sddr, sr = optimize_portfolio(  		  	   		  		 		  		  		    	 		 		   		 		  
        sd=start_date, ed=end_date, syms=symbols, gen_plot=True  		  	   		  		 		  		  		    	 		 		   		 		  
    )  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
    # Print statistics  		  	   		  		 		  		  		    	 		 		   		 		  
    print(f"Start Date: {start_date}")  		  	   		  		 		  		  		    	 		 		   		 		  
    print(f"End Date: {end_date}")  		  	   		  		 		  		  		    	 		 		   		 		  
    print(f"Symbols: {symbols}")  		  	   		  		 		  		  		    	 		 		   		 		  
    print(f"Allocations:{allocations}")  		  	   		  		 		  		  		    	 		 		   		 		  
    print(f"Sharpe Ratio: {sr}")  		  	   		  		 		  		  		    	 		 		   		 		  
    print(f"Volatility (stdev of daily returns): {sddr}")  		  	   		  		 		  		  		    	 		 		   		 		  
    print(f"Average Daily Return: {adr}")  		  	   		  		 		  		  		    	 		 		   		 		  
    print(f"Cumulative Return: {cr}")  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
if __name__ == "__main__":  		  	   		  		 		  		  		    	 		 		   		 		  
    # This code WILL NOT be called by the auto grader  		  	   		  		 		  		  		    	 		 		   		 		  
    # Do not assume that it will be called  		  	   		  		 		  		  		    	 		 		   		 		  
    test_code()  		  	   		  		 		  		  		    	 		 		   		 		  
