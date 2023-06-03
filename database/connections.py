from playhouse.shortcuts import model_to_dict

from config import ADMINS
from .models import *


async def add_user_db(user_id: int, username: str):
    with db:
        if not Users.select().where(Users.user_id == user_id).exists():
            Users.create(user_id=user_id, username=username)
            return True
        return False


async def update_user_db(user_id: int, full_name: str):
    with db:
        Users.update(full_name=full_name).where(Users.user_id == user_id).execute()



