from fastapi import FastAPI
import uvicorn


app = FastAPI(title="Recipe API")

# GET, POST, UPDATE, DELETE --> CRUD (Create, read, update and delete) OPERATIONS 
@app.get('/')
def home():
    return "API is working"

if __name__ == "main":
    uvicorn.run(app, host="127.0.0.1", port=8000)