import uvicorn
from fastapi import FastAPI

#Create the app object
app=FastAPI()

# Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {"message":"Hello World"}

#Route with a single paramter, returns the paratmeter within a message
# Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/welcome')
def get_name(name : str):
    return {"Welcome to the page":f"{name}"}