from src.models import product
from src.models import order
from src.models import user 
# Buscar as ordens de compra do usuário
async def get_order_item_id_user(order_items_collection, user_id):
    try:
        data = await order_items_collection.find({'order.user._id': user_id})
        if data:
            return data
    except Exception as e:
        print(f'get_order_item.error: {e}')


async def create_order_item(order_items_collection, user_id, order._id, product._id):
    try:
        if get_order_item_id_user == None:
            order_item = await order_items_collection.insert_one({"order": order._id, "product": product._id})
        
        if order_item.inserted_id:
            order_item = await get_order_item_id_user(order_items_collection, user_id)
            return order

    except Exception as e:
        print(f'create_order_item.error: {e}')



async def update_order_item(order_items_collection, order_item_id, order_item_data):
    try:
        data = {k: v for k, v in order_item_data.items() if v is not None}

        order_item_data = await order_items_collection.update_one(
            {'_id': order_item_id}, {'$addToSet': order_item_data}
        )

        if order_item_data.modified_count:
            return True, order_item_data.modified_count

        return False, 0
    except Exception as e:
        print(f'update_order_item.error: {e}')



async def delete_order_item(order_items_collection, order_item_id):
    try:
        order_item_data = await order_items_collection.delete_one(
            {'_id': order_item_id}
        )
        if order_item_data.deleted_count:
            return {'status': 'Order item deleted'}
    except Exception as e:
        print(f'delete_order_item.error: {e}')

async def sum_order_item (order_items_collection, user_id):
    try:
        sum_user = await order_items_collection.find({'order.user._id': user_id})
        count = 0
        for sum in sum_user:
            count = sum_user[sum].product.price + count
        print (f'o preço total é {count}')
    except Exception as e:
        print(f'sum_order_item.error: {e}')