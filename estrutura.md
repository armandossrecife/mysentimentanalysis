# Predicting Architectural Technical Debt: A Architectural Impact Issue Classification Model Based on Issue Details

Previsão de dívida técnica architectural: um modelo de classificação de issues de impacto arquitetural com base em detalhes dos issues.

## Sugestão de Estrutura

### Introdução
* **Problema:** Apresentar o problema da Dívida Técnica Arquitetural (ATD) e seu impacto no desenvolvimento de software.
* **Objetivo:** Definir o objetivo do trabalho, que é desenvolver um método para identificar issues relacionados à ATD em projetos de software, utilizando técnicas de aprendizado de máquina.
* **Contribuições:** Destacar as principais contribuições do trabalho, como o desenvolvimento do ATDCodeAnalyzer, o processo de inspeção semi-automática e o modelo de classificação baseado em Hugging Face DestilBert.

### Metodologia
* **ATDCodeAnalyzer:** Detalhar a construção e funcionamento do ATDCodeAnalyzer, explicando como ele identifica artefatos de código afetados por ATD.
* **Processo de Inspeção Semi-Automática:** Descrever o processo, incluindo a utilização do ChatGPT para analisar issues e a seleção dos projetos Apache como base de dados.
* **Modelo de Classificação:**
    * **Arquitetura:** Explicar a escolha do Hugging Face DestilBert e a arquitetura do modelo 
    * **Conjunto de Dados:** Detalhar o processo de coleta e preparação dos dados, incluindo pré-processamento, criação de rótulos e divisão em conjuntos de treinamento e teste.
    * **Treinamento:** Descrever o processo de treinamento, incluindo métricas utilizadas, otimizador e função de perda.
    * **Avaliação:** Apresentar os resultados da avaliação do modelo, utilizando as métricas precision, recall, accuracy, F1-score e AUC.

### Resultados e Discussão
* **Resultados Quantitativos:** Apresentar os resultados detalhados da classificação, incluindo as métricas para cada fold da validação cruzada.
* **Análise dos Resultados:**
    * Discutir os resultados obtidos, comparando-os com trabalhos anteriores e justificando as diferenças.
    * Analisar as métricas e identificar as classes que foram mais difíceis de classificar.
    * Avaliar a robustez do modelo em relação a diferentes projetos e conjuntos de dados.
* **Casos de Uso:** Apresentar exemplos práticos de como o modelo pode ser utilizado para identificar issues com impacto arquitetural em projetos reais.

### Conclusões
* **Resumo das Contribuições:** Reforçar as principais contribuições do trabalho.
* **Limitações:** Discutir as limitações do estudo, como a dependência da qualidade dos dados e a generalização do modelo para outros domínios.
* **Trabalhos Futuros:** Sugerir direções para trabalhos futuros, como a expansão do modelo para outros tipos de issues ou a integração do modelo em ferramentas de desenvolvimento de software.

### Apêndice
* **Código:** Incluir o código fonte do ATDCodeAnalyzer e do modelo de classificação, juntamente com uma breve explicação.
* **Detalhes Adicionais:** Apresentar detalhes técnicos adicionais, como a configuração do ambiente experimental e as bibliotecas utilizadas.

**Observações:**

* **Visualizações:** Utilize gráficos e tabelas para apresentar os resultados de forma clara e concisa.
* **Clareza e Concisão:** Escreva de forma clara e concisa, evitando jargões técnicos excessivos.
* **Revisão:** Revise cuidadosamente o texto para garantir a coesão e a fluidez.

**Sugestões Adicionais:**

* **Comparação com outras abordagens:** Comparar o seu método com outras abordagens existentes para identificar issues relacionadas à ATD.
* **Análise de erros:** Analisar os erros do modelo para identificar padrões e possíveis melhorias.
* **Estudo de caso:** Apresentar um estudo de caso detalhado para ilustrar a aplicação do método em um projeto real.
