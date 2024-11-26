import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
from langchain.agents import initialize_agent, Tool
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory



load_dotenv()

# LLM Model

llm = GoogleGenerativeAI(model="gemini-pro")

# Tools

tasks = []

def add_task(task: str) -> str:
    """Adiciona uma tarefa à lista."""
    tasks.append(task)
    return f"Tarefa '{task}' adicionada."

def list_tasks(args=None) -> str:
    """Lista todas as tarefas pendentes."""
    return "\n".join(tasks) if tasks else "Nenhuma tarefa pendente."

def remove_task(task: str) -> str:
    """Remove uma tarefa da lista."""
    if task in tasks:
        tasks.remove(task)
        return f"Tarefa '{task}' removida."
    else:
        return f"Tarefa '{task}' não encontrada."


tools = [
    Tool(name="add_task", func=add_task, description="Adiciona uma tarefa à lista."),
    Tool(name="list_tasks", func=list_tasks, description="Lista todas as tarefas pendentes."),
    Tool(name="remove_task", func=remove_task, description="Remove uma tarefa da lista."),
]

# Memory

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Agent

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True,
    memory=memory
)
# Input

while True:

    command = input("Digite um comando ou sair para encerrar a aplicação: ")

    if command.lower() == "sair":
        print("Encerrando aplicação...")
        break

    if command.lower() == "debug":
        print("Debugando...")
        print(tasks)
        print("\nHistórico de conversa:")
        print(memory.chat_memory.messages)

    else:
        response = agent.run(command)
        print(response)
        print("\n Lista Atualizada")
        print(tasks)