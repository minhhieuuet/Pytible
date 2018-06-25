import requests
import os
class ChatfuelAPI():
    def sendText(senderId,msg):
        r = requests.post('https://api.chatfuel.com/bots/'+os.getenv('BOT_ID')+'/users/'+str(senderId)+'/send?chatfuel_token='+os.getenv('CHATFUEL_TOKEN')+'&chatfuel_block_id='+os.getenv('CHATFUEL_BLOCK_TEXT'), json={"repmsg": msg})        
        return str(r.status_code)

    def sendImage(senderId,msg):
        r = requests.post('https://api.chatfuel.com/bots/'+os.getenv('BOT_ID')+'/users/'+str(senderId)+'/send?chatfuel_token='+os.getenv('CHATFUEL_TOKEN')+'&chatfuel_block_id='+os.getenv('CHATFUEL_BLOCK_IMAGE'), json={"urlImage": msg})   
        return str(r.status_code)

    def sendChangeFavorite(senderId):
        r = requests.post('https://api.chatfuel.com/bots/'+os.getenv('BOT_ID')+'/users/'+str(senderId)+'/send?chatfuel_token='+os.getenv('CHATFUEL_TOKEN')+'&chatfuel_block_id='+os.getenv('CHATFUEL_BLOCK_SELECTFAV'))     
        return str(r.status_code)
    
    def sendVoice(senderId,msg):
        r = requests.post('https://api.chatfuel.com/bots/'+os.getenv('BOT_ID')+'/users/'+str(senderId)+'/send?chatfuel_token='+os.getenv('CHATFUEL_TOKEN')+'&chatfuel_block_id='+os.getenv('CHATFUEL_BLOCK_VOICE'), json={"urlVoice": msg})
        return str(r.status_code)
