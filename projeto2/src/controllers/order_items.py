from src.models.address import address_aggregate
from src.models import product
from src.models import user
from src.models.order import (
    create_order_item,
    get_order_item_id_user,
    update_order_item,
    delete_order_item,
    sum_order_item
    )
from src.server.database import connect_db, db, disconnect_db


async def order_items_crud():
    option = input("Entre com a opção de CRUD: ")
    
    await connect_db()
    order_items_collection = db.order_items_collection

    order_item =  [
           {
             'order':{order._id}
             'product':{product._id}
           }
       ]

    if option == '1':
        # create order_item
        order_item = await create_order_item(
            order_items_collection,
            order._id,
            product._id,
            user._id
        )
        print(order_item)
    elif option == '2':
        # get order_items
        order_item = await get_order_item_id_user(
            order_items_collection,
            order_item["order.user._id"]
        )
        print(order)
    elif option == '3':
        # update
        order_item = await get_order_item_id_user(
            order_items_collection,
            order_item["order.user._id"]
        )

        order_item_data = {
              'order':{order._id}
             'product':{product._id}
           }

        is_updated, numbers_updated = await update_order_item(
            order_items_collection,
            order_item["_id"],
            order_item
        )
        if is_updated:
            print(f"Atualização realizada com sucesso, número de documentos alterados {numbers_updated}")
        else:
            print("Atualização falhou!")
    
        
    elif option == '4':
        # delete
        order_item = await get_order_item_id_user(
            order_items_collection,
            order_item["user._id"]
        )

        result = await delete_order_item(
            order_item_collection,
            order_item["_id"]
        )

        print(result)
    
    elif option == '5':
        result = await sum_order_item(
            order_items_collection,
            user._id
        )

   
    await disconnect_db()