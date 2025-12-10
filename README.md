# Democracia Aberta: Sistema Multiagente para Análise de Discursos, Propostas Legislativas e Coerência Política

Camile Alheiro, Maria Gabrielly e Thiago Ribeiro.

### Usando **CrewAI + Ollama (Llama 3)**

Este projeto implementa um **pipeline multiagente** capaz de:

1. **Analisar discursos políticos**
2. **Simplificar e auditar a análise**
3. **Analisar propostas legislativas**
4. **Avaliar coerência entre discursos e proposições oficiais**

A arquitetura usa **CrewAI** com agentes especializados e um modelo **local Llama 3 via Ollama**, garantindo desempenho e privacidade.

---

## 🚀 Tecnologias

* **Python 3.10+**
* **CrewAI**
* **Ollama** (executando `llama3`)
* **Modelos locais para LLM**
* Estrutura modular com agentes independentes

---

## 🏗️ Arquitetura dos Agentes

### 🔍 1. `analyzer_agent`

Analisa profundamente um discurso, identificando temas, padrões e objetivos.

### ✏️ 2. `simplifier_agent`

Transforma a análise em uma versão simples e acessível, em linguagem popular.

### 🕵️ 3. `auditor_agent`

Garante fidelidade da simplificação ao conteúdo original.

### 🧩 4. `coordinator_agent`

Une análise + simplificação + auditoria em um relatório final.

### 🗂️ 5. `proposal_analyzer_agent`

Analisa proposições oficiais (ex.: PLS, PL, PEC…).

### ⚖️ 6. `coherence_checker_agent`

Compara:

* análise dos discursos
* análise das propostas

E avalia **coerência política**.

---

## 🔧 Configuração do LLM (Ollama)

```python
from crewai import LLM

llm = LLM(
    model="ollama/llama3",
    base_url="http://localhost:11434",  
)
```

---

## 📌 Definição das Tasks

### **1) Análise do discurso**

```python
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
```

### **2) Simplificação**

```python
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
```

### **3) Auditoria**

```python
audit_task = Task(
    description="Verifique se o texto simplificado mantém fidelidade ao conteúdo original.",
    expected_output="Texto auditado e fiel.",
    agent=auditor_agent,
    output_key="auditado"
)
```

### **4) Relatório Final**

```python
final_task = Task(
    description="Combine análise, simplificação e auditoria em um relatório final.",
    expected_output="Relatório final consolidado.",
    agent=coordinator_agent,
    output_key="resultado_final"
)
```

### **5) Análise de Propostas**

```python
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
```

### **6) Verificação de Coerência**

```python
coherence_check_task = Task(
    description=(
        "Compare a análise dos Discursos (disponível no input: '{analise_discursos}') "
        "com a análise das Propostas (disponível no contexto da task anterior). "
        "Avalie se há coerência entre o que o político discursa e o que ele propõe formalmente. "
        "Sinalize áreas de conflito ou de alinhamento."
    ),
    expected_output=(
        "Um relatório de coerência detalhado e conclusivo "
        "(Coerente/Incoerente/Parcialmente Coerente)."
    ),
    agent=coherence_checker_agent,
    output_key="verificacao_coerencia"
)
```

---

## ▶️ Pipeline Completo

O pipeline segue a seguinte ordem:

1. `analysis_task`
2. `simplification_task`
3. `audit_task`
4. `final_task`
5. `proposal_analysis_task`
6. `coherence_check_task`

---

## 🗃️ Estrutura Recomendada do Projeto

```
/project
│
├── agents/
│   ├── analyzer_agent.py
│   ├── simplifier_agent.py
│   ├── auditor_agent.py
│   ├── coordinator_agent.py
│   ├── proposal_analyzer_agent.py
│   └── coherence_checker_agent.py
│
├── tasks.py
├── main.py
├── README.md
└── requirements.txt
```

---

## 📦 Instalação

### 1) Instalar dependências

```bash
pip install crewai python-dotenv
```

### 2) Instalar e rodar o Ollama

```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama pull llama3
ollama serve
```

### 3) Executar o pipeline

```bash
python main.py
```

---

## 🧪 Exemplo de Uso

```python
resultado = crew.run(
    {
        "documento": texto_dos_discursos,
        "propostas": json_de_proposicoes,
        "analise_discursos": analise_pelo_primeiro_agente
    }
)

print(resultado["verificacao_coerencia"])
```

Aqui está a **seção pronta para colar no README.md**, já formatada, limpa e elegante:

---

## 🔬 Experimentos com Modelos Ollama

Durante o desenvolvimento foram testados três variantes do Llama executadas localmente via **Ollama**. Os resultados práticos foram:

### 🔹 **llama3:8b**

* Mais rápido
* Mais leve
* Muito bom para tarefas de **coerência**
* **Resultado:** adequado, porém menos profundo nas análises complexas

---

### 🔹 **llama3:latest**

* Melhor equilíbrio entre velocidade e profundidade
* Custo computacional moderado
* Respostas mais consistentes que a versão **8b**
* **Resultado:** modelo com melhor custo × qualidade

---

### 🔹 **llama3.1:latest**

* Versão mais atualizada
* Em alguns testes apresentou maior estabilidade
* Entretanto, para este projeto específico, ofereceu **menos precisão analítica**
* **Resultado:** funcional, mas **não foi o ideal** para análise detalhada de discursos e propostas

---

