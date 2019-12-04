import asyncio
import orm
import sys
from models import User, Blog, Comment

async def test(loop):
    await orm.create_pool(loop, user='root', password='rootpwd', db='awesome')
    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
    await u.save()
    await orm.destroy_pool()

# loop = asyncio.get_event_loop()
loop = asyncio.new_event_loop()
loop.run_until_complete(test(loop))
loop.close()
print('done')
sys.exit(0)