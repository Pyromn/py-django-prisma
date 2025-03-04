
import asyncio

from prisma.enums import Role
from pydantic import PydanticUserError, TypeAdapter, ValidationError
from prisma import Prisma
from prisma.models import *

async def main() -> None:
    db = Prisma(auto_register=True)
    await db.connect()

    # write your queries here

    users = await User.prisma().find_many()
    posts = await Post.prisma().find_many()

    for user in users:
        print(user)

    for post in posts:
        print(post)

    try:
        print(User.model_json_schema())
    except PydanticUserError as e:
        print(e)


    user_list_adapter = TypeAdapter(List[User])
    print(user_list_adapter.json_schema())

    try:
        user_list = user_list_adapter.validate_python([{
            # 'id': '3',
            'name': 'Fred',
            'email': 'test@mail.com',
            'role': Role.ADMIN,
        }])
        print(repr(user_list))
    except ValidationError as e:
        print(e)

    # try without required email attribute
    try:
        user_list = user_list_adapter.validate_python([{
            # 'id': '3',
            'name': 'Fred',
            # 'email': 'test@mail.com',
            'role': Role.ADMIN,
        }])
        print(repr(user_list))
    except ValidationError as e:
        print(e)

    print(repr(user_list_adapter.dump_json(user_list)))


    await db.disconnect()

if __name__ == '__main__':
    asyncio.run(main())