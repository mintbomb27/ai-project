from pydantic import BaseModel, Field, EmailStr

class TicketModel(BaseModel):
    status: str = Field(...)
    description: EmailStr = Field(...)
    user: str = Field(...)
    status: str = Field(...)
    dept_assigned: str = Field(...)