import streamlit as st
from workflows.simplification_flow import executar_fluxo

st.title("Analisador de Discursos e Propostas")

deputado_id = st.text_input("ID do deputado")
data_inicio = st.text_input("Data início (AAAA-MM-DD)")
data_fim = st.text_input("Data fim (AAAA-MM-DD)")

if st.button("Executar Análise"):
    with st.spinner("Processando..."):
        resultados = executar_fluxo(int(deputado_id), data_inicio, data_fim)

    st.subheader("Resultado da Simplificação")
    st.write(resultados["simplificacao"])

    st.subheader("Resultado da Verificação de Coerência")
    st.write(resultados["coerencia"])
