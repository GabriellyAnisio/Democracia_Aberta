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

def get_propostas(deputado_id: int, data_inicio: str, data_fim: str):
    """
    Busca as propostas legislativas do deputado no período especificado,
    filtrando por 'idDeputadoAutor' e datas.

    :param deputado_id: O ID do deputado autor.
    :param data_inicio: Data de início do período (Ex: '2022-01-01').
    :param data_fim: Data de fim do período (Ex: '2022-03-31').
    :return: Uma string consolidada com as informações das propostas.
    """

    url = f"{BASE_URL}/proposicoes"
    
    # Parâmetros da requisição: Filtro por autor e período
    params = {
        "idDeputadoAutor": deputado_id,
        "dataApresentacaoInicio": data_inicio, # Chave correta para filtrar a data
        "dataApresentacaoFim": data_fim,       # Chave correta para filtrar a data
    }

    resp = requests.get(url, params=params)

    if resp.status_code != 200:
        return f"ERRO: Falha ao acessar API de Propostas ({resp.status_code}) para o ID {deputado_id}."

    json_data = resp.json()

    propostas = json_data.get("dados", [])

    if not propostas:
        return f"Nenhuma proposta encontrada para o deputado {deputado_id} entre {data_inicio} e {data_fim}."

    # Formatar os dados das propostas para análise
    textos_propostas = []
    for p in propostas:
        tipo_numero_ano = f"{p.get('siglaTipo')} {p.get('numero')}/{p.get('ano')}"
        ementa = p.get("ementa", "Ementa não disponível.")
        data = p.get("dataApresentacao", "Data não disponível").split('T')[0] # Limpa a hora

        textos_propostas.append(
            f"TIPO/NÚMERO/ANO: {tipo_numero_ano}\n"
            f"DATA DE APRESENTAÇÃO: {data}\n"
            f"EMENTA: {ementa}\n"
        )

    return "\n--- PROPOSTA ---\n".join(textos_propostas)
