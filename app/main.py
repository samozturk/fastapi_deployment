# pylint: disable=missing-module-docstring, no-else-return, line-too-long
#!/usr/bin/python3
import os

from pydantic.main import BaseModel
import uvicorn
import joblib
import numpy as np
from fastapi import FastAPI


app = FastAPI(title='My ML App')


@app.get("/")
def home() -> str:
    '''Homepage function.

    Returns:
        [dict]: A dictionary(JSON) shows services status.
    '''
    return "Working."
class My_Data(BaseModel):
    X: int

@app.post("/predict")
def predict(data:My_Data):
    my_model = joblib.load('app/my_model')
    X = np.array(data.X).reshape(-1, 1)
    return str(my_model.predict(X))

@app.get("/check")
def check():
    return os.listdir()
# Endpoint
if __name__ == "__main__":
    # Changed it from app to 'main:app' to reload changes automatically.
    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=True)
