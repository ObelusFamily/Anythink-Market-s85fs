#!/usr/bin/python
import pathlib
import sys
import asyncio
import asyncpg

sys.path.append(str(pathlib.Path(__file__).resolve().parents[2]))

from app.core.config import get_app_settings
from app.db.repositories.users import UsersRepository
from app.db.repositories.items import ItemsRepository
from app.db.repositories.comments import CommentsRepository
from app.api.dependencies.database import get_repository

SETTINGS = get_app_settings()
DATABASE_URL = SETTINGS.database_url.replace("postgres://", "postgresql://")

user_data_list = [{
    "username": f"user_{i}",
    "email": f"user_{i}@yopmail.com",
    "password": "password",
} for i in range(100)]

partial_item_data_list = [{
    "slug": f"Item-{i}",
    "title": f"Item-{i}",
    "description": f"Description for item {i}",
} for i in range(100)]


partial_comment_data_list = [{
    "body": f"Body of comment {i}",
} for i in range(100)]


async def create_objects(users_repo: UsersRepository, items_repo: ItemsRepository, comments_repo: CommentsRepository):
    for i in range(100):
        if i % 10 == 0:
            print()
            print(f"{i}% done")
            print()
        user_data = user_data_list[i]
        partial_item_data = partial_item_data_list[i]
        partial_comment_data = partial_comment_data_list[i]

        user_in_db = await users_repo.create_user(**user_data)
        item = await items_repo.create_item(**partial_item_data, seller=user_in_db)
        await comments_repo.create_comment_for_item(**partial_comment_data, item=item, user=user_in_db)


    print("Over")


async def main():
    conn =  await asyncpg.connect(DATABASE_URL)

    users_repo = get_repository(UsersRepository)(conn)
    items_repo = get_repository(ItemsRepository)(conn)
    comments_repo = get_repository(CommentsRepository)(conn)

    await create_objects(users_repo, items_repo, comments_repo)

    await conn.close()


asyncio.run(main())
