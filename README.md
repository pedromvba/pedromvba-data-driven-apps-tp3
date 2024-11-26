# Gerenciador de Tarefas com LangChain e Google Generative AI

## Descrição do Problema e da Solução

Este projeto é um gerenciador de tarefas simples que utiliza a biblioteca LangChain, Agentes e o modelo Google Generative AI para gerenciar uma lista de tarefas. O objetivo da aplicação é permitir que pessoas organizem e acompanhem suas tarefas cotidianas, como por exemplo, estudantes em uma faculdade ou profissionais liberais. A solução automatiza o processo de adicionar, listar e remover tarefas, proporcionando uma interface interativa e eficiente para o gerenciamento de tarefas.

## Casos de Uso Testados e Resultados Observados

### Caso de Uso 1: Adicionar Tarefa

Comando: "Adicione a tarefa 'Estudar matemática'

Resultado Esperado: A tarefa 'Estudar matemática' é adicionada à lista de tarefas

Resultado Observado: A tarefa foi adicionada corretamente e uma mensagem de confirmação foi exibida.

### Caso de Uso 2: Listar Tarefas
Comando: "Liste todas as tarefas"

Resultado Esperado: Todas as tarefas pendentes são listadas.

Resultado Observado: As tarefas foram listadas corretamente, exibindo todas as tarefas pendentes

### Caso de Uso 3: Remover Tarefa
Comando: "Remova a tarefa 'Estudar matemática'"

Resultado Esperado: A tarefa 'Estudar matemática' é removida da lista de tarefas

Resultado Observado: A tarefa foi removida corretamente e uma mensagem de confirmação foi exibida.

## Reflexão sobre a Facilitação pelo Agente

A utilização do agente baseado em LangChain e Google Generative AI facilitou o gerenciamento de tarefas em comparação a uma abordagem manual uma vez que apenas por meio de linguagem natural foi possível adicionar, listar e remover tarefas, o que reduz o tempo e o esforço necessários para gerenciar as tarefas.


## Requisitos

- Python 3.12.4
- `dotenv`
- `langchain`
- `langchain_google_genai`
- `langchain-community`

## Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/pedromvba/pedromvba-data-driven-apps-tp3
    ```

2. Crie um ambiente virtual e ative-o:

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. Execute o script `main.py`:

    ```bash
    python main.py
    ```

2. O script solicitará que o usuário informe um comando para ser realizado com a lista.

## Estrutura do Projeto

- `main.py`: Script principal que inicializa o agente, define as funções de gerenciamento de tarefas e executa comandos de exemplo.
- `requirements.txt`: Lista de dependências do projeto.

## Funcionalidades

- **Adicionar Tarefa**: Adiciona uma tarefa à lista de tarefas.
- **Listar Tarefas**: Lista todas as tarefas pendentes.
- **Remover Tarefa**: Remove uma tarefa da lista de tarefas.

## Exemplo de Uso

```python
# Adiciona uma tarefa
"Adicione a tarefa 'Estudar matemática'."

# Lista todas as tarefas
"Liste todas as tarefas."

# Remove uma tarefa
"Remova a tarefa 'Estudar matemática'."