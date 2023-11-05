from fastapi import FastAPI, HTTPException,Request
import pickle
import requests
import pickle
import numpy as np
from fastapi.middleware.cors import CORSMiddleware  #
app = FastAPI()



classAnimal = {0:'Cat',1:'Dog'}

def predict_catOrDog(model,hog):
    brand = model.predict(np.array(hog).reshape(1,-1))
    return {'species':classAnimal[brand[0]]}

url = "http://172.17.0.2:80/api/gethog"
catDogModel = pickle.load(open(f'model/Cat_Dog_Model.pkl', 'rb'))


@app.get("/")
def root():
    return {"message": "This is my api"}

@app.post("/api/catOrDog")
async def read_str(request:Request):
    item = await request.json()
    hog = requests.get(url,json=item)
    res = predict_catOrDog(catDogModel,hog.json()['hog'])
    return res