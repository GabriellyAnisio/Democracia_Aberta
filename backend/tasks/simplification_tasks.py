from crewai import Task
from agents.analyzer_agent import analyzer_agent
from agents.simplifier_agent import simplifier_agent
from agents.auditor_agent import auditor_agent
from agents.coordinator_agent import coordinator_agent

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
