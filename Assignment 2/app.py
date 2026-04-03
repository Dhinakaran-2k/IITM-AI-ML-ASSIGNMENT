from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_msg():
    return {
        "message": "Hello World This is my first API"
    }

@app.get("/data")
def get_data():
    return {
        "name": "Dhinakaran J",
        "Address":"NPCI HYD",
        "language": ["javascript", "c++", "python"]
    }