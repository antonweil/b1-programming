from fastapi import APIRouter, HTTPException, Query, Response, status
from typing import List, Optional
from schema import User, UserCreate, UserUpdate
import json
import os
#imports from fastAPI, typing, json, os as well as schema

user_file = "users.json"
router = APIRouter()
#create router to be accessed later

#will be used to load the data from users.txt to users.db
def load_data():
    if not os.path.exists(user_file):
        return []
    users = []
    with open(user_file, "r") as f:
        for line in f:
            clean_line = line.strip()
            if clean_line:
                users.append(json.loads(clean_line))
    return users

#will be used to save data into users.txt
def save_data(data):
    try:
        with open(user_file, "w") as f:
            for entry in data:
                line = json.dumps(entry)
            f.write(line + "\n")
    except Exception as e: 
        raise HTTPException(status_code=500, detail="Internal server error: Could not save data")

users_db = load_data()

def get_next_id():
    return len(users_db)+1

#POST API call, responds as User (which is UserBase+ID as objects), then defines create_user method, calling the UserCreate class
@router.post("/", response_model=User)
def create_user(user: UserCreate):
    #defines ID as the next in the sequence by checking length (starts with 1)
    #**user.model_dump() creates a new dict based on the input
    if any(u['email'] == new_user.email for u in users_db):
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = {"id": get_next_id(), **user.model_dump()}
    users_db.append(new_user)
    save_data(users_db)
    return new_user

#searches User by Name, returns all if no name is given
@router.get("/", response_model=List[User])
#uses query to look for the given name
def get_users(name: Optional[str] = Query(None, description="Search users by name")):
    if name:
        return [u for u in users_db if name.lower() in u["name"].lower()]
    return users_db

#requires id
@router.get("/{user_id}", response_model=User)
def get_user_by_id(id: int):
    #searches the user_db for u via next search
    user = next((u for u in users_db if u["id"] == id), None)
    if not user:
        #HTTP exception 404 if user isnt foung
        raise HTTPException(status_code=404, detail="User not found")
    return user

#Update User function, calls UserUpdate
@router.patch("/{user_id}", response_model=User)
def update_user(user_id: int, user_update: UserUpdate):
    #finds user based on index
    user_idx = next((i for i, u in enumerate(users_db) if u["id"] == user_id), None)
    #if not found, exception
    if user_idx is None:
        raise HTTPException(status_code=404, detail="User not found")
    #only update data that was changed at the index of the user in users_db
    stored_user_data = users_db[user_idx]
    update_data = user_update.model_dump(exclude_unset=True)
    updated_user = {**stored_user_data, **update_data}
    #set updated user to the position in users_db and returns it
    users_db[user_idx] = updated_user
    save_data(users_db)
    return updated_user

#delete function, works the same as update, but only checks if user exists
@router.delete("/{user_id}")
def delete_user(user_id: int):
    global users_db
    original_length = len(users_db)
    users_db = [u for u in users_db if u["id"] != user_id]
    if len(users_db) == original_length:
        raise HTTPException(status_code=404, detail="User not found")
    save_data(users_db)
    return {"message": "User deleted"}