from crewai import Agent
from tools.camara_api import get_discursos

collector_agent = Agent(
    role="Coletor de discursos",
    goal="Coletar discursos da API e entregar texto limpo.",
    backstory="Especialista em integração com a API da Câmara.",
    verbose=True,
    allow_delegation=False
)

def coletar_discursos(deputado_id: int, data_inicio: str, data_fim: str):
    discursos = get_discursos(deputado_id, data_inicio, data_fim)

    if isinstance(discursos, dict) and "erro" in discursos:
        return discursos["erro"]

    texto_final = ""
    for disc in discursos:
        texto_final += (
            f"\n[DISCURSO]\n"
            f"Data: {disc['data']}\n"
            f"Tipo: {disc['tipo']}\n"
            f"Sumário: {disc['sumario']}\n\n"
            f"{disc['transcricao']}\n"
            + "-"*80 + "\n"
        )

    return texto_final
