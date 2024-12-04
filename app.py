import uvicorn
from fastapi import FastAPI
from BankNotes import BankNote
import pickle
import pandas as np

# Create the app object
app = FastAPI()
pickle_in = open("classifier.pkl","rb")
classifier = pickle.load(pickle_in)

# Index route
@app.get('/')
def index():
    return {"message":"Hello World"}

# Route with a single paramter, returns the paramter within a message
@app.get('/{name}')
def get_name(name : str):
    return {"message":f"Welcome to the page, {name}"}

# Expose the prediction functionality, make a prediction from the passed JSON
# data and return the predicted Bank Note with the confidence 

@app.post('/predict')
def predict_banknote(data : BankNote):
    data = data.dict()
    variance = data['variance']
    skewness = data['skewness']
    curtosis = data['curtosis']
    entropy = data['entropy']

    prediction = classifier.predict([[variance,skewness,curtosis,entropy]])

    if(prediction[0] > 0.5):
        prediction = "Fake Note"
    else:
        prediction = "It's a Bank Note"
    return{
        'prediction':prediction

    }