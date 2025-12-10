from crewai import Task
from agents.analyzer_agent import analyzer_agent
from agents.simplifier_agent import simplifier_agent
from agents.auditor_agent import auditor_agent
from agents.coordinator_agent import coordinator_agent
from agents.proposal_analyzer_agent import proposal_analyzer_agent
from agents.coherence_checker_agent import coherence_checker_agent

# 1) Analisar
analysis_task = Task(
    description=(
        "Analise profundamente o documento abaixo. "
        "Identifique tópicos centrais, temas recorrentes, aspectos sociais, "
        "pontos políticos e objetivos principais.\n\n"
        "DOCUMENTO:\n{documento}"
    ),
    expected_output="Um relatório detalhado com tópicos e achados relevantes.",
    agent=analyzer_agent,
    output_key="analise"
)

# 2) Simplificar
simplification_task = Task(
    description=(
        "Com base na análise anterior, reescreva o conteúdo em linguagem "
        "extremamente simples, popular e acessível a qualquer pessoa. "
        "Evite termos técnicos."
    ),
    expected_output="Um texto simplificado e fácil de entender.",
    agent=simplifier_agent,
    output_key="simplificado"
)

# 3) Auditar
audit_task = Task(
    description=(
        "Verifique se o texto simplificado mantém fidelidade ao conteúdo original."
    ),
    expected_output="Texto auditado e fiel.",
    agent=auditor_agent,
    output_key="auditado"
)

# 4) Versão final
final_task = Task(
    description="Combine análise, simplificação e auditoria em um relatório final.",
    expected_output="Relatório final consolidado.",
    agent=coordinator_agent,
    output_key="resultado_final"
)

# 5) Analisar Propostas
proposal_analysis_task = Task(
    description=(
        "Analise o conjunto de propostas legislativas do político. "
        "Identifique padrões, áreas de foco, e os principais temas propostos.\n\n"
        "PROPOSTAS:\n{propostas}"
    ),
    expected_output="Um relatório conciso sobre os temas e foco das propostas.",
    agent=proposal_analyzer_agent,
    output_key="analise_propostas"
)

# 6) Verificar Coerência
coherence_check_task = Task(
    description=(
        "Compare a análise dos Discursos (disponível no input: '{analise_discursos}') " # <-- Referenciando a chave de input
        "com a análise das Propostas (disponível no contexto da task anterior). " 
        "Avalie se há coerência entre o que o político discursa e o que ele propõe formalmente. "
        "Sinalize áreas de conflito ou de alinhamento."
    ),
    expected_output="Um relatório de coerência detalhado e conclusivo (Coerente/Incoerente/Parcialmente Coerente).",
    agent=coherence_checker_agent,
    output_key="verificacao_coerencia"
)