# LAB03 - Análise de Code Review no GitHub

**Disciplina:** Laboratório de Experimentação de Software  
**Professor:** João Paulo Carneiro Aramuni  
**Grupo:** Letícia Rodrigues Blom e Júlia Borges Araújo Silva

---

## Contexto

No GitHub, revisões de código são feitas por meio de **pull requests**, onde desenvolvedores propõem alterações no código e colaboradores do projeto realizam a revisão antes de integrá-lo à branch principal. Essa análise pode envolver revisores humanos e ferramentas automáticas (bots e CI/CD). Neste projeto, consideramos apenas revisões humanas, com pelo menos 1 hora de duração e 1 revisão registrada.

---

## Objetivo

Este laboratório tem como objetivo analisar a atividade de **code review** em repositórios populares do GitHub. O foco está em identificar variáveis que influenciam o sucesso de um *pull request* (PR), ou seja, se ele é aceito (merged) ou rejeitado (closed), e o número de revisões que ele recebe durante o processo.

---

## Metodologia

### 1. Coleta de Dados

Selecionamos PRs de repositórios que:

- Estão entre os **200 mais populares** do GitHub.
- Possuem **pelo menos 100 PRs** (merged + closed).
- Têm **status** `MERGED` ou `CLOSED`.
- Possuem **pelo menos uma revisão**.
- O tempo entre a criação e o encerramento do PR é **maior que 1 hora** (para excluir bots e automações).

A coleta foi realizada utilizando a API do GitHub e scripts próprios para automatizar o processo.

### 2. Métricas Coletadas

| Dimensão       | Métrica                                                 |
|----------------|----------------------------------------------------------|
| Tamanho        | Nº de arquivos, linhas adicionadas e removidas          |
| Tempo de Análise | Tempo entre criação e fechamento/merge do PR           |
| Descrição      | Nº de caracteres no corpo da descrição do PR (Markdown) |
| Interações     | Nº de participantes e comentários no PR                 |

### 3. Questões de Pesquisa

#### A. Feedback Final (Status do PR)
- **RQ01:** Tamanho do PR influencia o status (merged/closed)?
- **RQ02:** Tempo de análise influencia o status?
- **RQ03:** Descrição influencia o status?
- **RQ04:** Interações influenciam o status?

#### B. Número de Revisões
- **RQ05:** Tamanho influencia o nº de revisões?
- **RQ06:** Tempo de análise influencia o nº de revisões?
- **RQ07:** Descrição influencia o nº de revisões?
- **RQ08:** Interações influenciam o nº de revisões?

---

## Análise de Dados

As correlações entre as variáveis serão avaliadas utilizando testes estatísticos como:

- **Correlação de Spearman** (para variáveis ordinais ou não-normalizadas)
- **Correlação de Pearson** (para variáveis contínuas com distribuição normal)

A escolha do teste será justificada com base na distribuição dos dados.

---
