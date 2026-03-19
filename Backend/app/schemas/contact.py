from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional
from datetime import datetime

class ContactCreate(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None
    service: str
    message: str

class ContactResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: Optional[str] = None
    service: str
    message: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
