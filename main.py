from Bot import CheatBotStress
from norm import TextNormalizer, WordExtractor, ApplyStemmer
Bot = CheatBotStress("Salut")
update_id = None
while True:
    updates = Bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = item["message"]["text"]
            except:
                message = None
            if message:
                chat_id = item["message"]["chat"]["id"]
                Bot.verify_msg(message, chat_id)