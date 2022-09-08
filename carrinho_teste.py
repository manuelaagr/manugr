cart = []

def add_item_cart(item):
    cart.append(item)

def continua(resposta):
    resposta = input('Deseja adicionar itens ao carrinho? s ou n?')
    if resposta == 's':
        id_user = input('Digite o id do usuário:')
        id_produto = input('Digite o id do produto:')
        price_product = float(input('Digite o preço do produto:'))
        quantity_product = int(input('Digite a quantidade do produto:'))
        item = [id_user, id_produto, price_product, quantity_product]
        add_item_cart(item)
        continua(resposta)

resposta = input('Deseja adicionar itens ao carrinho? s ou n?')
if resposta == 's':
    id_user = input('Digite o id do usuário:')
    id_produto = input('Digite o id do produto:')
    price_product = float(input('Digite o preço do produto:'))
    quantity_product = int(input('Digite a quantidade do produto:'))
    item = [id_user, id_produto, price_product, quantity_product]
    add_item_cart(item)
    continua(resposta)

print(cart)




