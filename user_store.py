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

    def save(self):
        with open(self.filepath, "w") as f:
            for entry in self:
                line = json.dumps(entry)
                f.write(line + "\n")

    def find_by_id(self, id):
        #searches the user_db for u via next search
        user = next((u for u in self._users if u["id"] == id), None)
        return user