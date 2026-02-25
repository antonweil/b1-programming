from fastapi import APIRouter, HTTPException, Query, Response, status
from typing import List, Optional
from schema import User, UserCreate, UserUpdate
import json
import os
from user_store import UserStore
#imports from fastAPI, typing, json, os as well as schema

user_file = "users.jsonl"
router = APIRouter()
#create router to be accessed later
store = UserStore("users.db")

def get_next_id():
    return len(store.load())+1

#POST API call, responds as User (which is UserBase+ID as objects), then defines create_user method, calling the UserCreate class
@router.post("/", response_model=User)

@router.post("/", response_model=User, status_code=201)
def create_user(user_in: UserCreate):
    result = store.save(user_in.model_dump())
    if result == "duplicate_email":
        raise HTTPException(
            status_code=400, 
            detail="A user with this email already exists."
        )
    if not result:
         raise HTTPException(status_code=500, detail="Error creating user")
    return result

#searches User by Name, returns all if no name is given
@router.get("/", response_model=List[User])
#uses query to look for the given name
def get_users(name: Optional[str] = Query(None, description="Search users by name")):
    if name:
        return store.load("WHERE name LIKE ?", (f"%{name}%",))
    return store.load()

#requires id
@router.get("/{user_id}", response_model=User)
def get_user_by_id(id: int):
    user = store.find_by_id(id)
    if not user:
        raise HTTPException(
            status_code=404, 
            detail=f"User with ID {id} not found"
        )
    return user

#Update User function, calls UserUpdate
@router.patch("/{user_id}", response_model=User)
def update_user(user_id: int, user_update: UserUpdate):
    update_data = user_update.model_dump(exclude_unset=True)
    updated_user = store.update_user(user_id, update_data)
    if not updated_user:
        raise HTTPException(
            status_code=404, 
            detail=f"User with ID {user_id} not found"
        )
    return updated_user

#delete function, works the same as update, but only checks if user exists
@router.delete("/{user_id}")
def delete_user(user_id: int):
    was_deleted = store.delete_user(user_id)
    if not was_deleted:
        raise HTTPException(
            status_code=404, 
            detail=f"User with ID {user_id} not found"
        )
    return Response(status_code=status.HTTP_204_NO_CONTENT)