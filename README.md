# MIAU — Missões Inclusivas de Aprendizagem Universal

Protótipo em Python, no terminal, para a disciplina Fundamentos da Programação.

## Como rodar

```
python main.py
```

O programa cria o arquivo `dados.json` sozinho na primeira vez.

## Fluxograma

Cada cor é uma pessoa do grupo. As caixas vermelhas são tratamento de erro.

```mermaid
flowchart TD
    INICIO(["python main.py"])
    P1["PASSO 1 · Carregar dados<br/>carregar_dados() · Pessoa 2"]
    ERRO1["Sem arquivo?<br/>usa dados vazios"]
    P2["PASSO 2 · Mostrar menu<br/>mostrar_menu() · Pessoa 1"]
    P3["PASSO 3 · Ler a opção<br/>ler_opcao() · Pessoa 5"]
    ERRO2["Digitou letra?<br/>pede de novo"]
    P4{"PASSO 4 · Qual opção?"}
    TURMAS["Opções 1 a 4 · turmas.py · Pessoa 3<br/>cadastrar_turma<br/>listar_turmas<br/>editar_turma<br/>excluir_turma"]
    DUA["Opções 5 e 6 · estrategias.py · Pessoa 4<br/>sugerir_estrategias<br/>registrar_feedback"]
    PAINEL["Opção 7 · relatorio.py · Pessoa 5<br/>painel_gestor<br/>contar_resultados<br/>banco_da_escola"]
    SAIR["Opção 0 · main.py · Pessoa 1<br/>break: sai do laço"]
    P5["PASSO 5 · Salvar dados<br/>salvar_dados() · Pessoa 2"]
    JSON2[("dados.json")]
    FIM(["Fim"])

    INICIO --> P1
    P1 -.-> ERRO1
    P1 --> P2
    P2 --> P3
    P3 -.-> ERRO2
    ERRO2 -.-> P3
    P3 --> P4
    P4 -->|1 a 4| TURMAS
    P4 -->|5 e 6| DUA
    P4 -->|7| PAINEL
    P4 -->|0| SAIR
    TURMAS --> P5
    DUA --> P5
    PAINEL --> P5
    SAIR --> FIM
    P5 --> JSON2
    P5 -->|volta ao menu| P2
    JSON2 -.->|na próxima execução, carrega o que foi salvo| P1

    classDef pessoa1 fill:#EEEDFE,stroke:#534AB7,color:#3C3489
    classDef pessoa2 fill:#E1F5EE,stroke:#0F6E56,color:#085041
    classDef pessoa3 fill:#FAECE7,stroke:#993C1D,color:#712B13
    classDef pessoa4 fill:#FBEAF0,stroke:#993556,color:#72243E
    classDef pessoa5 fill:#FAEEDA,stroke:#854F0B,color:#633806
    classDef erro fill:#FCEBEB,stroke:#A32D2D,color:#791F1F
    classDef neutro fill:#F1EFE8,stroke:#5F5E5A,color:#444441

    class P2,SAIR pessoa1
    class P1,P5 pessoa2
    class TURMAS pessoa3
    class DUA pessoa4
    class P3,PAINEL pessoa5
    class ERRO1,ERRO2 erro
    class INICIO,FIM,P4,JSON2 neutro
```

## Quem faz o quê

| Pessoa | Arquivo | Tarefa |
|---|---|---|
| 1 | `main.py` | Menu e integração das partes |
| 2 | `arquivos.py` | Salvar e carregar o `dados.json` |
| 3 | `turmas.py` | CRUD de turmas |
| 4 | `estrategias.py` | Sugestão de DUA e feedback |
| 5 | `relatorio.py` | `ler_opcao` e painel do gestor |

## Regras do grupo

1. Cada pessoa mexe só no seu arquivo.
2. Não mude o nome das funções. Outros arquivos chamam essas funções.
3. Não mude o formato dos dados sem avisar o grupo.
4. Procure os comentários `TODO`. Eles mostram o que falta fazer.
5. Apague as linhas marcadas com `APAGUE` quando terminar a função.
6. A Pessoa 5 termina `ler_opcao` primeiro, porque todos usam essa função.

## Formato combinado dos dados

```python
dados = {
    "turmas": [
        {"id": 1, "nome": "8A", "serie": "8º ano", "barreiras": ["atencao", "leitura"]}
    ],
    "feedbacks": [
        {"turma_id": 1, "estrategia": "Etapas numeradas", "resultado": "funcionou"}
    ],
    "proximo_id": 2
}
```

## Critérios do professor

| Critério | Onde está |
|---|---|
| CRUD | `turmas.py` |
| Lista, tupla e dicionário | todos os arquivos |
| Funções e modularização | 5 arquivos separados |
| Manipulação de arquivos | `arquivos.py` |
| Tratamento de exceções | `arquivos.py`, `relatorio.py`, `turmas.py`, `estrategias.py` |
