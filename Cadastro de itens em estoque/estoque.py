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
    con.commit()
    print(" Produto cadastrado com sucesso!")


def excluir_produto():
    nome = input("\nNome do produto a excluir: ")

    cur.execute("SELECT id FROM produtos WHERE LOWER(nome) = LOWER(?)", (nome,))
    produto = cur.fetchone()
     if produto:
        cur.execute("DELETE FROM produtos WHERE id = ?", (produto[0],))
        con.commit()
        print("Produto excluído.")
    else:
        print("Produto não encontrado.")




    
