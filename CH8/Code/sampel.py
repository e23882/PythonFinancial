import csv
import numpy as np
import pandas as pd
# 引用pylab > pip install matplotlib
from pylab import mpl, plt
plt.style.use('seaborn')
mpl.rcParams['font.family'] = 'serlf'

filename = 'D:\Data.csv'
f = open(filename, 'r')
#讀取檔案，確認是否有檔案
#print(f.readlines())

#透過padnas讀取csv到變數data
#data = pd.read_csv(filename,index_col=0, parse_dates=True)

#讀取檔案相關資訊
#print(data.info())

#讀取檔案前五筆
#print(data.head())

#讀取檔案最後五筆
#print(data.tail())

# 畫圖
#data.plot(figsize=(0,12), subplots=True)
#plt.show()

# https://www.geeksforgeeks.org/python-pandas-dataframe-mean/
# 取得統計資料 mean 欄位的平均值
#              std 標準差 
#              min 最小值
#              25% 常態分布25%值
#              50% .
#              70% .
#              max 最大值
#print(data.describe())


# 書224有例外，要在查一下原因
#data.aggregate(min, np.mean, np.std, np.median, max )

# 取得資料間變動
#data.diff().head().plot()
#plt.show()

# 取得資料間變動的平均值
#data.diff().mean().plot()
#plt.show()


# 取得欄位間的變動率
#data.pct_change().round(3).head()
# 取得欄位間的變動率平均值 畫圖
#data.pct_change().mean().plot()
#plt.show()

# https://cashflowrich.blogspot.com/2017/07/historical-volatilityhv.html
# 對數報酬率 取得歷史資料的變動程度
# 取得對數報酬率 
#rets = np.log(data/data.shift(1))
#rets.head().round(3)
#rets.cumsum().apply(np.exp).plot()
#plt.show()


# 再抽樣(降低抽樣頻率)
# 抽樣每周
#data.resample('1w', label='right').last().head()
#data.plot()
#plt.show()
# 抽樣每月
#data.resample('1m', label='right').last().head()
#data.plot()
#plt.show()











