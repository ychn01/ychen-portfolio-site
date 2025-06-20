import TheoreticallyOptimalStrategy as tos  
import marketsimcode as msc
import indicators as ind
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
from util import get_data, plot_data  

def author():
    return "ychen3281"

if __name__ == "__main__":
    ### Part 1 TOS
    #generate data from TOS
    df_trades = tos.testPolicy(symbol = "JPM", sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009,12,31), sv = 100000)  
    bm_df = tos.benchmark(symbol = "JPM", sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009,12,31), sv = 100000) 
    jpm = tos.trades(symbol = "JPM", sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009,12,31), sv = 100000)

    #plot TOS vs benchmark
    benchmark = msc.compute_portvals(bm_df, start_val=100000, commission=0, impact=0)
    jpm_df = msc.compute_portvals(jpm, start_val=100000, commission=0, impact=0)
    jpm_df.rename(columns={'portval': 'TOS'}, inplace=True)
    benchmark.rename(columns={'portval': 'Benchmark'}, inplace=True)
    jpm = jpm_df.plot(color='red', label='TOS')
    benchmark.plot(color='purple', label='Benchmark', ax=jpm)
    plt.title("TOS vs Benchmark Portfolio")
    plt.xlabel("Date")
    plt.ylabel("Normalized Portfolio Value")
    plt.grid(True)
    plt.margins(x=0)
    plt.savefig('TOS.png')
    
    #create table of returns 
    def return_vals(port_val):
        dr = ((port_val/port_val.shift(1)) - 1)[1:]
        adr = round(dr.mean(),6)
        cr = round((port_val.iloc[-1]/port_val.iloc[0])-1,6)
        sddr = round(dr.std(), 6)
        df = pd.DataFrame({
            'Cumulative Return': cr,
            'Standard Deviation of Daily Return': sddr,
            'Average Daily Return': adr
        })
        df = df.reset_index(drop=True)
        return df
    bench_vals = pd.DataFrame(return_vals(benchmark))
    bench_vals['Returns'] = 'Benchmark'
    port_vals = pd.DataFrame((return_vals(jpm_df)))
    port_vals['Returns'] = 'Portfolio'

    combined_df = pd.concat([bench_vals, port_vals])
    combined_df.set_index('Returns', inplace=True)
    print(combined_df)
    
    ### Part 2 Indicators
    #generate date range prices
    sd = dt.datetime(2008,1,1)
    ed = dt.datetime(2009,12,31)
    lookback_pd = sd - dt.timedelta(days=50)
    dates = pd.date_range(lookback_pd, ed)
    syms = ['JPM']
    prices_all = get_data(syms, dates)
    prices = prices_all[syms]
    prices.fillna(method ='ffill',inplace=True)
    prices.fillna(method ='bfill',inplace=True)
    prices_SPY = prices_all["SPY"] 

    # normalized prices
    syms_normed = prices/prices.iloc[0]
    spy_normed = prices_SPY/prices_SPY.iloc[0]
    
    #generate indicator data
    bbp_vals = ind.calc_bbp(prices)
    ema_vals = ind.calc_ema(prices)
    mom_vals = ind.calc_momentum(prices)
    rsi_vals = ind.calc_rsi(prices)
    macd_vals, sig_vals = ind.calc_macd(prices)
    
    #plot using the data
    ind.bbp_plot(bbp_vals)
    ind.ema_plot(prices, ema_vals)
    ind.mom_plot(mom_vals)
    ind.rsi_plot(rsi_vals)
    ind.macd_plot(macd_vals, sig_vals)