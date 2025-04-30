from fastapi import FastAPI
from routers import books, frontend
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.include_router(books.router, tags=["books"])
app.include_router(frontend.router)
app.mount("/static", StaticFiles(directory="app/static"), name="static")
