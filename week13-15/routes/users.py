from fastapi import APIRouter, HTTPException, Query, Response, status
from typing import List, Optional
#from schema import User, UserCreate, UserUpdate
from schema import User, UserCreate, UserUpdate
import json
import os
from user_store import UserStore
#imports from fastAPI, typing, json, os as well as schema

user_file = "users.json"
router = APIRouter()
#create router to be accessed later
store = UserStore("users.json")

def get_next_id():
    return len(store.load())+1

#POST API call, responds as User (which is UserBase+ID as objects), then defines create_user method, calling the UserCreate class
@router.post("/users", response_model=User)
def create_user(user: UserCreate):
    users = store.load()
    new_id = get_next_id()
    new_user = {"id": new_id, **user.model_dump()}
    users.append(new_user)
    store.save(users)
    return new_user

#searches User by Name, returns all if no name is given
@router.get("/users", response_model=List[User])
#uses query to look for the given name
def get_users(name: Optional[str] = Query(None, description="Search users by name")):
    users = store.load()
    if name:
        return [u for u in users if name.lower() in u["name"].lower()]
    return users

#requires id
@router.get("/{user_id}", response_model=User)
def get_user_by_id(id: int):
    user = store.find_by_id(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

#Update User function, calls UserUpdate
@router.patch("/{user_id}", response_model=User)
def update_user(user_id: int, user_update: UserUpdate):
    #finds user based on index
    users = store.load
    user_idx = next((i for i, u in enumerate(users) if u["id"] == user_id), None)
    #if not found, exception
    if user_idx is None:
        raise HTTPException(status_code=404, detail="User not found")
    stored_user_data = users[user_idx]
    update_data = user_update.model_dump(exclude_unset=True)
    updated_user = {**stored_user_data, **update_data}
    users[user_idx] = updated_user
    store.save(users)
    return updated_user

#delete function, works the same as update, but only checks if user exists
@router.delete("/{user_id}")
def delete_user(user_id: int):
    users = store.load()
    user = store.find_by_id(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    updated_users = [u for u in users if u["id"] != user_id]
    store.save(updated_users)
    return None