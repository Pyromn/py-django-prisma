
import asyncio

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

    await db.disconnect()

if __name__ == '__main__':
    asyncio.run(main())