#Carrinho de compras
id_user = input('Digite o id do usuário:')
id_produto = input('Digite o id do produto:')
price_product = float(input('Digite o preço do produto:'))
quantity_product = int(input('Digite a quantidade do produto:'))

item = [id_user, id_produto, price_product, quantity_product]

chart = []
def add_item_cart(item):
    pass

def get_all_item_cart():
    return

def get_all_item_cart_by_id(id_product):
    pass

def remove_item_id(id_product):
    #remover o item do carrinho que tem esse produto

#eu quero o item onde o produto for o tenis adidas que o código é 123

new_lista = None

for item in chart:
    #print item
    if item[0] == '123':
        new_lista = item
        #new lista.append(item)

print (new_lista)

new_list = [item for item in chart if item[0]=='123']
print (new_list[0])

def filtra_item(item, product):
    if item[0] == product:
        return item

n_list = filter(lambda elem: elem[0] =='123', chart)
print(list(n_list))

# for i in cart

# filter -> cart

def retorna_item_id(produto):
    def filtra_item(item):
        if item[0] == produto:
            return item

        n_list = filter(filtra_item, chart)
        print(list(n_list))

retorna_item_id('123')

def get_all_item_cart():
    return chart

print (chart)

