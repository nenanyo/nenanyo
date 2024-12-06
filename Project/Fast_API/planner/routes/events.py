from typing import List

from beanie import PydanticObjectId
from fastapi import APIRouter, Depends, HTTPException, Request, status
from database.connection import get_session, Database
from sqlmodel import select

from models.events import Event, EventUpdate

event_router = APIRouter(
    tags=["Events"]
)

events = []

#==========================  sqlalchemy사용   ================================

# # 전체 이벤트 조회
# @event_router.get("/", response_model=List[Event])
# async def retrieve_all_events(session=Depends(get_session)) -> List[Event]:
#     statement = select(Event)
#     events = session.exec(statement).all()
#     return events

# # 단일 이벤트 조회
# @event_router.get("/{id}", response_model=Event)
# async def retrieve_event(id: int, session=Depends(get_session)) -> Event:
#     event = session.get(Event, id)
#     if event:
#          return event
#     raise HTTPException(
#         status_code=status.HTTP_404_NOT_FOUND,
#         detail="Event with supplied ID does not exist"
#     )

# # 이벤트 저장
# @event_router.post("/new")
# async def create_event(new_event: Event,
#     session = Depends(get_session)) -> dict:
#         session.add(new_event)
#         session.commit()
#         session.refresh(new_event)
#         return {
#         "message": "Event created successfully"
#     }

# # 이벤트 수정
# @event_router.put("/edit/{id}", response_model=Event)
# async def update_event(id: int, new_data: EventUpdate,session = Depends(get_session)) -> Event:   # 한줄로 작성 줄바꿈하면 에러남 
#     event = session.get(Event, id)
#     if event:
#         # new_data에서 제공된 필드만 업데이트하고 나머지 필드는 기존 값을 유지
#         event_data = new_data.dict(exclude_unset=True)  # 제공되지 않은 필드는 제외
#         for key, value in event_data.items():
#             setattr(event, key, value)

#         session.add(event)
#         session.commit()
#         session.refresh(event)

#         return event
    
#     raise HTTPException(
#          status_code=status.HTTP_404_NOT_FOUND,
#          detail="Event with supplied ID does not exist"
#      )

# # 단일 이벤트 삭제
# @event_router.delete("/delete/{id}")
# async def delete_event(id: int, session=Depends(get_session)) -> dict:
#     event = session.get(Event, id)
#     if event:
#          session.delete(event)
#          session.commit()
#          return {
#               "message" : "Event deleted successfully."
#          }

#     raise HTTPException(
#         status_code=status.HTTP_404_NOT_FOUND,
#         detail="Event with supplied ID does not exist"
#     )
  
# # 전체 이벤트 삭제
# @event_router.delete("/")
# async def delete_all_events() -> dict:
#     events.clear()
#     return {
#         "message": "Events deleted successfully"
#     }


#==================================  beanie(mongoDB)  ======================================

event_database = Database(Event)

# 전체 이벤트 조회
@event_router.get("/", response_model=List[Event])
async def retrieve_all_events() -> List[Event]:
    events = await event_database.get_all()
    return events

# 단일 이벤트 조회
@event_router.get("/{id}", response_model=Event)
async def retrieve_event(id: PydanticObjectId) -> Event:
    event = await event_database.get(id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist"
        )   
    return event

# 이벤트 저장
@event_router.post("/new")
async def create_event(body: Event) -> dict:
        await event_database.save(body)    
        return {
        "message": "Event created successfully"
    }

# 이벤트 수정
@event_router.put("/{id}", response_model=Event)
async def update_event(id: PydanticObjectId, body: EventUpdate) -> Event:
    updated_event = await event_database.update(id, body)
    if not updated_event:        
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist"
        )
    return updated_event

# 단일 이벤트 삭제
@event_router.delete("/{id}")
async def delete_event(id: PydanticObjectId) -> dict:
    event = await event_database.delete(id)
    if not event:        
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist"
        )
    return {
        "message": "Event deleted successfully."
    }
  
# 전체 이벤트 삭제
@event_router.delete("/")
async def delete_all_events() -> dict:
    events.clear()
    return {
        "message": "Events deleted successfully"
    }