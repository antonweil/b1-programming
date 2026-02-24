from fastapi import FastAPI
from routes import users
#imports from fastapi and the routes folder

#creates the FastAPI app, with title desc and version
app = FastAPI(
    title = "User Management API",
    description = "FastAPI Backend for managing users",
    version = "1.0.0"
)

#attach users.py to website
app.include_router(users.router, prefix="/users", tags=["Users"])

#defines general health check function
@app.get("/")
def health_check():
    return {"status":"healthy", "message":"API is running"}

#how to run from proper week13 directory
#uvicorn main:app --reload