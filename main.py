from fastapi import FastAPI
from handlers import router as handlers_router
from middlewares import add_middlewares

app = FastAPI()

app.include_router(handlers_router)
add_middlewares(app)

@app.get("/")
async def root():
    return {"message": "Hello, World!"}
