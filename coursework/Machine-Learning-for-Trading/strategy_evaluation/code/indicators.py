from util import get_data, plot_data
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

def author(): 
  return 'ychen3281' 

#indicator functions
def calc_bbp(prices, lb_period=20, sd=dt.datetime(2008,1,1)):
    mean = prices.rolling(window=lb_period).mean()
    std = prices.rolling(window=lb_period).std()
    lower = mean + std*2
    upper = mean - std*2
    pct_band = 100 * ((prices-lower)/(upper-lower))
    pct_band = pct_band.rename(columns={'JPM': 'BBP'})
    pct_band = pct_band[pct_band.index >= sd]
    return pct_band

def calc_rsi(prices, lb_period=14, sd=dt.datetime(2008,1,1)):
    diff = prices.diff()
    up = diff.where(diff > 0, 0)
    down = diff.where(diff < 0, 0)
    avg_up = up.rolling(window=lb_period).mean()
    avg_down = down.rolling(window=lb_period).mean().abs()
    rsi = 100 * avg_up/(avg_up+avg_down)
    rsi = rsi.rename(columns={'JPM': 'RSI'})
    rsi = rsi[rsi.index >= sd]
    return rsi

def calc_momentum(prices, period=20, sd=dt.datetime(2008,1,1)):
    momentum = (prices/prices.shift(period-1)) -1
    momentum = momentum.rename(columns={'JPM': 'Momentum'})
    momentum = momentum[momentum.index >= sd]
    return momentum

def calc_ema(prices, lb_period=20, sd=dt.datetime(2008,1,1)):
    ema = prices.ewm(span=lb_period, adjust=False).mean()
    ema = ema.rename(columns={'JPM': 'EMA'})
    ema = ema[ema.index >= sd]
    return ema

def calc_macd(prices, short_lb=12, long_lb=26, sig_period=9, sd=dt.datetime(2008,1,1)):
    short = calc_ema(prices, short_lb)
    long = calc_ema(prices, long_lb)
    macd = short-long
    macd_sig = calc_ema(macd,sig_period)
    macd = macd.rename(columns={'EMA': 'MACD'})
    macd = macd[macd.index >= sd]
    macd_sig = macd_sig.rename(columns={'EMA': 'Signal'})
    macd_sig = macd_sig[macd_sig.index >= sd]
    return macd, macd_sig

#plot functions

def bbp_plot(bbp_vals):
    plt.figure(figsize=(20, 6))
    plt.plot(bbp_vals.index, bbp_vals, label='BBP', color='blue')
    plt.axhline(0, color='purple', linestyle='--', label='Lower Band')
    plt.axhline(100, color='r', linestyle='--', label='Upper Band')
    plt.fill_between(bbp_vals.index, 0, 100, color='lightgrey', alpha=0.3) 
    plt.grid()
    plt.margins(x=0.002) 
    plt.xlabel('Date')
    plt.ylabel('BBP%')
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=1))  
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%b %Y")) 
    plt.xticks(rotation=30)
    plt.title('BBP - Bollinger Band Percentage')
    plt.legend()
    return plt.savefig('BBP.png')

def rsi_plot(rsi_vals):
    plt.figure(figsize=(20, 6))
    plt.plot(rsi_vals.index, rsi_vals, label='RSI', color='blue')
    plt.axhline(70, color='r', linestyle='--', label='Overbought')
    plt.axhline(30, color='g', linestyle='--', label='Oversold')
    plt.fill_between(rsi_vals.index, 30, 70, color='lightgrey', alpha=0.3) 
    plt.fill_between(rsi_vals.index, rsi_vals['RSI'], 30, where=rsi_vals['RSI'] < 30, color='green', alpha=0.5, label='Buy Signal')
    plt.fill_between(rsi_vals.index, rsi_vals['RSI'], 70, where=rsi_vals['RSI'] > 70, color='red', alpha=0.5, label='Sell Signal')
    plt.grid()
    plt.margins(x=0.002) 
    plt.xlabel('Date')
    plt.ylabel('RSI')
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=1))  
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%b %Y")) 
    plt.xticks(rotation=30)
    plt.title('RSI - Relative Strength Index (14 day)')
    plt.legend()
    return plt.savefig('RSI.png')

def mom_plot(mom_vals):
    plt.figure(figsize=(20, 6))
    plt.plot(mom_vals.index, mom_vals, label='Momentum', color='blue')
    plt.axhline(0, color='purple', linestyle='--')
    plt.fill_between(mom_vals.index, mom_vals['Momentum'], 0, where=mom_vals['Momentum'] < 0, color='red', alpha=0.5, label='Sell Signal')
    plt.fill_between(mom_vals.index, mom_vals['Momentum'], 0, where=mom_vals['Momentum'] > 0, color='green', alpha=0.5, label='Buy Signal')
    plt.grid()
    plt.margins(x=0.002) 
    plt.xlabel('Date')
    plt.ylabel('Momentum')
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=1))  
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%b %Y")) 
    plt.xticks(rotation=30)
    plt.title('Momentum (20 day)')
    plt.legend()
    return plt.savefig('Momentum.png')

def ema_plot(prices, ema_vals, sd=dt.datetime(2008,1,1)):
    adj_price = prices[prices.index >= sd]
    plt.figure(figsize=(20, 6))
    plt.plot(ema_vals.index, ema_vals, label='EMA', color='blue')
    plt.plot(adj_price.index, adj_price, label='Prices', color='black')
    plt.fill_between(ema_vals.index, ema_vals['EMA'], adj_price['JPM'], where=(ema_vals['EMA'] < adj_price['JPM']), color='green', alpha=0.5, label='Bullish')
    plt.fill_between(ema_vals.index, ema_vals['EMA'], adj_price['JPM'], where=(ema_vals['EMA'] >= adj_price['JPM']), color='red', alpha=0.5, label='Bearish')
    plt.grid()
    plt.margins(x=0.002) 
    plt.xlabel('Date')
    plt.ylabel('Exponential Moving Average')
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=1))  
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%b %Y")) 
    plt.xticks(rotation=30)
    plt.title('EMA - Exponential Moving Average (20 day)')
    plt.legend()
    return plt.savefig('EMA.png')

def macd_plot(macd_vals, sig_vals, sd=dt.datetime(2008,1,1)):
    hist = macd_vals['MACD'] - sig_vals['Signal']
    plt.figure(figsize=(20, 6))
    plt.plot(macd_vals.index, macd_vals, label='MACD', color='blue')
    plt.plot(sig_vals.index, sig_vals, label='Signal', color='black')
    plt.bar(hist.index, hist, width=1.5, color='purple', alpha=0.5, label='MACD Histogram')
    plt.fill_between(macd_vals.index, macd_vals['MACD'], sig_vals['Signal'], where=(macd_vals['MACD'] < sig_vals['Signal']), color='red', alpha=0.5, label='Sell Signal')
    plt.fill_between(macd_vals.index, macd_vals['MACD'], sig_vals['Signal'], where=(macd_vals['MACD'] >= sig_vals['Signal']), color='green', alpha=0.5, label='Buy Signal')

    plt.grid()
    plt.margins(x=0.002) 
    plt.xlabel('Date')
    plt.ylabel('MACD')
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=1))  
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%b %Y")) 
    plt.xticks(rotation=30)
    plt.title('MACD - Moving Average Convergence/Divergence indicator (12,26,9)')
    plt.legend()
    return plt.savefig('MACD.png')