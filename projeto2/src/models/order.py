from src.models import user
from src.models.address import aggregate_address


# Buscar a ordem de compra pelo id do usuário
async def get_order_id_user(orders_collection, user_id):
    try:
        data = await orders_collection.find_one({'user._id': user_id})
        if data:
            return data
    except Exception as e:
        print(f'get_order.error: {e}')

#criar ordem de compra quando não existe ordem de compra para o usuário
async def create_order(orders_collection, user, address_aggregate, order, user_id):
    try:
        if get_order_id_user == None:
            order = await orders_collection.insert_one(order{"user": user, "address": address_aggregate})
        
        if order.inserted_id:
            order = await get_order_id_user(orders_collection, user_id)
            return order

    except Exception as e:
        print(f'create_order.error: {e}')



#adicionar uma ordem quando já existe uma ordem de compra vinculado ao usuario
async def update_order(orders_collection, user_id, order_data, address_aggregate):
    try:
        data = {k: v for k, v in order_data.items() if v is not None}

        order = await orders_collection.update_one(
            {'user._id': user_id}, {'address': address_aggregate}, {'$addToSet': data}
        )

        if order.modified_count:
            return True, order.modified_count

        return False, 0
    except Exception as e:
        print(f'add_order.error: {e}')



async def delete_order(orders_collection, order_id):
    try:
        order = await orders_collection.delete_one(
            {'_id': order_id}
        )
        if order.deleted_count:
            return {'status': 'Order deleted'}
    except Exception as e:
        print(f'delete_order.error: {e}')
