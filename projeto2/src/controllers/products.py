from src.models.product import (
    create_product,
    get_product_by_code,
    update_product,
    delete_product,
    get_products
)
from src.server.database import connect_db, db, disconnect_db


async def products_crud():
    option = input("Entre com a opção de CRUD: ")
    
    await connect_db()
    products_collection = db.products_collection

    product =  {
        "name" : "Bicicleta Aro 29 Freio a Disco 21M. Velox Branca/Verde - Ello Bike",
        "description" : "Bicicleta produzida com materiais de qualidade e foi criada pensando nas pessoas que desejam praticar o ciclismo e ter uma vida saudável sem abrir mão de conforto um excelente custo x benefício.",
        "price" : 898.2,
        "image" : "https://a-static.mlcdn.com.br/800x560/bicicleta-aro-29-freio-a-disco-21m-velox-branca-verde-ello-bike/ellobike/6344175219/b84d5dd41098961b4c2f397af40db4ce.jpg",
        "code" : 97880.0
    }

    if option == '1':
        # create product
        product = await create_product(
            products_collection,
            product
        )
        print(product)
    elif option == '2':
        # get product
        product = await get_product_by_code(
            products_collection,
            product["code"]
        )
        print(product)
    elif option == '3':
        # update
        product = await get_product_by_code(
            products_collection,
            product["code"]
        )

        product_data = {
            "price": 900
        }

        is_updated, numbers_updated = await update_product(
            products_collection,
            product["_id"],
            product_data
        )
        if is_updated:
            print(f"Atualização realizada com sucesso, número de documentos alterados {numbers_updated}")
        else:
            print("Atualização falhou!")
    elif option == '4':
        # delete
        product = await get_product_by_code(
            products_collection,
            product["code"]
        )

        result = await delete_product(
            products_collection,
            product["_id"]
        )

        print(result)

    elif option == '5':
        # pagination
        products = await get_products(
            products_collection,
            skip=2,
            limit=2
        )
        print(products)

    await disconnect_db()
