# LAB03 - Análise de Code Review no GitHub

**Disciplina:** Laboratório de Experimentação de Software  
**Professor:** João Paulo Carneiro Aramuni  
**Grupo:** Letícia Rodrigues Blom e Júlia Borges Araújo Silva  

---

## Contexto

No GitHub, revisões de código são feitas por meio de *pull requests* (PRs), onde desenvolvedores propõem alterações no código e colaboradores do projeto realizam uma análise antes de integrá-las à branch principal. Esse processo pode envolver revisores humanos e ferramentas automáticas (como bots e pipelines CI/CD). Neste trabalho, consideramos apenas revisões humanas, com pelo menos 1 hora de duração e ao menos 1 revisão registrada.

---

## Objetivo

Este laboratório tem como objetivo analisar a atividade de *code review* em repositórios populares do GitHub. O foco está em identificar variáveis que podem influenciar o sucesso de um pull request — definido como a sua aceitação (status `merged`) — e o número de revisões realizadas no processo.

### Hipóteses Iniciais

Este relatório analisa como características dos Pull Requests (PRs) — como tamanho, tempo de análise, descrição e interações — se relacionam com dois aspectos principais:

A. O feedback final da revisão (se o PR foi aceito ou rejeitado)

B. O número de revisões realizadas (iterações até a aprovação)

Formulamos hipóteses simples para cada relação, buscando entender padrões que podem melhorar o processo de revisão colaborativa.

#### A. Feedback Final das Revisões (Status do PR)

- **RQ01. Qual a relação entre o tamanho dos PRs e o feedback final das revisões?**  
  *Hipótese:* O tamanho do PR influencia o status do PR, e PRs maiores tendem a demorar mais a alterar seu status (merged/closed), além de terem maior chance de serem rejeitados por dificultarem a revisão.

- **RQ02. Qual a relação entre o tempo de análise dos PRs e o feedback final das revisões?**  
  *Hipótese:* PRs que levam mais tempo para serem analisados têm maior chance de serem rejeitados, pois podem indicar falta de prioridade ou dificuldades na revisão.

- **RQ03. Qual a relação entre a descrição dos PRs e o feedback final das revisões?**  
  *Hipótese:* PRs com descrições mais detalhadas tendem a ser aceitos com mais frequência, já que facilitam a compreensão do objetivo e impacto da mudança.

- **RQ04. Qual a relação entre as interações nos PRs e o feedback final das revisões?**  
  *Hipótese:* PRs com mais interações (comentários e participantes) podem ter maior chance de serem aceitos, pois indicam engajamento e colaboração na revisão. Por outro lado, muitos comentários podem sinalizar problemas ou dúvidas, aumentando a chance de rejeição.

#### B. Número de Revisões

- **RQ05. Qual a relação entre o tamanho dos PRs e o número de revisões realizadas?**  
  *Hipótese:* PRs maiores tendem a passar por mais revisões, pois envolvem mais mudanças no código e requerem maior atenção dos revisores.

- **RQ06. Qual a relação entre o tempo de análise dos PRs e o número de revisões realizadas?**  
  *Hipótese:* PRs que ficam mais tempo abertos geralmente acumulam mais revisões, seja por refinamento progressivo ou por necessidade de ajustes após feedbacks.

- **RQ07. Qual a relação entre a descrição dos PRs e o número de revisões realizadas?**  
  *Hipótese:* PRs com descrições mais completas podem receber menos revisões, já que tornam o propósito e as mudanças mais claras, facilitando a aprovação direta.

- **RQ08. Qual a relação entre as interações nos PRs e o número de revisões realizadas?**  
  *Hipótese:* Um maior número de interações tende a estar associado a mais revisões, já que comentários e sugestões frequentemente resultam em novas versões do PR.
 
---

## Metodologia

### 1. Coleta de Dados

Foram selecionados PRs de repositórios que atendem aos seguintes critérios:

- Estão entre os 200 mais populares do GitHub.
- Possuem ao menos 100 PRs com status `merged` ou `closed`.
- Possuem pelo menos uma revisão registrada.
- O tempo entre a criação e o encerramento do PR é superior a 1 hora (para evitar análises automáticas por bots ou pipelines).

A coleta foi realizada por meio da API do GitHub, utilizando scripts próprios automatizados.

---

### 2. Métricas Coletadas

| Dimensão           | Métrica Coletada                                                  |
|--------------------|--------------------------------------------------------------------|
| **Tamanho**         | Número de arquivos modificados, linhas adicionadas e removidas    |
| **Tempo de Análise**| Tempo entre a criação e o fechamento/merge do PR                  |
| **Descrição**       | Número de caracteres no corpo da descrição do PR (em Markdown)    |
| **Interações**      | Número de participantes e número de comentários no PR             |

As análises foram feitas usando valores medianos para sumarização e utilizamos o teste de correlação de Spearman por ser não paramétrico (não exige normalidade dos dados).

---

## Gráficos Gerados e Análise de Dados

## A. Feedback Final das Revisões

### RQ01. Tamanho do PR vs. Status (Merged/Closed)

- **Hipótese:** PRs maiores são mais difíceis de revisar e podem ser rejeitados com mais frequência.  
- **Correlação (linhas adicionadas x status):** ρ = **-0.52**  
- **Correlação (arquivos modificados x status):** ρ = **-0.49**

**Resultado:** Correlação negativa moderada, indicando que PRs maiores têm maior chance de **não serem aceitos**.

---

### RQ02. Tempo de Análise vs. Status

- **Hipótese:** PRs que demoram mais na análise tendem a ser rejeitados.  
- **Correlação (tempo de análise x status):** ρ = **-0.58**

**Resultado:** Correlação negativa moderada/forte. PRs que demoram mais para serem revisados tendem a ser **rejeitados com maior frequência**.

---

### RQ03. Descrição do PR vs. Status

- **Hipótese:** PRs bem descritos tendem a ser aceitos com mais frequência.  
- **Correlação (tamanho da descrição x status):** ρ = **+0.55**

**Resultado:** Correlação positiva moderada. Descrições mais detalhadas estão associadas a **maior taxa de aceitação**.

---

### RQ04. Interações (comentários e participantes) vs. Status

- **Hipótese:** Mais interações indicam maior chance de aceitação (por colaboração), mas podem também indicar problemas.  
- **Correlação (nº de comentários x status):** ρ = **-0.31**  
- **Correlação (nº de participantes x status):** ρ = **+0.25**

**Resultado:**  
- Comentários em excesso estão levemente relacionados à **rejeição**.  
- Mais participantes tendem a contribuir com **aprovação**.

---

## B. Número de Revisões

### RQ05. Tamanho do PR vs. Número de Revisões

- **Hipótese:** PRs maiores passam por mais revisões.  
- **Correlação (linhas adicionadas x nº revisões):** ρ = **+0.80**  
- **Correlação (arquivos modificados x nº revisões):** ρ = **+0.63**

**Resultado:** Correlação forte positiva. PRs maiores exigem mais revisões.

---

### RQ06. Tempo de Análise vs. Número de Revisões

- **Hipótese:** PRs abertos por mais tempo tendem a passar por mais revisões.  
- **Correlação (tempo de análise x nº revisões):** ρ = **+0.63**

**Resultado:** Correlação moderada positiva. Tempo está diretamente ligado ao número de iterações.

---

### RQ07. Descrição do PR vs. Número de Revisões

- **Hipótese:** Descrições completas reduzem a necessidade de revisões.  
- **Correlação (tamanho da descrição x nº revisões):** ρ = **-0.40**

**Resultado:** Correlação negativa moderada. Boas descrições ajudam a evitar múltiplas revisões.

---

### RQ08. Interações vs. Número de Revisões

- **Hipótese:** Mais interações implicam em mais revisões.  
- **Correlação (comentários x nº revisões):** ρ = **+0.45**  
- **Correlação (participantes x nº revisões):** ρ = **+0.41**

**Resultado:** Correlação positiva moderada. Engajamento gera mais iteração — talvez por melhorias progressivas.

---

## 4. Discussão das Hipóteses vs Resultados

| Questão | Hipótese Confirmada? | Comentário |
|--------|------------------------|------------|
| RQ01 | Sim | PRs maiores tendem a ser rejeitados |
| RQ02 | Sim | PRs demorados também são mais rejeitados |
| RQ03 | Sim | Descrições boas ajudam na aprovação |
| RQ04 | Parcial | Mais comentários ≠ aceitação. Mais participantes = melhor |
| RQ05 | Sim | Tamanho influencia diretamente revisões |
| RQ06 | Sim | Revisões prolongadas acumulam mais iterações |
| RQ07 | Sim | Descrição reduz revisões |
| RQ08 | Sim | Mais comentários e participação = mais iterações |

---

## 5. Justificativa Estatística

Utilizou-se o **teste de Spearman** por ser ideal para:

- Dados **não-normais** ou com valores atípicos
- Relações **monotônicas** (uma variável cresce ou decresce com a outra)
- Contextos com **ordenação natural** (como status aceito/rejeitado)

Mais robusto e adequado para análise de repositórios de código reais.

---

## Conclusão

O estudo mostrou que:

- PRs **grandes e vagos** tendem a ser rejeitados e revisados mais vezes.
- PRs **bem descritos e colaborativos** são aceitos com mais frequência e rapidez.
- O **tempo de análise** é um fator importante — revisões longas tendem à rejeição.

---
