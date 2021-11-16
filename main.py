# pylint: disable=missing-module-docstring, no-else-return, line-too-long
#!/usr/bin/python3
import os
from dataclasses import dataclass

from typing import Optional
from typing import Dict, Any, AnyStr
from pydantic.main import BaseModel
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import joblib
import numpy as np


app = FastAPI(title='My App')


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
    my_model = joblib.load('my_model')
    X = np.array(data.X).reshape(-1, 1)
    return str(my_model.predict(X))

# Endpoint
if __name__ == "__main__":
    # Changed it from app to 'main:app' to reload changes automatically.
    uvicorn.run('main:app', host="127.0.0.1", port=8000, reload=True)
