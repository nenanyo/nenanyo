from model.explorer import Explorer
from fastapi import HTTPException

from typing import List
"""python 3.8이하에서는 typing 모듈에서 사용하는 List, Tuple, Dict등을 사용해야 함"""

""" 가짜 데이터. 10장에서 실제 데이터베이스와 SQL로 바꾼다. """

_explorers = [
    Explorer(name="Claude Hande", country="FR", description="보름달이 뜨면 만나기 힘듦"),
    Explorer(name="Noah Weiser", country="DE", description="눈이 나쁘고 벌목도를 가지고 다님")
]


def get_all() -> List[Explorer]:
    """탐험가 목록을 반환한다."""
    
    return _explorers


def get_one(name: str) -> Explorer:
    """검색한 탐험가를 반환한다."""
    for _explorer in _explorers:
        if _explorer.name == name:
            return _explorer
    return None


# 다음 함수는 현재 올바로 동작하지 않는다.
# 실제로는 _explorers 목록을 수정하지 않지만,
# 마치 작동하는 것처럼 동작한다.
def create(explorer: Explorer) -> Explorer:
    """탐험가를 추가한다."""
    return explorer


def modify(name: str, explorer: Explorer) -> Explorer:
    """탐험가의 정보를 일부 수정한다."""
    return explorer


def replace(name: str, explorer: Explorer) -> Explorer:
    """탐험가를 완전히 교체한다."""
    return explorer


def delete(name: str) -> dict:
    """탐험가를 삭제한다. 만약 대상이 없다면 False를 반환한다."""
    for _explorer in _explorers:
        if _explorer.name == name:
            return {"message": f"탐험가 {name} 삭제 완료"}
    return HTTPException(status_code=404, detail="탐험가를 찾을 수 없습니다.")