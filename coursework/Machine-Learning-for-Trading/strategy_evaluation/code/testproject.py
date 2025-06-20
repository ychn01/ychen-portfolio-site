import datetime as dt  		  	   		  		 		  		  		    	 		 		   		 		  
import random  		  	   		  		 		  		  		    	 		 		   		 		  
import matplotlib.pyplot as plt  		  	   		  		 		  		  		    	 		 		   		 		  
import pandas as pd  		  	   		  		 		  		  		    	 		 		   		 		  
from util import get_data, plot_data  		  	   		  		 		  		  		    	 		 		   		 		    		  		 		 
import indicators as ind
import marketsimcode as msc	 	 
from ManualStrategy import ManualLearner

def author():
    return "ychen3281"

#benchmark
def benchmark_func(symbol="AAPL", sd=dt.datetime(2010, 1, 1), ed=dt.datetime(2011,12,31), sv = 100000):
    price = get_data([symbol], pd.date_range(sd, ed)).reset_index().rename(columns={'index': 'Date'})
    del price['SPY']
    price['Order'] = "HOLD"
    price.loc[0, 'Order'] = "BUY"
    price['Shares'] = 0
    price.loc[0, 'Shares'] = 1000

    bm_df = price.copy()
    bm_df["Symbol"] = symbol
    del bm_df[symbol]
    print(type(bm_df), bm_df)
    return bm_df

#manual strategy in-sample
bm_df = benchmark_func(symbol = "JPM", sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009,12,31), sv = 100000) 
jpm = ManualLearner.trades(symbol = "JPM", sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009,12,31), sv = 100000)

buy = jpm[jpm.apply(lambda row: "BUY" in row.values, axis=1)]
sell = jpm[jpm.apply(lambda row: "SELL" in row.values, axis=1)]


benchmark_1 = msc.compute_portvals(bm_df, start_val=100000, commission=9.95, impact=0.05)
jpm_df_1 = msc.compute_portvals(jpm, start_val=100000, commission=9.95, impact=0.005)
jpm_df_1.rename(columns={'portval': 'Manual Strategy'}, inplace=True)  
benchmark_1.rename(columns={'portval': 'Benchmark'}, inplace=True)
jpm_1 = jpm_df_1.plot(color='red', label='Manual Strategy')
benchmark_1.plot(color='purple', label='Benchmark', ax=jpm_1) 

for i, row in buy.iterrows():
    plt.axvline(x=i, color='blue', linestyle='--', label="Long entry point")
    
for i, row in sell.iterrows():
    plt.axvline(x=i, color='black', linestyle='--', label="Short entry point")
    
plt.title("Manual Strategy vs Benchmark Portfolio (in-sample)")
plt.xlabel("Date")
plt.ylabel("Normalized Portfolio Value")
plt.grid(True)
plt.margins(x=0)
plt.savefig('Manual Strategy in-sample.png')

#manual strategy out-of-sample
bm_df_2 = benchmark_func(symbol = "JPM", sd=dt.datetime(2010, 1, 1), ed=dt.datetime(2011,12,31), sv = 100000) 
jpm_2 = ManualLearner.trades(symbol = "JPM", sd=dt.datetime(2010, 1, 1), ed=dt.datetime(2011,12,31), sv = 100000)

buy_2 = jpm_2[jpm_2.apply(lambda row: "BUY" in row.values, axis=1)]
sell_2 = jpm_2[jpm_2.apply(lambda row: "SELL" in row.values, axis=1)]

benchmark_2 = msc.compute_portvals(bm_df_2, start_val=100000, commission=9.95, impact=0.005)
jpm_df_2 = msc.compute_portvals(jpm_2, start_val=100000, commission=9.95, impact=0.005)
jpm_df_2.rename(columns={'portval': 'Manual Strategy'}, inplace=True)
benchmark_2.rename(columns={'portval': 'Benchmark'}, inplace=True)

jpm_2 = jpm_df_2.plot(color='red', label='Manual Strategy')
benchmark_2.plot(color='purple', label='Benchmark', ax=jpm_2)

for i, row in buy_2.iterrows():
    plt.axvline(x=i, color='blue', linestyle='--', label="Long entry point")
    
for i, row in sell_2.iterrows():
    plt.axvline(x=i, color='black', linestyle='--', label="Short entry point")
    
plt.title("Manual Strategy vs Benchmark Portfolio (out-of-sample)")
plt.xlabel("Date")
plt.ylabel("Normalized Portfolio Value")
plt.grid(True)
plt.margins(x=0)
plt.savefig('Manual Strategy out-of-sample.png')

#table of benchmark vs manual in sample
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

bench_vals_in = pd.DataFrame(return_vals(benchmark_1))
bench_vals_in['Returns'] = 'Benchmark'
port_vals_in = pd.DataFrame((return_vals(jpm_df_1)))
port_vals_in['Returns'] = 'Portfolio'
combined_df_in = pd.concat([bench_vals_in, port_vals_in])
combined_df_in.set_index('Returns', inplace=True)
    
    
#table of benchmark vs manual out sample
bench_vals_out = pd.DataFrame(return_vals(benchmark_2))
bench_vals_out['Returns'] = 'Benchmark'
port_vals_out = pd.DataFrame((return_vals(jpm_df_2)))
port_vals_out['Returns'] = 'Portfolio'

combined_df_out = pd.concat([bench_vals_out, port_vals_out])
combined_df_out.set_index('Returns', inplace=True)