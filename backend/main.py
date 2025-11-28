from workflows.simplification_flow import executar_fluxo
from dotenv import load_dotenv
load_dotenv()

resultado = executar_fluxo(
    deputado_id=74646,
    data_inicio="2022-01-01",
    data_fim="2022-03-31"
)

print(resultado)
