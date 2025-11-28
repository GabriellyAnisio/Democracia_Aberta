from crewai import Agent
from config.llm import llm

simplifier_agent = Agent(
    role="Simplificador de discurso",
    goal="Reescrever discursos em linguagem simples e acessível.",
    backstory=(
        "Especialista em comunicação clara e acessível. "
        "Transforma discursos políticos e jurídicos em textos simples."
    ),
    verbose=True,
    allow_delegation=False,
    llm=llm
)
