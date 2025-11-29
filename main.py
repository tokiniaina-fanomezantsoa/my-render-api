from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API Python OK"}

@app.post("/execute")
def execute(data: dict):
    text = data.get("text", "")
    return {"output": text.upper()}
