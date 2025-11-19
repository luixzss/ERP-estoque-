from codigo import cadastrar_produto, excluir_produto, mostrar_relatorio
from database import con  # para fechar depois
def main():
    while True:
        print("\n=== Sistema de Estoque ===")
        print("1 - Cadastrar produto")
        print("2 - Excluir produto")
        print("3 - Mostrar relatório")
        print("4 - Sair")

        opcao = input("Escolha: ")

