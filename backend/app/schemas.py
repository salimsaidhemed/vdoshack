from pydantic import BaseModel

class CustomerCreate(BaseModel):
    full_name: str
    email: str
    phone: str | None = None

class Customer(CustomerCreate):
    id: int

    class Config:
        orm_mode = True
