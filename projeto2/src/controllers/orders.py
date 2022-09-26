from src.models.address import address_aggregate
from src.models import user
from src.models.order import (
    create_order,
    get_order_id_user,
    update_order,
    delete_order,
    )
from src.server.database import connect_db, db, disconnect_db


async def orders_crud():
    option = input("Entre com a opção de CRUD: ")
    
    await connect_db()
    orders_collection = db.orders_collection

    order =  [
           {
              "user": {},
              "price": "728",
              "paid": "no",
              "create": "26/09/2022",
              "address": {},
              "autority": True
           }
       ]

    if option == '1':
        # create order
        order = await create_order(
            orders_collection,
            order,
            address_aggregate,
            user._id
        )
        print(address)
    elif option == '2':
        # get order
        order = await get_order_id_user(
            orders_collection,
            order["user._id"]
        )
        print(order)
    elif option == '3':
        # update
        order = await get_order_id_user(
            orders_collection,
            order["user._id"]
        )

        order_data = {
              "user": {},
              "price": "26",
              "paid": "no",
              "create": "26/09/2022",
              "address": {},
              "autority": True
           }

        is_updated, numbers_updated = await update_order(
            orders_collection,
            order["_id"],
            order_data
        )
        if is_updated:
            print(f"Atualização realizada com sucesso, número de documentos alterados {numbers_updated}")
        else:
            print("Atualização falhou!")
    
        
    elif option == '4':
        # delete
        order = await get_order_id_user(
            orders_collection,
            order["user._id"]
        )

        result = await delete_order(
            orders_collection,
            order["_id"]
        )

        print(result)

   
    await disconnect_db()