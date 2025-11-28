from crewai import Agent
from config.llm import llm

auditor_agent = Agent(
    role="Auditor de Fidelidade",
    goal="Garantir que a simplificação mantém fidelidade ao texto original.",
    backstory="Especialista em detectar erros, distorções e mudanças de sentido.",
    verbose=True,
    llm=llm
)
