from sqlmodel import JSON, SQLModel, Field, Column
from typing import Optional, List

from beanie import Document
from pydantic import BaseModel


# class Event(BaseModel):
#     id: int
#     title: str
#     image: str
#     description: str
#     tags: List[str]
#     location: str

#     # 문서화할때 샘플데이터 보여줌 
#     class Config:
#         json_schema_extra = {
#             "example": {
#                 "title": "FastAPI Book Launch",
#                 "image": "https://linktomyimage.com/image.png",
#                 "description": "We will be discussing the contents of the FastAPI book in this event.Ensure to come with your own copy to win gifts!",
#                 "tags": ["python", "fastapi", "book", "launch"],
#                 "location": "Google Meet"
#             }
#         }

#=================================== SQLalchemy ======================================================================

# class Event(SQLModel, table=True):
#     id: int = Field(default=None, primary_key=True)
#     title: str
#     image: str
#     description: str
#     tags: List[str] = Field(sa_column=Column(JSON))
#     location: str

#     class Config:
#         arbitrary_types_allowed = True
#         json_schema_extra = {
#             "example": {
#                 "title": "FastAPI Book Launch",
#                 "image": "https://linktomyimage.com/image.png",
#                 "description": "We will be discussing the contents of the FastAPI book in this event. Ensure to come with your own copy to win gifts!",
#                 "tags": ["python", "fastapi", "book", "launch"],
#                 "location": "Google Meet"
#             }
#         }


# class EventUpdate(BaseModel):
#     title: Optional[str] = None  # 기본값 None 설정
#     image: Optional[str] = None  # 기본값 None 설정
#     description: Optional[str] = None  # 기본값 None 설정
#     tags: Optional[List[str]] = None  # 기본값 None 설정
#     location: Optional[str] = None  # 기본값 None 설정
    
#     class Config:
#         json_schema_extra = {
#             "example": {
#                 "title": "FastAPI BookLaunch",
#                 "image": "https://linktomyimage.com/image.png",
#                 "description": "We will be discussing the contents of the FastAPI book in this event.Ensure to come with your own copy to win gifts!",
#                 "tags": ["python", "fastapi", "book", "launch"],
#                 "location": "Google Meet"
#             }
#         }
# 
# 
#======================= beanie(mongoDB ODM) ====================
class Event(Document):
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    class Config:
            json_schema_extra = {
                "example": {
                    "title": "FastAPI BookLaunch",
                    "image": "https://linktomyimage.com/image.png",
                    "description": "We will be discussing the contents of the FastAPI book in this event.Ensure to come with your own copy to win gifts!",
                    "tags": ["python", "fastapi", "book", "launch"],
                    "location": "Google Meet"
                }
            }

class EventUpdate(BaseModel):
    title: Optional[str] = None  # 기본값 None 설정
    image: Optional[str] = None  # 기본값 None 설정
    description: Optional[str] = None  # 기본값 None 설정
    tags: Optional[List[str]] = None  # 기본값 None 설정
    location: Optional[str] = None  # 기본값 None 설정
    
    class Config:
        json_schema_extra = {
            "example": {
                "title": "FastAPI BookLaunch",
                "image": "https://linktomyimage.com/image.png",
                "description": "We will be discussing the contents of the FastAPI book in this event.Ensure to come with your own copy to win gifts!",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet"
            }
        }