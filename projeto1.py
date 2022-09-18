from fastapi import FastAPI
from typing import List
from pydantic import BaseModel


app = FastAPI()

OK = "OK"
FALHA = "FALHA"


# Classe representando os dados do endereço do cliente
class Endereco(BaseModel):
    rua: str
    cep: str
    cidade: str
    estado: str


# Classe representando os dados do cliente
class Usuario(BaseModel):
    id: int
    nome: str
    email: str
    senha: str


# Classe representando a lista de endereços de um cliente
class ListaDeEnderecosDoUsuario(BaseModel):
    usuario: Usuario
    enderecos: List[Endereco] = []


# Classe representando os dados do produto
class Produto(BaseModel):
    id: int
    nome: str
    descricao: str
    preco: float


# Classe representando o carrinho de compras de um cliente com uma lista de produtos
class CarrinhoDeCompras(BaseModel):
    id_usuario: int
    id_produtos: List[Produto] = []
    preco_total: float
    quantidade_de_produtos: int


db_usuarios = {}
db_produtos = {}
db_end = {}        # enderecos_dos_usuarios
db_carrinhos = {}

# Criar um usuário,
# se tiver outro usuário com o mesmo ID retornar falha, 
# se o email não tiver o @ retornar falha, 
# senha tem que ser maior ou igual a 3 caracteres,
# senão retornar OK
@app.post("/usuario/")
async def criar_usuario(usuario: Usuario):
    if usuario.id in db_usuarios:
        return FALHA
    else:
        db_usuarios[usuario.id] = usuario
        return ("Novo usuário inserido:", usuario.dict())


# Se o id do usuário existir, retornar os dados do usuário
# senão retornar falha
@app.get("/usuario/")
async def retornar_usuario(id: int):
    if id in db_usuarios:
        return db_usuarios[id]
    return FALHA


# Se existir um usuário com exatamente o mesmo nome, retornar os dados do usuário
# senão retornar falha
@app.get("/usuario/nome")
async def retornar_usuario_com_nome(nome: str):
    for user in db_usuarios:
        if db_usuarios[user].nome == nome:
            return db_usuarios[user]
    return FALHA

  
# Se o id do usuário existir, deletar o usuário e retornar OK
# senão retornar falha
# ao deletar o usuário, deletar também endereços e carrinhos vinculados a ele
@app.delete("/usuario/")
async def deletar_usuario(id: int):
    if id in db_usuarios:
        db_usuarios.pop(id)
        db_end.pop(id) 
        return (db_usuarios)
    else:
        return FALHA


# Se não existir usuário com o id_usuario retornar falha, 
# senão retornar uma lista de todos os endereços vinculados ao usuário
# caso o usuário não possua nenhum endereço vinculado a ele, retornar 
# uma lista vazia
### Estudar sobre Path Params (https://fastapi.tiangolo.com/tutorial/path-params/)
@app.get("/usuario/{id_usuario}/endereços/")
async def retornar_enderecos_do_usuario(id_usuario: int, usuario:Usuario):
    for user_end_list in db_usuarios:
        if db_usuarios[user_end_list].id == id_usuario:
            return ListaDeEnderecosDoUsuario(usuario.id)
        return FALHA




# Se não existir usuário com o id_usuario retornar falha, 
# senão cria um endereço, vincula ao usuário e retornar OK
@app.post("/endereco/{id_usuario}/")
async def criar_endereco(endereco: Endereco, id_usuario: int, usuario:Usuario):
    for user_end in db_usuarios:
        if db_usuarios[user_end].id == id_usuario:
            db_end[usuario.id] = endereco
            return OK 
    return FALHA



# Se não existir endereço com o id_endereco retornar falha, 
# senão deleta endereço correspondente ao id_endereco e retornar OK
# (lembrar de desvincular o endereço ao usuário)
@app.delete("/endereco/{id_endereco}/")
async def deletar_endereco(id_endereco: int, usuario: Usuario):
    for del_end in db_end:
        if db_end[del_end].usuario.id == id_endereco:
            db_end.pop(id_endereco)
            return OK



# Se tiver outro produto com o mesmo ID retornar falha, 
# senão cria um produto e retornar OK
@app.post("/produto/")
async def criar_produto(produto: Produto):
    if produto.id in db_produtos:
        return FALHA
    else: 
        db_produtos[produto.id] = produto
        return OK



# Se não existir produto com o id_produto retornar falha, 
# senão deleta produto correspondente ao id_produto e retornar OK
# (lembrar de desvincular o produto dos carrinhos do usuário)
@app.delete("/produto/{id_produto}/")
async def deletar_produto(id_produto: int):
    for prod in db_produtos:
        if db_produtos[prod].id == id_produto:
            db_produtos.pop(id)
            db_carrinhos.pop(id) 
        return OK
    else:
        return FALHA



# Se não existir usuário com o id_usuario ou id_produto retornar falha, 
# se não existir um carrinho vinculado ao usuário, crie o carrinho
# e retornar OK
# senão adiciona produto ao carrinho e retornar OK
@app.post("/carrinho/{id_usuario}/{id_produto}/")
async def adicionar_carrinho(id_usuario: int, id_produto: int, carrinho: CarrinhoDeCompras):
    for user_car in db_carrinhos:
        if db_carrinhos[user_car].id_usuario == id_usuario:
            return FALHA
        else: 
            db_carrinhos[carrinho.id_usuario] = carrinho
            return OK  
        

# Se não existir carrinho com o id_usuario retornar falha, 
# senão retorna o carrinho de compras.
@app.get("/carrinho/{id_usuario}/")
async def retornar_carrinho(id_usuario: int):
    for car in db_carrinhos:
        if db_carrinhos[car].id_usuario == id_usuario:
            return FALHA
    return CarrinhoDeCompras.id_usuario



# Se não existir carrinho com o id_usuario retornar falha, 
# senão retorna o o número de itens e o valor total do carrinho de compras.
@app.get("/carrinho/{id_usuario}/")
async def retornar_total_carrinho(id_usuario: int):
    for car in db_carrinhos:
        if db_carrinhos[car].id_usuario == id_usuario:
            return FALHA
        else: 
            return db_carrinhos.quantidade_de_produtos, db_carrinhos.preco_total


# Se não existir usuário com o id_usuario retornar falha, 
# senão deleta o carrinho correspondente ao id_usuario e retornar OK
@app.delete("/carrinho/{id_usuario}/")
async def deletar_carrinho(id_usuario: int):
    for del_car in db_carrinhos:
        if db_carrinhos[del_car].id_usuario == id_usuario:
            db_carrinhos.pop(id_usuario)
            return OK


@app.get("/")
async def bem_vinda():
    site = "Seja bem vinda, que bom ter você aqui"
    return site.replace('\n', '')
