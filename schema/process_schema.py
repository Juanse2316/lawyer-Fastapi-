#python
from datetime import datetime, date
from typing import Optional

#pydantic
from pydantic import BaseModel, Field

class Process(BaseModel):
    id: Optional[int] 
    
    tittle: str = Field(
        ...,
        min_length= 1,
        max_length= 255,
        )
    description: str = Field(
        ...,
        min_length= 1,
        max_length= 255,
    ) 
    start_date: datetime = Field(default=datetime.now())
    update_at: Optional[datetime]= Field(default=None)
    finish_date: date= Field(...)
    status: bool = Field(default=True)
    user_id: int = Field(...)
    
