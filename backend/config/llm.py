from crewai import LLM

# Usando o modelo local do Ollama
llm = LLM(
    model="ollama/llama3.1",
    base_url="http://localhost:11434",  # padrão do Ollama
)
