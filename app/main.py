from fastapi import FastAPI
from database import engine
from models import Base
from routes import password
from uvicorn import run

# Initialize DB
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include routes
app.include_router(password.router)

if __name__ == "__main__":
    run("main:app", host="0.0.0.0", port=7878, reload=True)



