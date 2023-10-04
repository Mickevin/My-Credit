from fastapi import FastAPI
import uvicorn

app = FastAPI(title= "My First API",)

@app.get('/square')
def square(n:str=None) -> str:
    if n == None:return "Please enter a number"
    else:return str(int(n)*int(n))

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)