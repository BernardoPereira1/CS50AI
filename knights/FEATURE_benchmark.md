# Feature: Benchmark e Medição de Desempenho de Inferência

## 1. Descrição e Enquadramento
O algoritmo `model_check` implementado no ficheiro `logic.py` fundamenta-se na verificação exaustiva de modelos através de uma árvore de recursão booleana. O espaço de estados cresce a uma taxa de $2^n$, onde $n$ é o total de símbolos proposicionais em análise.

Esta funcionalidade introduz um script independente (`benchmark.py`) destinado a quantificar a latência de execução de cada puzzle, fornecendo métricas de tempo em milissegundos.

## 2. Implementação Técnica
* **Ficheiro:** `benchmark.py`
* **Branch Git:** `feature/puzzle-benchmark`
* **Mecanismo de Temporização:** Utilização de `time.perf_counter()`, relógio de precisão monótona do sistema operativo imune a variações do relógio de sistema.
* **Isolamento:** O script consome as variáveis de conhecimento exportadas por `puzzle.py` sem interferir com os testes formais do validador `check50`.

## 3. Como Executar
```bash
python benchmark.py
```

## 4. Análise de Resultados
* **Puzzle 0 (2 símbolos):** Avaliação de 4 atribuições booleanas; tempo médio inferior a 0.15 ms.
* **Puzzles 1 e 2 (4 símbolos):** Avaliação de 16 atribuições booleanas; tempo médio na ordem dos 0.20–0.30 ms.
* **Puzzle 3 (6 símbolos):** Avaliação de 64 atribuições booleanas; observa-se um salto empírico no tempo decorrido, demonstrando a complexidade computacional da inferência por força bruta.

## 5. Apoio de Ferramentas de IA
* **Ferramenta:** IA Generativa (LLM).
* **Função:** Apoio na estruturação do profiler de CPU com `perf_counter` e elaboração da grelha de relatório em terminal.