from fastapi import FastAPI, APIRouter, HTTPException
import json

app = FastAPI()
router = APIRouter()

@router.get("/hello")
async def say_hello():
    return {"message": "Everything is working!"}

@router.get("/error")
async def trigger_error():
    # Testing HTTPException
    raise HTTPException(status_code=400, detail="This is a test error")

def add_user(id: int, name: str, age: int):
    user_data = {
        "id": id,
        "name": name,
        "age": age
    }
    
    # "a" means append: it adds to the end of the file without deleting old data
    with open("users.txt", "a") as file:
        # Convert dictionary to JSON string and add a newline character
        file.write(json.dumps(user_data) + "\n")

def get_users():
    users = []
    try:
        with open("users.txt", "r") as file:
            for line in file:
                # Convert each line back into a Python dictionary
                users.append(json.loads(line.strip()))
    except FileNotFoundError:
        return []
    return users

@router.post("/users")
async def create_user(user_id: int, name: str, age: int):
    user_entry = {"id": user_id, "name": name, "age": age}
    
    with open("users.txt", "a") as file:
        file.write(json.dumps(user_entry) + "\n")
        
    return {"message": "User added successfully", "user": user_entry}

# Example usage:
add_user(1, "Alice", 25)
add_user(2, "Bob", 30)

app.include_router(router)
