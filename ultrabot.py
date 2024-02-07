import json
import requests

class ultraChatBot():    
    def __init__(self, json):
        self.json = json
        self.dict_messages = json['data']
        self.ultraAPIUrl = 'APIURL'
        self.token = 'TOKEN'

   
    def send_requests(self, type, data):
        url = f"{self.ultraAPIUrl}{type}?token={self.token}"
        headers = {'Content-type': 'application/json'}
        answer = requests.post(url, data=json.dumps(data), headers=headers)
        return answer.json()

    def send_message(self, chatID, text):
        data = {"to" : chatID,
                "body" : text}  
        answer = self.send_requests('messages/chat', data)
        return answer
    
    def send_image(self, chatID, image_url):
        data = {"to" : chatID,
                "image" : image_url}  
        answer = self.send_requests('messages/image', data)
        return answer

    def set_message(self,chatID,response):
        if "text" in response[0]:
            return self.send_message(chatID, response[0]["text"])
        elif "image" in response[0]:
            return self.send_image(chatID, response[0]["image"])
        else:
            return self.send_message(chatID, "response")


    def Processingـincomingـmessages(self):
        if self.dict_messages != []:
            message =self.dict_messages
            print(message)
            text = message['body'].split()
            message_type = message['type'].split()
            if not message['fromMe']:
                chatID  = message['from'] 
                url = "WEBHOOK"
                headers = {'Content-type': 'application/json'}
                print(20*"*")
                print(message_type)
                if(message_type[0] == "image"):
                    data = {"message":"/read_image"} 
                else:
                    data = {"message":text[0]} 
                response = requests.post(url, data=json.dumps(data), headers=headers)
                return self.set_message(chatID,response.json()) #answer.json()[0]["text"]
            else: return 'NoCommand'