# =====================================================
# MIAU - estrategias.py
# RESPONSÁVEL: Pessoa 4
#
# O QUE ESTE ARQUIVO FAZ:
# A parte específica do MIAU:
# 1. Sugere estratégias DUA para a turma, a partir das barreiras.
# 2. Registra o feedback do professor: funcionou, parcial ou não.
#
# CRITÉRIOS QUE ESTE ARQUIVO ATENDE:
# - Funcionalidade específica da solução
# - Dicionário e tupla
# - Funções
#
# FORMATO DE UM FEEDBACK (dicionário):
# {"turma_id": 1, "estrategia": "Etapas numeradas", "resultado": "funcionou"}
# =====================================================

import relatorio  # para usar ler_opcao (Pessoa 5)
import turmas     # para usar buscar_turma e listar_turmas (Pessoa 3)

# Dicionário: cada barreira (chave) tem uma tupla de estratégias (valor).
# O grupo pode trocar ou aumentar estas estratégias.
ESTRATEGIAS_DUA = {
    "atencao": ("Dividir a aula em blocos curtos",
                "Pergunta principal em destaque"),
    "leitura": ("Frases curtas no enunciado",
                "Ler o enunciado em voz alta"),
    "organizacao": ("Etapas numeradas",
                    "Lista de tarefas no quadro"),
    "memoria": ("Resumo no fim da aula",
                "Exemplo com algo que o aluno gosta"),
    "barulho": ("Momento de silêncio combinado",
                "Lugar mais calmo na sala"),
}

# Tupla: os resultados possíveis do feedback.
RESULTADOS = ("funcionou", "parcial", "nao funcionou")


def sugerir_estrategias(dados):
    """Mostra as estratégias DUA para as barreiras de uma turma."""
    # TODO (Pessoa 4):
    # 1. Chame turmas.listar_turmas(dados).
    # 2. Peça o id com relatorio.ler_opcao("Id da turma: ")
    # 3. Use turmas.buscar_turma. Se for None, avise e pare com return.
    # 4. Para cada barreira em turma["barreiras"]:
    #        pegue as estratégias com ESTRATEGIAS_DUA.get(barreira, ())
    #        mostre a barreira e as estratégias.
    print("[em construção] sugerir_estrategias")


def registrar_feedback(dados):
    """Guarda se uma estratégia funcionou na turma."""
    # TODO (Pessoa 4):
    # 1. Escolha a turma (igual aos passos 1 a 3 acima).
    # 2. Peça o nome da estratégia usada com input.
    # 3. Mostre os RESULTADOS com um número na frente (use enumerate).
    # 4. Peça o número com relatorio.ler_opcao.
    # 5. Use try/except IndexError caso o número não exista.
    # 6. Monte o dicionário do feedback e use
    #    dados["feedbacks"].append(feedback)
    # 7. Mostre: "Feedback registrado!"
    print("[em construção] registrar_feedback")
