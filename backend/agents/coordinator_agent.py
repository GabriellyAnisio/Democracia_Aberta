from crewai import Agent
from config.llm import llm

coordinator_agent = Agent(
    role="Coordenador",
    goal="Orquestrar o fluxo completo e consolidar o relatório final.",
    backstory="Gerente responsável pela integração das etapas.",
    verbose=True,
    llm=llm
)
