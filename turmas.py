# =====================================================
# MIAU - turmas.py
# RESPONSÁVEL: Pessoa 3
#
# O QUE ESTE ARQUIVO FAZ:
# O CRUD de turmas:
#   C = Create = cadastrar
#   R = Read   = listar
#   U = Update = editar
#   D = Delete = excluir
#
# CRITÉRIOS QUE ESTE ARQUIVO ATENDE:
# - CRUD (obrigatório)
# - Lista, tupla e dicionário
# - Funções
#
# FORMATO DE UMA TURMA (dicionário):
# {"id": 1, "nome": "8A", "serie": "8º ano", "barreiras": ["atencao", "leitura"]}
# =====================================================

import relatorio  # para usar ler_opcao (Pessoa 5)

# Tupla: as barreiras possíveis. Tupla porque esta lista não muda.
BARREIRAS = ("atencao", "leitura", "organizacao", "memoria", "barulho")


def buscar_turma(dados, id_turma):
    """Procura a turma pelo id. Devolve o dicionário da turma ou None."""
    for turma in dados["turmas"]:
        if turma["id"] == id_turma:
            return turma
    return None


def escolher_barreiras():
    """Pergunta quais barreiras a turma tem. Devolve uma lista."""
    # TODO (Pessoa 3):
    # 1. Mostre as BARREIRAS com um número na frente (use enumerate).
    # 2. Peça os números separados por vírgula. Exemplo: 1,3
    # 3. Para cada número, pegue a barreira certa da tupla.
    # 4. Coloque na lista escolhidas com append.
    # 5. Se a pessoa digitar algo errado, use try/except e ignore.
    escolhidas = []
    return escolhidas


def cadastrar_turma(dados):
    """C - Create: cria uma turma nova e coloca na lista."""
    # TODO (Pessoa 3):
    # 1. Peça o nome da turma com input. Exemplo: 8A
    # 2. Peça a série com input. Exemplo: 8º ano
    # 3. Chame escolher_barreiras()
    # 4. Monte o dicionário da turma. Use dados["proximo_id"] como id.
    # 5. Coloque a turma em dados["turmas"] com append.
    # 6. Some 1 em dados["proximo_id"].
    # 7. Mostre: "Turma cadastrada!"
    print("[em construção] cadastrar_turma")


def listar_turmas(dados):
    """R - Read: mostra todas as turmas."""
    # TODO (Pessoa 3):
    # 1. Se a lista estiver vazia, mostre "Nenhuma turma cadastrada."
    # 2. Se não, use for para mostrar id, nome, série e barreiras.
    print("[em construção] listar_turmas")


def editar_turma(dados):
    """U - Update: muda o nome, a série ou as barreiras de uma turma."""
    # TODO (Pessoa 3):
    # 1. Chame listar_turmas(dados).
    # 2. Peça o id com relatorio.ler_opcao("Id da turma: ")
    # 3. Use buscar_turma. Se devolver None, mostre "Turma não encontrada."
    # 4. Peça o novo nome. Se a pessoa só apertar Enter, mantenha o antigo.
    # 5. Faça o mesmo para a série.
    # 6. Pergunte se quer mudar as barreiras (s/n).
    print("[em construção] editar_turma")


def excluir_turma(dados):
    """D - Delete: apaga uma turma da lista."""
    # TODO (Pessoa 3):
    # 1. Chame listar_turmas(dados).
    # 2. Peça o id com relatorio.ler_opcao("Id da turma: ")
    # 3. Use buscar_turma. Se devolver None, mostre "Turma não encontrada."
    # 4. Pergunte "Tem certeza? (s/n)".
    # 5. Se for "s", use dados["turmas"].remove(turma).
    print("[em construção] excluir_turma")
