from crewai import Crew, Process
from agents.collector_agent import get_discursos
from tools.camara_api import get_propostas # <-- IMPORTE A FUNÇÃO DO ARQUIVO tools/camara_api.py # Importe o novo coletor
from tasks.simplification_tasks import (
    analysis_task,
    simplification_task,
    audit_task,
    final_task,
    proposal_analysis_task,
    coherence_check_task
)

def executar_fluxo(deputado_id: int, data_inicio: str, data_fim: str):

    # 1. Coleta de Dados
    documento_discursos = get_discursos(deputado_id, data_inicio, data_fim)
    documento_propostas = get_propostas(deputado_id, data_inicio, data_fim)

    # 2. Configuração do Crew
    simplification_crew = Crew(
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
        verbose=False,
        return_intermediate_steps=True
    )

    coherence_crew = Crew(
        agents=[
            proposal_analysis_task.agent,
            coherence_check_task.agent,
        ],
        tasks=[
            proposal_analysis_task,
            coherence_check_task,
        ],
        process=Process.sequential,
        verbose=False,
        return_intermediate_steps=True
    )

    # 3. Execução dos Fluxos
    resultado_simplificacao = simplification_crew.kickoff(
        inputs={"documento": documento_discursos}
    )

    analise_discursos = str(resultado_simplificacao)

    resultado_coerencia = coherence_crew.kickoff(
        inputs={
            "propostas": documento_propostas,
            "analise_discursos": analise_discursos
        }
    )

    return {
        "simplificacao": resultado_simplificacao,
        "coerencia": resultado_coerencia
    }