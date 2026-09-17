import json
import os

HISTORY_FILE = "data/chat_history/chat.json"

def load_chat_history():
    if not os.path.exists(HISTORY_FILE):
        return []
    
    with open(HISTORY_FILE, "r", encoding="utf-8") as file:
        return json.load(file)
    
def save_chat_history(chat_history):
    os.makedirs(
        os.path.dirname(HISTORY_FILE), exist_ok=True
    )
    with open(HISTORY_FILE,"w", encoding="utf-8") as file:
        json.dump(chat_history, file, indent=4, ensure_ascii=False)
    
    