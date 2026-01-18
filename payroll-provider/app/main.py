
from fastapi import FastAPI
from app.routers import payroll
from app.routers import health

app = FastAPI()
app.include_router(payroll.graphql_app, prefix="/graphql")
app.include_router(health.router, prefix="/health")

@app.get("/")
async def root():
    return {"This works"}
