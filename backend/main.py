from workflows.simplification_flow import executar_fluxo
from dotenv import load_dotenv
load_dotenv()

deputado_id = 74646
data_inicio = "2022-01-01"
data_fim = "2022-03-31"

print(f"## ⏳ Iniciando Análise para Deputado {deputado_id} ({data_inicio} a {data_fim})")
print("---")

resultados = executar_fluxo(
    deputado_id=deputado_id,
    data_inicio=data_inicio,
    data_fim=data_fim
)

print("\n\n" + "="*50)
print("## RESULTADO FINAL DA CREW")
print("="*50 + "\n")

# 1. Resultado da Simplificação
print("### Relatório de Análise e Simplificação")
print(resultados["simplificacao"])

print("\n" + "-"*50 + "\n")

# 2. Resultado da Coerência
print("### Relatório de Coerência entre Discursos e Propostas")
print(resultados["coerencia"])
print("\n" + "="*50)