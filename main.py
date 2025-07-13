from fastapi import FastAPI
from api import router

app = FastAPI(
    title="Cannabis ROI Calculator",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
def root():
    return {"message": "Welcome to the Cannabis ROI API"}
