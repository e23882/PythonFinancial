#pip install pymongo==3.4.0
import pymongo 

myclient = pymongo.MongoClient("mongodb://rr114.ddns.net:27017/?connectTimeoutMS=30000&maxIdleTimeMS=600000")
mydb = myclient["StockDB"]
mycol = mydb["StockData"]
 
print(mycol.find_one())