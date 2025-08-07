from fastapi import FastAPI
from app.routes import customers
from app.database import engine
from app.models import Base

app = FastAPI(title="Vdoshack Video Rental API")

Base.metadata.create_all(bind=engine)

# Routers
app.include_router(customers.router, prefix="/customers", tags=["Customers"])

@app.get("/")
def root():
    return {"message": "Welcome to Vdoshack API"}
