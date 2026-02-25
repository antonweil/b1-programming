import os
from typing import List, Optional, Dict
import json
from fastapi import APIRouter, HTTPException, Query, Response, status


class UserStore:
    def __init__(self, filepath):
        self.filepath = filepath
        self._users: List[Dict] = self.load()

    def __iter__(self):
        return iter(self._users)

    def load(self):
        if not os.path.exists(self.filepath):
            return []
        users = []
        with open(self.filepath, "r") as f:
            for line in f:
                clean_line = line.strip()
                if clean_line:
                    users.append(json.loads(clean_line))
            return users

    def save(self, users: list):
        with open(self.filepath, "w") as f:
            for entry in self:
                line = json.dumps(entry)
                f.write(line + "\n")
        self._users = users

    def find_by_id(self, user_id):
        #searches the user_db for u via next search
        self.load()
        user = next((u for u in self._users if u["id"] == user_id), None)
        print(user)
        return user
    
    def update_user(self, user_id, updated_data:dict):
        users = self.load()
        index = next((i for i, u in enumerate(users) if u["id"] == user_id), None)
        if index is None:
            return None
        users[index].update(updated_data)
        self.save(users)
        return users[index]
        
    def delete_user(self, user_id):
        users = self.load()
        original_count = len(users)
        updated_users = [u for u in users if u["id"] != user_id]
        if len(updated_users) == original_count:
            return False
        self.save(updated_users)
        return True
