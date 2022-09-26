import asyncio

from src.controllers.users import users_crud
from src.controllers.products import products_crud
from src.controllers.address import address_crud
from src.controllers.orders import orders_crud
from src.controllers.order_items import order_items_crud

loop = asyncio.get_event_loop()
loop.run_until_complete(users_crud())
