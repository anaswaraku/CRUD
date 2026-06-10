from fastapi import FastAPI

app = FastAPI(title="A simple crud web app")

@app.get("/")
async def home():
    return "Hai this is a simple crud app!!!"