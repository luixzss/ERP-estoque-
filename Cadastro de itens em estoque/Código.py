from database import cur, con

def cadastrar_produto():
    print("\n--- Cadastro de Novo Produto ---")

    nome = input("Nome: ")
    categoria = input("Categoria: ")
    unidade = input("Unidade (UN, KG, LT): ").upper()
    preco = float(input("Preço: "))
    quantidade = float(input("Quantidade: "))

    cur.execute("""
        INSERT INTO produtos (nome, categoria, unidade_medida, preco, quantidade)
        VALUES (?, ?, ?, ?, ?)
    """, (nome, categoria, unidade, preco, quantidade))


    
