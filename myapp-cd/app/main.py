# app/main.py
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
async def hello():
    return JSONResponse(content={"message": "hello from myapp", "env": "REPLACE_ENV"})

# For local run (optional)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
