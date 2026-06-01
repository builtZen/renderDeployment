from pydantic import BaseModel

class MessageBase(BaseModel):
    name: str
    msg: str

class MessageCreate(MessageBase):
    pass

class Message(MessageBase):
    id: int

    class Config:
           from_attributes = True
