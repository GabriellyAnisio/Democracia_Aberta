from crewai import Agent
from config.llm import llm

analyzer_agent = Agent(
    role="Analista Legislativo",
    goal="Classificar o texto, identificar termos técnicos e organizar tópicos.",
    backstory="Especialista em análise de documentos jurídicos.",
    verbose=True,
    llm=llm
)
