# Projeto Democracia Aberta

Equipe: Camile Alheiro, Maria Gabrielly A. Santana e Thiago Ribeiro

Este projeto investiga como discursos, textos de proposições e registros de voto podem ser combinados para medir a coerência ideológica e comportamental dos deputados federais. A proposta preenche uma lacuna importante na literatura: a maioria dos estudos foca apenas em dados estruturados, enquanto aqui integramos conteúdo textual complexo usando técnicas modernas de Processamento de Linguagem Natural (PLN) e modelagem de tópicos.

Ao cruzar o que o parlamentar diz com o que ele vota, buscamos revelar padrões de consistência (ou divergência) que hoje não são visíveis ao cidadão comum. Isso reforça a transparência e permite novas formas de interpretação do comportamento legislativo.

## Objetivos do Projeto
- Analisar a coerência entre retórica e comportamento de voto de deputados federais;
- Utilizar técnicas de NLP e LLM para análise dos dados;
- Criar uma metodologia replicável para estudos de comportamento legislativo baseados em texto;
- Contribuir para maior transparência e compreensão do processo legislativo por parte do cidadão comum.

--- 

## Contribuições
- Integração entre dados textuais completos e registros de votação da Câmara.
- Abordagem que permite identificar a divergência entre discurso e voto;
- Aplicação de técnicas modernas de PLN e LLM para análise legislativa em português;
- Metodologia que complementa estudos anteriores focados em Random Forest, redes complexas e modelos analíticos;
- Avanço em transparência pública ao fornecer um caminho para ferramentas que explicam legislação em linguagem simples;
- Reforço da participação democrática ao tornar documentos complexos mais acessíveis.

---

## Execução

--- 

## Visão Técnica do Projeto

Este projeto utiliza **IA multiagente** e **Modelos de Linguagem rodando localmente via Ollama** para analisar discursos de parlamentares, simplificar linguagem, auditar fidelidade e, em fases futuras, avaliar a **coerência entre discurso e prática legislativa**.

Ele combina:

* Análise linguística
* Simplificação acessível
* Auditoria automática
* RAG (memória vetorial)
* Análise legislativa
* Medição de coerência política
* Pipeline sequencial com múltiplos agentes

### Funcionalidades Atuais (MVP)

* Coleta automática de discursos da API da Câmara dos Deputados
* Análise profunda dos discursos por agente especializado
* Simplificação para linguagem acessível
* Auditoria da fidelidade entre discurso original e simplificado
* Geração de relatório final consolidado
* Execução local usando modelos LLM via **Ollama**

### Roadmap 

**Fase 1 — MVP**

* Pipeline multiagente com análise, simplificação, auditoria e consolidação
* Coleta de discursos via API
* Execução local via Ollama

**Fase 2 — Memória Longa (RAG)**

* Criação de um banco vetorial (ChromaDB ou similar)
* Armazenamento de discursos, proposições, votações e metadados
* Criação de um agente especializado em consultas RAG

**Fase 3 — Análise de Proposições Legislativas**

* Coleta automática de proposições e projetos de lei
* Classificação temática das proposições
* Enriquecimento da memória vetorial com dados legislativos

**Fase 4 — Índice de Coerência Política**

* Cálculo de similaridade entre temas dos discursos e das proposições
* Identificação de conexões, contradições e inconsistências
* Geração de score de coerência entre fala e prática legislativa

**Fase 5 — Agente de Coerência Política**

* Agente especializado em cruzar discursos, proposições e votações
* Relatório analítico explicando onde o político é coerente ou contraditório

**Fase 6 — Pipeline Integrado Completo**

* Pipeline unificado combinando análise, RAG e coerência
* Relatório final com avaliação temática, coerência e resumo simplificado

**Fase 7 — Exportação Profissional**

* Exportação para PDF e JSON.
