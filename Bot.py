import json
import random
import requests
from norm import TextNormalizer, WordExtractor, ApplyStemmer
import pickle

stress = ['Everything will be fine', "I’m here for you", 'Stay well', 'Please be careful and stay safe', 'Cheer up', 'Lighten up', "Whenever I’m feeling down, I buy myself a cake",
          "Never look back", 'Enjoy every moment', 'Live for yourself', 'Life is beautiful']
not_stress = ['Super', 'Very good', "I'm happy for you", "You are great, this is good", "I can’t explain how happy I am for you"]

class CheatBotStress:
    def __init__(self, pipeline_path):
        self.token = '1921692631:AAE6Cb3z4kV-4URkddthNnGE3-dOohl9Azw'
        self.url = f"https://api.telegram.org/bot{self.token}"
        self.pipe = pickle.load(open('PIPE.PKL', 'rb'))

    def get_updates(self, offset):
        url = self.url + "/getUpdates?timeout=100"
        if offset:
            url = url + f"&offset={offset+1}"
        url_info = requests.get(url)
        return json.loads(url_info.content)

    def send_message(self, msg, chat_id):
        url = self.url + f'/sendMessage?chat_id={chat_id}&text={msg}'
        if msg is not None:
            requests.get(url)

    def verify_msg(self, msg, chat_id):
        predicion = self.pipe.predict([msg])
        if predicion[0] == 1:
            response = random.choice(stress)
            self.send_message(response, chat_id)
        else:
            response = random.choice(not_stress)
            self.send_message(response, chat_id)