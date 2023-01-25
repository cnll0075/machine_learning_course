import uuid

import uvicorn
import inference
from fastapi import File
from fastapi import FastAPI
from fastapi import UploadFile
import numpy as np
from PIL import Image

app = FastAPI()


@app.get("/")
def ping():
    return 'pong'


@app.post("/predict")
def make_predictions(file: UploadFile = File(...)):
    image = np.array(Image.open(file.file))
    output = inference.predict(image)
    return output

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)