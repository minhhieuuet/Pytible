import app
from urllib.parse import urlparse
from ChatfuelAPI import ChatfuelAPI
import random

def isFacebookMessage(url):
    o = urlparse(url)
    if o.scheme != 'https': 
        return False
    if ('fbcdn.net' in o.hostname) and (o.path.endswith('.png') or o.path.endswith('.jpg') or o.path.endswith('.jpeg') or o.path.endswith('.gif')):
        return True
    return False

def handleUser(senderId,timestamp,message,name,profile_pic,gender):
        usersCollection = app.mongo.db.Users
        result = usersCollection.find_one({'_id':int(senderId)})
        print(result)
        if result is None:
            usersCollection.insert_one({ "_id": int(senderId), "idCouple":None, "status": 1, "favorite":'any' , "timestamp": timestamp, "name": name, "gender": gender, "profile_pic": profile_pic})
            handleMessage(senderId,"Chờ 1 chút nhaaa :D Đang tìm bạn cho bạn nèee","text")
            startSession()
        else:
            status = result['status']
            if(status==0):
                usersCollection.update_one({"_id":int(senderId)},{"$set":{"status":1,"timestamp":timestamp}})
                handleMessage(senderId,"Đang tìm bạn cho bạn nèee","text")
                startSession()
            if(status==1):
                handleMessage(senderId,"Bình tĩnh nào D:","text")
            if(status==2):
                partnerId = result['idCouple']
                if(isFacebookMessage(message)):
                    handleMessage(senderId,"Hiện tại thì chúng mình chưa hoàn thành được cái send hình thông cảm nhaa","text")
                    handleMessage(partnerId,"Bạn của bạn vừa send 1 hình nhưng mà chúng mình kh chuyển qua cho bạn được :< Rất xin lỗi trong lần thử nghiệm nhéee","text")
                else:
                    if(message.lower()=="pp"):
                        baibai(senderId,partnerId)
                    else:
                        handleMessage(partnerId,message,"text")

def handleMessage(senderId,msg,type):
    if(type=="text"):
        ChatfuelAPI.sendText(senderId,msg)

def startSession():
    usersCollection = app.mongo.db.Users
    result = list(usersCollection.find({"status":1}).sort("timestamp",1))
    if(len(result)>1):
        user1=result[0]["_id"]
        user2 = user1
        while (user1 == user2):
            user2 = result[random.randint(0,len(result)-1)]["_id"]
        usersCollection.update_one({"_id":int(user1)},{"$set":{"status":2,"timestamp":None,"idCouple":user2}})
        usersCollection.update_one({"_id":int(user2)},{"$set":{"status":2,"timestamp":None,"idCouple":user1}})
        handleMessage(user1,"Hì tìm thấy bạn rùi thử chào nhau 1 câu xem nàoo","text")
        handleMessage(user2,"Hì tìm thấy bạn rùi thử chào nhau 1 câu xem nàoo","text")

def baibai(senderId,partnerId):
    usersCollection = app.mongo.db.Users
    usersCollection.update_one({"_id":int(senderId)},{"$set":{"status":0,"idCouple":None}})
    usersCollection.update_one({"_id":int(partnerId)},{"$set":{"status":0,"idCouple":None}})
    handleMessage(senderId,"Bạn đã kết thúc cuộc trò chuyện này :(","text")
    handleMessage(partnerId,"Bạn kia đã kết thúc cuộc trò chuyện nfay :(","text")
