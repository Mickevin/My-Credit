import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib





# Description of the API
description = """
This is your app description, written in markdown code 

# This is a title 

* This is a bullet point

"""

# Tags for documentation
tag_metadata = [{
    "name": "Predict",
    "description": "Operations with GET methods. ",
    },
    {"name": "POST",
    "description": "Operations with POST methods. ",
    }]

# Create the app
app = FastAPI(title= "My First API",description=description,openapi_tags=tag_metadata)


# Create a first endpoint
@app.get("/", tags=['Predict'])
def index():
    return "Hello World"


# Create a GET endpoint
@app.get("/user_name", tags=['Test'])
def user_name(name:str='Joe'):
    return "Bonjour " + name

# Create a GET endpoint
@app.get("/square", tags=['Test'])
def square(number:int=0):
    message = {
        'Text' : "La valeur au carré de " + str(number) + " est " + str(number*number),
        "Value" : number*number
    }
    return message

class Predict(BaseModel):
    age	        : int
    job	        : int
    marital	    : int
    education	: int
    default	    : int
    balance	    : int
    housing	    : int
    loan	    : int
    contact	    : int
    day	        : int
    month	    : int
    duration    : int	
    campaign    : int	
    pdays	    : int
    previous    : int	
    poutcome    : int	


@app.post("/predict")
def predict(predict:Predict):
    print(predict.age)
    sc = joblib.load(open('scaler.pkl', 'rb'))
    model = joblib.load(open('model-xg.pkl', 'rb'))

    return str(model.predict(sc.transform([[
        int(predict.age), 
        int(predict.job),
        int(predict.marital),
        int(predict.education),
        int(predict.default),
        int(predict.balance),
        int(predict.housing),
        int(predict.loan),
        int(predict.contact),
        int(predict.day),
        int(predict.month),
        int(predict.duration),
        int(predict.campaign),
        int(predict.pdays),
        int(predict.previous),
        int(predict.poutcome)]
        ]))[0])


# Create a base model
class Article(BaseModel):
    title: str
    content: str
    author: str


# Create a POST endpoint
@app.post("/article", tags=['POST', 'Test'])
def create_article(article: Article):
    df = pd.read_csv('articles.csv')

    data_article = {
        'id': len(df) +1,
        "title": article.title,
        "content": article.content,
        "author": article.author
    }

    data = pd.DataFrame(data_article, index=[0])

    df = pd.concat([df, data], ignore_index=True)
    df.to_csv('articles.csv', index=False)
    return df.to_json()


# Create a first endpoint
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=4000)