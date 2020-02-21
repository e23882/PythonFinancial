#pip install yahoo_fin
from yahoo_fin.stock_info import *

from pylab import mpl, plt
plt.style.use('seaborn')
mpl.rcParams['font.family'] = 'serlf'

#import pandas as pd
# get_analysts_info,
# get_balance_sheet,                                 
# get_cash_flow,                                 
# get_data,                                 
# get_day_gainers,                                 
# get_day_losers,                                 
# get_day_most_active,                                 
# get_holders,                                 
# get_income_statement,                                 
# get_live_price,                                 
# get_quote_table,                                 
# get_top_crypto,                                 
# get_stats,tickers_dow,                                 
# tickers_nasdaq,                
# tickers_other                 
# tickers_sp500
#https://finance.yahoo.com/lookup
result = get_data('2330.TW')
print(result)
result.plot()
plt.show()
#type(result)