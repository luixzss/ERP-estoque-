# Lista para armazenar os produtos. Cada produto será um dicionário.
estoque = []
# Variável para gerar um ID único para cada produto.
proximo_id = 1

    def cadastrar_produto():
    """
    Função para cadastrar um novo produto no estoque.
    Solicita nome, categoria, unidade de medida, preço e quantidade.
    """
    global proximo_id
    print("\n--- Cadastro de Novo Produto ---")
