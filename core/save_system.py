import json
import os

SAVE_FILE = "save/save1.json"

def load_game():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            return json.load(f)
    return {"player": {"map": "treehouse", "pos": [4, 4], "hp": 6}, "inventory": []}

def save_game(data):
    with open(SAVE_FILE, "w") as f:
        json.dump(data, f, indent=4)
