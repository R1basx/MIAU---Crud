# =====================================================
# MIAU - relatorio.py
# RESPONSÁVEL: Pessoa 5
#
# O QUE ESTE ARQUIVO FAZ:
# 1. ler_opcao: lê um número sem deixar o programa quebrar.
#    TODOS os outros arquivos usam esta função.
# 2. painel_gestor: mostra os números da escola para o gestor.
#
# CRITÉRIOS QUE ESTE ARQUIVO ATENDE:
# - Tratamento de erros e exceções (try / except ValueError)
# - Lista e dicionário
# - Funções
# =====================================================


def ler_opcao(mensagem):
    """Pede um número inteiro. Repete até a pessoa digitar um número.

    Exemplo: se a pessoa digitar "abc", int("abc") dá ValueError.
    """
    # TODO (Pessoa 5):
    # while True:
    #     texto = input(mensagem)
    #     try:
    #         devolva int(texto) com return
    #     except ValueError:
    #         mostre "Digite apenas números."
    #
    # ATENÇÃO: esta função é usada pelo grupo todo.
    # Termine esta primeiro!

    return int(input(mensagem))  # APAGUE esta linha quando terminar


def contar_resultados(dados):
    """Conta os feedbacks. Devolve um dicionário.

    Exemplo de retorno: {"funcionou": 3, "parcial": 1, "nao funcionou": 2}
    """
    # TODO (Pessoa 5):
    # 1. Crie o dicionário contagem com os 3 resultados valendo 0.
    # 2. Para cada feedback em dados["feedbacks"]:
    #        some 1 em contagem[feedback["resultado"]]
    # 3. Devolva contagem com return.
    contagem = {}
    return contagem


def banco_da_escola(dados):
    """Devolve uma lista com as estratégias que funcionaram (sem repetir)."""
    # TODO (Pessoa 5):
    # 1. Crie a lista vazia que_funcionaram = []
    # 2. Para cada feedback, se o resultado for "funcionou"
    #    e a estratégia ainda não estiver na lista, use append.
    # 3. Devolva a lista com return.
    que_funcionaram = []
    return que_funcionaram


def painel_gestor(dados):
    """Mostra os números da escola. Não mostra nomes de alunos."""
    # TODO (Pessoa 5):
    # 1. Mostre quantas turmas existem: len(dados["turmas"])
    # 2. Mostre quantos feedbacks existem: len(dados["feedbacks"])
    # 3. Chame contar_resultados e mostre cada resultado.
    # 4. Chame banco_da_escola e mostre cada estratégia.
    print("[em construção] painel_gestor")
