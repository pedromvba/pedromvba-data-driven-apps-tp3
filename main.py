import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
from langchain.agents import initialize_agent, Tool
from langchain.prompts import PromptTemplate

#from langchain.tools import tool
#from langchain.agents import create_react_agent, AgentExecutor
#from langchain.prompts import PromptTemplate 




load_dotenv()

# LLM Model

#GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
#llm = GoogleGenerativeAI(model="gemini-1.5-flash",api_key=GEMINI_API_KEY)
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

# Agent

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True,
)

# Execução do agente com uma entrada inicial
response = agent.run("Adicione a tarefa 'Estudar matemática'.")


print(response)
print(tasks)
