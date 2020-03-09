#pip install pymongo==3.4.0
import pymongo 



myclient = pymongo.MongoClient("mongodb://rr114.ddns.net:27017/?connectTimeoutMS=30000&maxIdleTimeMS=600000") 
mydb = myclient["StockDB"]
mycol = mydb["StockData"]

mylist = [
   { "name": "Taobao", "alexa": "100", "url": "https://www.taobao.com" },
   { "name": "QQ", "alexa": "101", "url": "https://www.qq.com" },
   { "name": "Facebook", "alexa": "10", "url": "https://www.facebook.com" },
   { "name": "知乎", "alexa": "103", "url": "https://www.zhihu.com" },
   { "name": "Github", "alexa": "109", "url": "https://www.github.com" }
]
x = mycol.insert_many(mylist)

#insert one
#mydict = { "name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com" }
#x = mycol.insert_one(mydict) 


print(x.inserted_ids)