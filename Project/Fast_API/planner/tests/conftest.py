import asyncio

import httpx
import pytest

from database.connection import Settings
from main import app
from models.events import Event
from models.users import User


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


async def init_db():
    test_settings = Settings()
    test_settings.DATABASE_URL = "mongodb://localhost:27017/testdb"

    await test_settings.initialize_database()


# 애플리케이션 인스턴스 반환
@pytest.fixture(scope="session")
async def default_client():
    await init_db()
    async with httpx.AsyncClient(app=app, base_url="http://app") as client:
        yield client

        # 리소스 정리
        await Event.find_all().delete()
        await User.find_all().delete()