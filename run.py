from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel


class Square(BaseModel):
    age : int

app = FastAPI(title= "My First API",)

@app.post('/square')
def square(s:Square) -> str:
    if s.n == None:return "Please enter a number"
    else:return str(int(s.n)*int(s.n))

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)