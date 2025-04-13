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

---

### 3. Questões de Pesquisa e Hipóteses


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

## Análise de Dados

As relações entre as variáveis serão avaliadas por meio de testes estatísticos, conforme a natureza dos dados:

- **Correlação de Spearman:** Utilizada para variáveis ordinais ou que não seguem uma distribuição normal.
- **Correlação de Pearson:** Utilizada para variáveis contínuas com distribuição normal.

A escolha do teste apropriado será justificada com base em uma análise da distribuição dos dados (utilizando histogramas, boxplots e testes de normalidade).

---
