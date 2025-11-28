from crewai import Crew, Process

from agents.collector_agent import coletar_discursos
from tasks.simplification_tasks import (
    analysis_task,
    simplification_task,
    audit_task,
    final_task
)

def executar_fluxo(deputado_id: int, data_inicio: str, data_fim: str):

    documento = coletar_discursos(deputado_id, data_inicio, data_fim)

    crew = Crew(
        agents=[
            analysis_task.agent,
            simplification_task.agent,
            audit_task.agent,
            final_task.agent
        ],
        tasks=[
            analysis_task,
            simplification_task,
            audit_task,
            final_task
        ],
        process=Process.sequential,
        verbose=True
    )

    resultado = crew.kickoff(
        inputs={
            "documento": documento
        }
    )

    return resultado
