
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"income statement": "200k last month"}
