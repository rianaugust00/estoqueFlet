import flet as ft
from models import Session, Produto  # Importando o modelo e a sessão do models.py

# Função principal da interface
def main(page: ft.Page):
    page.title = "Cadastro de Produto"
    session = Session()  # Iniciar a sessão aqui

    # Função para cadastrar produto no banco
    def cadastrar(e):
        # Cria um novo produto com os valores informados
        novoProduto = Produto(titulo=produto.value, preco=float(preco.value))
        session.add(novoProduto)  # Adiciona o produto na sessão
        session.commit()  # Confirma a inserção no banco de dados
        print('Produto salvo com sucesso')

    # Componentes da interface gráfica
    txt_titulo = ft.Text('Título do produto:')
    produto = ft.TextField(label="Digite o título do produto:", text_align=ft.TextAlign.LEFT)
    txt_preco = ft.Text('Preço do produto:')
    preco = ft.TextField(value="0", label="Digite o preço do produto:", text_align=ft.TextAlign.LEFT)
    btnProduto = ft.ElevatedButton('Cadastrar', on_click=cadastrar)

    # Adiciona os componentes à página
    page.add(
        txt_titulo,
        produto,
        txt_preco,
        preco,
        btnProduto
    )

# Executa o app com a função principal
ft.app(target=main)
