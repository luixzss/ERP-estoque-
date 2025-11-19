from estoque import cadastrar_produto, excluir_produto, mostrar_relatorio
from database import con  # para fechar depois
def main():
    while True:
        print("\n=== Sistema de Estoque ===")
        print("1 - Cadastrar produto")
        print("2 - Excluir produto")
        print("3 - Mostrar relatório")
        print("4 - Sair")

        opcao = input("Escolha: ")

         if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            excluir_produto()
        elif opcao == "3":
            mostrar_relatorio()
        elif opcao == "4":
            print("Saindo...")
            con.close()
            break
        else:
            print("Opção inválida.")

if _name_ == "_main_":
    main()