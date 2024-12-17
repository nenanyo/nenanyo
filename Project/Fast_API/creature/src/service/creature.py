from typing import List, Optional
from model.creature import Creature
import data.creature as data


def get_all() -> List[Creature]:
    return data.get_all()


def get_one(name: str) -> Optional[Creature]:
    return data.get_one(name)


def create(creature: Creature) -> Creature:
    return data.create(creature)


def replace(name: str, creature: Creature) -> Creature:
    return data.replace(name, creature)


def modify(name: str, creature: Creature) -> Creature:
    return data.modify(name, creature)


def delete(name: str) -> bool:
    return data.delete(name)