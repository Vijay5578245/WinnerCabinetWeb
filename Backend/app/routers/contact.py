from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.database import get_db
from app.models import Contact
from app.schemas.contact import ContactCreate, ContactResponse
from app.services.email_service import notify_owner, send_confirmation


router = APIRouter(
    prefix="/contact",
    tags=["contact"],
)

@router.post("/")
async def create_contact(data: ContactCreate, background_tasks: BackgroundTasks, db: AsyncSession = Depends(get_db)):
    contact = Contact(**data.model_dump())
    db.add(contact)
    await db.commit()
    await db.refresh(contact)

    background_tasks.add_task(notify_owner, contact)
    background_tasks.add_task(send_confirmation, contact)

    return contact


@router.get("/", response_model=list[ContactResponse])
async def list_contacts(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Contact).order_by(Contact.created_at.desc()))
    contacts = result.scalars().all()
    return contacts
