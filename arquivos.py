# =====================================================
# MIAU - arquivos.py
# RESPONSÁVEL: Pessoa 2
#
# O QUE ESTE ARQUIVO FAZ:
# Guarda os dados no arquivo dados.json e lê os dados de volta.
# Assim, as turmas não somem quando o programa fecha.
#
# CRITÉRIOS QUE ESTE ARQUIVO ATENDE:
# - Manipulação de arquivos (open, read, write)
# - Tratamento de erros e exceções (try / except)
#
# DICA: o módulo json transforma um dicionário Python em texto
# e transforma o texto de volta em dicionário.
# =====================================================

import json

NOME_ARQUIVO = "dados.json"


def dados_vazios():
    """Devolve os dados iniciais, sem nenhuma turma.

    Este é o FORMATO COMBINADO pelo grupo. Não mude sem avisar todos.
    """
    return {
        "turmas": [],      # lista de dicionários (uma turma por item)
        "feedbacks": [],   # lista de dicionários (um feedback por item)
        "proximo_id": 1    # número do próximo id de turma
    }


def carregar_dados():
    """Lê o arquivo dados.json e devolve um dicionário.

    Se o arquivo não existir, devolve dados_vazios().
    Se o arquivo estiver estragado, avisa e devolve dados_vazios().
    """
    # TODO (Pessoa 2): complete os passos abaixo.
    #
    # try:
    #     abra o arquivo com: open(NOME_ARQUIVO, "r", encoding="utf-8")
    #     leia com: json.load(arquivo)
    #     devolva o que leu com return
    # except FileNotFoundError:
    #     o arquivo ainda não existe (primeira vez que o programa roda)
    #     devolva dados_vazios()
    # except json.JSONDecodeError:
    #     o arquivo existe, mas o texto dentro está errado
    #     mostre um aviso com print e devolva dados_vazios()

    return dados_vazios()  # APAGUE esta linha quando terminar


def salvar_dados(dados):
    """Escreve o dicionário dados no arquivo dados.json."""
    # TODO (Pessoa 2): complete os passos abaixo.
    #
    # try:
    #     abra o arquivo com: open(NOME_ARQUIVO, "w", encoding="utf-8")
    #     escreva com: json.dump(dados, arquivo, ensure_ascii=False, indent=2)
    # except OSError:
    #     não deu para gravar (disco cheio, sem permissão...)
    #     mostre um aviso com print

    pass  # APAGUE esta linha quando terminar
