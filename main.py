# =====================================================
# MIAU - main.py
# RESPONSÁVEL: Pessoa 1
#
# O QUE ESTE ARQUIVO FAZ:
# Mostra o menu principal e chama as funções dos outros arquivos.
# Este arquivo NÃO faz contas nem cadastros. Ele só organiza.
#
# CRITÉRIOS QUE ESTE ARQUIVO ATENDE:
# - Uso de funções (modularização): importa os outros arquivos
# - Integração de todas as partes do grupo
# =====================================================

# Cada linha abaixo traz um arquivo de outra pessoa.
import arquivos      # Pessoa 2
import turmas        # Pessoa 3
import estrategias   # Pessoa 4
import relatorio     # Pessoa 5


def mostrar_menu():
    """Mostra as opções do menu na tela."""
    print()
    print("========== MIAU ==========")
    print("1 - Cadastrar turma")
    print("2 - Listar turmas")
    print("3 - Editar turma")
    print("4 - Excluir turma")
    print("5 - Ver estratégias DUA de uma turma")
    print("6 - Registrar feedback de uma estratégia")
    print("7 - Painel do gestor")
    print("0 - Sair")
    print("==========================")


def main():
    """Função principal. O programa começa aqui."""
    # 1. Carrega os dados do arquivo (função da Pessoa 2).
    dados = arquivos.carregar_dados()

    # 2. Repete o menu até a pessoa escolher 0.
    while True:
        mostrar_menu()

        # ler_opcao é da Pessoa 5. Ela não deixa o programa quebrar
        # se a pessoa digitar uma letra.
        opcao = relatorio.ler_opcao("Escolha uma opção: ")

        if opcao == 1:
            turmas.cadastrar_turma(dados)
        elif opcao == 2:
            turmas.listar_turmas(dados)
        elif opcao == 3:
            turmas.editar_turma(dados)
        elif opcao == 4:
            turmas.excluir_turma(dados)
        elif opcao == 5:
            estrategias.sugerir_estrategias(dados)
        elif opcao == 6:
            estrategias.registrar_feedback(dados)
        elif opcao == 7:
            relatorio.painel_gestor(dados)
        elif opcao == 0:
            print("Até logo!")
            break
        else:
            print("Opção inválida. Escolha um número do menu.")

        # 3. Salva depois de cada ação (função da Pessoa 2).
        arquivos.salvar_dados(dados)


# Esta linha faz o programa rodar quando executamos: python main.py
if __name__ == "__main__":
    main()
