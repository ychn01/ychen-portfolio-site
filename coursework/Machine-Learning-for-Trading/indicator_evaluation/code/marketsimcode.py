""""""  		  	   		  		 		  		  		    	 		 		   		 		  
"""MC2-P1: Market simulator.  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
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
GT User ID: ychen3281  	   		  		 		  		  		    	 		 		   		 		  
GT ID: 903566160 		  	   		  		 		  		  		    	 		 		   		 		  
"""  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
import datetime as dt  		  	   		  		 		  		  		    	 		 		   		 		  
import os  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
import numpy as np  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
import pandas as pd  		  	   		  		 		  		  		    	 		 		   		 		  
from util import get_data, plot_data  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
def author(): 
  return 'ychen3281' 
 		  	   		  		 		  		  		    	 		 		   		 		  
def compute_portvals(  		  	   		  		 		  		  		    	 		 		   		 		  
    trades,  		  	   		  		 		  		  		    	 		 		   		 		  
    start_val=1000000,  		  	   		  		 		  		  		    	 		 		   		 		  
    commission=9.95,  		  	   		  		 		  		  		    	 		 		   		 		  
    impact=0.005,  		  	   		  		 		  		  		    	 		 		   		 		  
):  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    Computes the portfolio values.  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
    :param orders_file: Path of the order file or the file object  		  	   		  		 		  		  		    	 		 		   		 		  
    :type orders_file: str or file object  		  	   		  		 		  		  		    	 		 		   		 		  
    :param start_val: The starting value of the portfolio  		  	   		  		 		  		  		    	 		 		   		 		  
    :type start_val: int  		  	   		  		 		  		  		    	 		 		   		 		  
    :param commission: The fixed amount in dollars charged for each transaction (both entry and exit)  		  	   		  		 		  		  		    	 		 		   		 		  
    :type commission: float  		  	   		  		 		  		  		    	 		 		   		 		  
    :param impact: The amount the price moves against the trader compared to the historical data at each transaction  		  	   		  		 		  		  		    	 		 		   		 		  
    :type impact: float  		  	   		  		 		  		  		    	 		 		   		 		  
    :return: the result (portvals) as a single-column dataframe, containing the value of the portfolio for each trading day in the first column from start_date to end_date, inclusive.  		  	   		  		 		  		  		    	 		 		   		 		  
    :rtype: pandas.DataFrame  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    # this is the function the autograder will call to test your code  		  	   		  		 		  		  		    	 		 		   		 		  
    # NOTE: orders_file may be a string, or it may be a file object. Your  		  	   		  		 		  		  		    	 		 		   		 		  
    # code should work correctly with either input  		  	   		  		 		  		  		    	 		 		   		 		  
    # TODO: Your code here  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
    # In the template, instead of computing the value of the portfolio, we just  		  	   		  		 		  		  		    	 		 		   		 		  
    # read in the value of IBM over 6 months  		  	   		  		 		  		  		    	 		 		   		 		  
    # start_date = dt.datetime(2008, 1, 1)  		  	   		  		 		  		  		    	 		 		   		 		  
    # end_date = dt.datetime(2008, 6, 1)  		  	   		  		 		  		  		    	 		 		   		 		  
    # portvals = get_data(["IBM"], pd.date_range(start_date, end_date))  		  	   		  		 		  		  		    	 		 		   		 		  
    # portvals = portvals[["IBM"]]  # remove SPY  		  	   		  		 		  		  		    	 		 		   		 		  
    # rv = pd.DataFrame(index=portvals.index, data=portvals.values)  		  	   		  		 		  		  		    	 		 		   		 		  
  	
    #trades = pd.read_csv(orders_file)
    trades['Date'] = pd.to_datetime(trades['Date'])
    trades['Date'] = trades['Date'].dt.strftime('%Y-%m-%d')
    trades = trades.sort_values(by="Date", ascending = True)
    syms = trades['Symbol'].unique() 

    start_date = trades['Date'].iloc[0]
    end_date = trades['Date'].iloc[-1]

    price = get_data(syms, pd.date_range(start_date, end_date)).reset_index().rename(columns={'index': 'Date'})
    price['inv']=0
    price['Date'] = price['Date'].dt.strftime('%Y-%m-%d')

    portfolio = pd.DataFrame(columns=['Date', 'Cash'])
    portfolio['Date'] = price['Date']
    portfolio['Cash'] = start_val*1.0
    portfolio['portval'] = 0.0

    inv = {}
    for i, row in price.iterrows():
        today = row['Date']
        prev_cash = start_val if i==0 else portfolio.at[i-1, 'Cash']
        if not trades.empty and today in trades.Date.values:
            today_trades = trades[trades['Date'] == today]
            for j, trade in today_trades.iterrows():
                stock = trade['Symbol']
                if trade['Order'] == 'BUY':
                    portfolio.at[i, 'Cash'] = prev_cash - trade['Shares']*row[stock]
                    portfolio.at[i, 'Cash'] -= commission
                    portfolio.at[i, 'Cash'] -= impact*trade['Shares']*row[stock]
                    prev_cash = portfolio.at[i, 'Cash']
                    inv[stock] = inv.get(stock, 0) + trade['Shares']
                elif trade['Order'] == 'SELL':
                    portfolio.at[i, 'Cash'] = prev_cash + trade['Shares']*row[stock]
                    portfolio.at[i, 'Cash'] -= commission
                    portfolio.at[i, 'Cash'] -= impact*trade['Shares']*row[stock]
                    prev_cash = portfolio.at[i, 'Cash']
                    inv[stock] = inv.get(stock, 0) - trade['Shares']
                else:
                    portfolio.at[i, 'Cash'] = prev_cash   
        else:
            portfolio.at[i, 'Cash'] = prev_cash
            
        portfolio.at[i, 'portval'] = prev_cash
        for stock, shares in inv.items():
            portfolio.at[i, 'portval'] += shares * row[stock]
    portfolio.set_index('Date', inplace=True)  
    
    port_stand = pd.DataFrame(portfolio['portval']/start_val)
    return port_stand
  	   		  		 		  		  		    	 		 		   		 		  
def test_code():  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    Helper function to test code  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    # this is a helper function you can use to test your code  		  	   		  		 		  		  		    	 		 		   		 		  
    # note that during autograding his function will not be called.  		  	   		  		 		  		  		    	 		 		   		 		  
    # Define input parameters  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
    of = "./orders/orders2.csv"  		  	   		  		 		  		  		    	 		 		   		 		  
    sv = 1000000  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
    # Process orders  		  	   		  		 		  		  		    	 		 		   		 		  
    portvals = compute_portvals(orders_file=of, start_val=sv)  		  	   		  		 		  		  		    	 		 		   		 		  
    if isinstance(portvals, pd.DataFrame):  		  	   		  		 		  		  		    	 		 		   		 		  
        portvals = portvals[portvals.columns[0]]  # just get the first column  		  	   		  		 		  		  		    	 		 		   		 		  
    else:  		  	   		  		 		  		  		    	 		 		   		 		  
        "warning, code did not return a DataFrame"  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
    # Get portfolio stats  		  	   		  		 		  		  		    	 		 		   		 		  
    # Here we just fake the data. you should use your code from previous assignments.  		  	   		  		 		  		  		    	 		 		   		 		  
    start_date = dt.datetime(2008, 1, 1)  		  	   		  		 		  		  		    	 		 		   		 		  
    end_date = dt.datetime(2008, 6, 1)  		  	   		  		 		  		  		    	 		 		   		 		  
    cum_ret, avg_daily_ret, std_daily_ret, sharpe_ratio = [  		  	   		  		 		  		  		    	 		 		   		 		  
        0.2,  		  	   		  		 		  		  		    	 		 		   		 		  
        0.01,  		  	   		  		 		  		  		    	 		 		   		 		  
        0.02,  		  	   		  		 		  		  		    	 		 		   		 		  
        1.5,  		  	   		  		 		  		  		    	 		 		   		 		  
    ]  		  	   		  		 		  		  		    	 		 		   		 		  
    cum_ret_SPY, avg_daily_ret_SPY, std_daily_ret_SPY, sharpe_ratio_SPY = [  		  	   		  		 		  		  		    	 		 		   		 		  
        0.2,  		  	   		  		 		  		  		    	 		 		   		 		  
        0.01,  		  	   		  		 		  		  		    	 		 		   		 		  
        0.02,  		  	   		  		 		  		  		    	 		 		   		 		  
        1.5,  		  	   		  		 		  		  		    	 		 		   		 		  
    ]  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
    # Compare portfolio against $SPX  		  	   		  		 		  		  		    	 		 		   		 		  
    print(f"Date Range: {start_date} to {end_date}")  		  	   		  		 		  		  		    	 		 		   		 		  
    print()  		  	   		  		 		  		  		    	 		 		   		 		  
    print(f"Sharpe Ratio of Fund: {sharpe_ratio}")  		  	   		  		 		  		  		    	 		 		   		 		  
    print(f"Sharpe Ratio of SPY : {sharpe_ratio_SPY}")  		  	   		  		 		  		  		    	 		 		   		 		  
    print()  		  	   		  		 		  		  		    	 		 		   		 		  
    print(f"Cumulative Return of Fund: {cum_ret}")  		  	   		  		 		  		  		    	 		 		   		 		  
    print(f"Cumulative Return of SPY : {cum_ret_SPY}")  		  	   		  		 		  		  		    	 		 		   		 		  
    print()  		  	   		  		 		  		  		    	 		 		   		 		  
    print(f"Standard Deviation of Fund: {std_daily_ret}")  		  	   		  		 		  		  		    	 		 		   		 		  
    print(f"Standard Deviation of SPY : {std_daily_ret_SPY}")  		  	   		  		 		  		  		    	 		 		   		 		  
    print()  		  	   		  		 		  		  		    	 		 		   		 		  
    print(f"Average Daily Return of Fund: {avg_daily_ret}")  		  	   		  		 		  		  		    	 		 		   		 		  
    print(f"Average Daily Return of SPY : {avg_daily_ret_SPY}")  		  	   		  		 		  		  		    	 		 		   		 		  
    print()  		  	   		  		 		  		  		    	 		 		   		 		  
    print(f"Final Portfolio Value: {portvals[-1]}")  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
if __name__ == "__main__":  		  	   		  		 		  		  		    	 		 		   		 		  
    test_code()  		  	   		  		 		  		  		    	 		 		   		 		  




#Hint, use code like this to read in the orders file: 
'''
orders_df = pandas.read_csv(orders_file, index_col=’Date’, parse_dates=True, na_values=[‘nan’]) 
'''
#In terms of execution prices, you should assume you get the adjusted close price for the day of the trade. 