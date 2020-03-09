#pip install pymongo==3.4.0
import pymongo 
#pip install yahoo_fin
from yahoo_fin.stock_info import *


#Declarations
StockDataCollection = []



def AppendData(date, open, high, low, close, adjclose, volume, ticker):
    #StockDataCollection.append('{"Date":"'+str(date)+'", "High":"'+str(high)+'", "Low":"'+str(low)+'", "Close":"'+str(close)+'", "AdjClose":"'+str(adjclose)+'", "Volume":"'+str(volume)+'", "Ticker":"'+str(ticker)+'"}')
    myclient = pymongo.MongoClient("mongodb://leo:54088@rr114.ddns.net:27017/StockDB?connectTimeoutMS=30000&maxIdleTimeMS=600000&authMechanism=MONGODB-CR") 
    mydb = myclient["StockDB"]
    mycol = mydb["StockData"]   
    mydict = { "Date": date, "High": high, "Low": low, "Close":close, "AdjClose":adjclose, "Volume":volume, "Ticker":ticker }
    mycol.insert_one(mydict) 
    
def InsertData():
    myclient = pymongo.MongoClient("mongodb://leo:54088@rr114.ddns.net:27017/StockDB?connectTimeoutMS=30000&maxIdleTimeMS=600000&authMechanism=MONGODB-CR") 
    mydb = myclient["StockDB"]
    mycol = mydb["StockData"]    
    #x = mycol.insert_many(StockDataCollection)
    
    
def PrepareData():
    result = get_data('2330.TW')
    for index, row in result.iterrows():
        AppendData(index, row["open"], row["high"], row["low"], row["close"], row["adjclose"], row["volume"], row["ticker"])


PrepareData()
InsertData()