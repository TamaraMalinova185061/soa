from fastapi import FastAPI
from src.api import v1

app = FastAPI()
app.include_router(v1.router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, port=8000, host="0.0.0.0", reload=True)
