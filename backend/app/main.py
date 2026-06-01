from fastapi import FastAPI
from app.vaild import MessageCreate
from fastapi.middleware.cors import CORSMiddleware
from app.db import Base, SessionLocal
from fastapi import Depends
from app.db import engine
from sqlalchemy.orm import Session
from app.models import Message


Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#  Example: CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5173"],  # frontend dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/Hello_msg")
async def Msg(msg:MessageCreate):
     return {"Hello": msg.name, "Message": msg.msg}

@app.post("/messages/")
def create_message(message:MessageCreate, db: Session = Depends(get_db)):
    db_message = Message(name=message.name, msg=message.msg)
    db.add(db_message)
    db.commit()

@app.get("/messages/")
def read_messages(db: Session = Depends(get_db)):
    return db.query(Message).all()
