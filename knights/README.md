# Trabalho Prático 1: Knights (Modelação Proposicional e Inferência)

**Unidade Curricular:** Inteligência Artificial  
**Curso:** Licenciatura em Engenharia de Sistemas e Tecnologias Informáticas (LESTI) — 3.º Ano  
**Instituição:** Universidade do Algarve (UAlg)  
**Ano Letivo:** 2026/2027  
**Docente:** Jaime A. Martins  

---
## 1. Introdução e Enquadramento

O presente trabalho prático enquadra-se no módulo de **Conhecimento e Lógica Proposicional** da unidade curricular de Inteligência Artificial, tendo por base o projeto *Knights* do programa curricular *CS50's Introduction to Artificial Intelligence with Python* da Universidade de Harvard.

O objetivo central consiste em modelar em lógica proposicional os clássicos enigmas lógicos de *Knights and Knaves* (Cavaleiros e Valetes), formulados originalmente pelo matemático Raymond Smullyan:
- **Cavaleiros (*Knights*):** Falam estritamente a verdade em todas as circunstâncias.
- **Valetes (*Knaves*):** Falam estritamente mentiras em todas as circunstâncias.

O objetivo prático não é resolver os enigmas manualmente, mas sim estruturar bases de conhecimento compostas por sentenças lógicas (axiomas do domínio e premissas orais de cada personagem) para que um algoritmo de inferência (`model_check`) determine, de forma automática e formal, a identidade de cada habitante.

---

## 2. Modelação Lógica e Resolução dos Puzzles

Para cada habitante $X$ interveniente nos enigmas, o sistema define duas proposições fundamentais:
- $X_{\text{Knight}}$: "$X$ é Cavaleiro"
- $X_{\text{Knave}}$: "$X$ é Valete"

### 2.1. Axiomas Estruturais da Ilha
Cada habitante tem de pertencer obrigatoriamente a uma classe e não pode pertencer a ambas em simultâneo:
$$\text{Or}(X_{\text{Knight}}, X_{\text{Knave}})$$
$$\text{Not}(\text{And}(X_{\text{Knight}}, X_{\text{Knave}}))$$

### 2.2. Conexão entre Habitante e Afirmação
A correspondência entre a identidade de um habitante e a veracidade do que ele expressa é capturada através do operador de equivalência lógica (**Bicondicional**):
$$\text{Biconditional}(X_{\text{Knight}}, \phi)$$
Onde $\phi$ representa a sentença enunciada pelo habitante $X$. Se $X$ for Cavaleiro ($X_{\text{Knight}} = \text{True}$), $\phi$ é forçada a ser verdadeira; se for Valete ($X_{\text{Knight}} = \text{False}$), $\phi$ tem de ser falsa.

### 2.3. Resumo das Soluções Obtidas
- **Puzzle 0:** A afirma ser simultaneamente cavaleiro e valete $\rightarrow$ **A is a Knave**.
- **Puzzle 1:** A afirma que ambos são valetes; B não fala $\rightarrow$ **A is a Knave**, **B is a Knight**.
- **Puzzle 2:** A afirma que são do mesmo tipo; B afirma que são de tipos diferentes $\rightarrow$ **A is a Knave**, **B is a Knight**.
- **Puzzle 3:** A afirma uma de duas alternativas; B afirma que A disse ser valete e acusa C; C diz que A é cavaleiro $\rightarrow$ **A is a Knight**, **B is a Knave**, **C is a Knight**.

---

## 3. Funcionalidades Extra Desenvolvidas com Apoio de IA

Em conformidade com a grelha de avaliação e a política de desenvolvimento assistido por IA, foram concebidas e implementadas duas funcionalidades modulares em branches dedicados:

### 3.1. Módulo de Benchmark e Medição de Desempenho (`benchmark.py`)
* **Branch:** `feature/puzzle-benchmark`
* **Documentação:** `FEATURE_benchmark.md`
* **Descrição:** Ferramenta de profiling empírico que recorre a `time.perf_counter` para medir a latência do motor `model_check`, demonstrando o impacto do crescimento do número de variáveis booleanas ($2^n$) entre o Puzzle 0 e o Puzzle 3.

### 3.2. Visualizador e Exportador de Tabelas de Verdade (`truth_table.py`)
* **Branch:** `feature/truth-table`
* **Documentação:** `FEATURE_truth_table.md`
* **Descrição:** Ferramenta analítica que gera a exploração exaustiva dos mundos possíveis, avaliando `knowledge.evaluate()` em cada combinação. Imprime uma visualização compacta no terminal com os modelos válidos e exporta um relatório estilizado em `truth_tables.html`.

---

## 4. Declaração e Política de Uso de Inteligência Artificial

Em estrito cumprimento do regulamento e da política institucional da UAlg (RT.89/2026) para a avaliação da componente prática:

- **Ferramentas Utilizadas:** Modelos de Linguagem de Larga Escala (LLM / IA Generativa — ChatGPT e Gemini).
- **Finalidade:** 
  1. Apoio na formulação matemática das premissas e análise da semântica booleana de sentenças compostas.
  2. Implementação das funcionalidades extras (`benchmark.py` e `truth_table.py`) e geração de documentação técnica.
  3. Resolução de incompatibilidades no emparelhamento de tipos de símbolos proposicionais e otimização da apresentação em terminal.
- **Transparência e Domínio:** Toda a lógica gerada com auxílio das ferramentas foi inspecionada, testada com `check50` e assimilada pelo estudante para a respetiva defesa presencial.

### Exemplos de Prompts e Respostas

#### Exemplo 1: Modelação com bicondicional
- **Prompt:** *"Porque é que no bicondicional damos sempre o Knight? Faz diferença se passarmos o Knave?"*
- **Output Resumido da IA:** *"O operador Biconditional(P, Q) impõe P == Q. Se usarmos Biconditional(AKnight, frase), quando AKnight é True a frase é True, e quando AKnight é False a frase é False. Se usássemos AKnave diretamente sem negar a frase, estaríamos a dizer que ser valete equivale a falar a verdade."*

#### Exemplo 2: Otimização de visualização
- **Prompt:** *"A tabela de verdade fica enorme para ver na consola do vscode, não existe outra forma?"*
- **Output Resumido da IA:** *"Podemos adotar duas técnicas de CLI: apresentar por defeito apenas as linhas que correspondem a soluções consistentes no terminal de forma compacta e, em simultâneo, exportar um ficheiro HTML com formatação e realce visual das soluções para consulta no navegador."*

---

## 5. Instruções de Execução

### Resolução dos Puzzles Base:
```bash
python puzzle.py
```

### Execução do Benchmark de Desempenho:
```bash
python benchmark.py
```

### Execução do Visualizador de Tabelas de Verdade:
```bash
python truth_table.py
```

### Validação com Ferramentas CS50:
```bash
check50 ai50/projects/2024/x/knights
style50 puzzle.py
```