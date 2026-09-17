import os
import json

CHAT_DIR = "data/chat_history"

def get_chat_sessions():
    os.makedirs(CHAT_DIR, exist_ok=True)
    sessions = []
    
    for filename in os.listdir(CHAT_DIR):
        if filename.endswith(".json"):
            sessions.append(filename[:-5])
    return sorted(sessions)

def create_chat_session(session_name):
    os.makedirs(CHAT_DIR, exist_ok=True)
    file_path = os.path.join(CHAT_DIR, f"{session_name}.json")
    
    if not os.path.exists(file_path):
        with open(file_path,"w",encoding="utf-8") as file:
            json.dump([],file,indent=4)
    return file_path

def load_session_history(session_name):
    file_path = os.path.join(CHAT_DIR, f"{session_name}.json")
    if not os.path.exists(file_path):
        return []
    with open(file_path,"r",encoding="utf-8") as file:
        return json.load(file)
    
def save_session_history(session_name, chat_history):
    os.makedirs(CHAT_DIR,exist_ok=True)
    file_path = os.path.join(CHAT_DIR,f"{session_name}.json")
    with open(file_path,"w", encoding="utf-8") as file:
        json.dump(chat_history, file, indent=4, ensure_ascii=False)