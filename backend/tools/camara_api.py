import requests

BASE_URL = "https://dadosabertos.camara.leg.br/api/v2"

def get_discursos(deputado_id: int, data_inicio: str, data_fim: str):
    """
    Busca discursos no período especificado.
    Exemplo de data: '2022-01-01'
    """

    url = f"{BASE_URL}/deputados/{deputado_id}/discursos"
    params = {
        "dataInicio": data_inicio,
        "dataFim": data_fim
    }

    resp = requests.get(url, params=params)

    if resp.status_code != 200:
        return {"erro": f"Falha ao acessar API ({resp.status_code})"}

    json_data = resp.json()

    discursos = json_data.get("dados", [])

    # Extrair as transcrições dos discursos
    textos = []
    for d in discursos:
        transcricao = d.get("transcricao")
        sumario = d.get("sumario")
        tipo = d.get("tipoDiscurso")
        inicio = d.get("dataHoraInicio")

        textos.append({
            "data": inicio,
            "tipo": tipo,
            "sumario": sumario,
            "transcricao": transcricao or ""
        })

    return textos
