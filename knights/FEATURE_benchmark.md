# Feature: Benchmark e Medição de Desempenho de Inferência

## 1. Descrição e Enquadramento
O algoritmo `model_check` implementado no ficheiro `logic.py` fundamenta-se na verificação exaustiva de modelos através de uma árvore de recursão booleana. Para uma consulta, o número de modelos considerados cresce como $2^n$, onde $n$ é o total de símbolos proposicionais na base de conhecimento e na consulta.

Esta funcionalidade introduz um script independente (`benchmark.py`) que mede o tempo médio de resolução de cada puzzle, em milissegundos. Cada puzzle é consultado apenas quanto aos símbolos dos personagens que nele participam.

## 2. Implementação Técnica
* **Ficheiro:** `benchmark.py`
* **Branch Git:** `feature/puzzle-benchmark`
* **Mecanismo de Temporização:** Utilização de `time.perf_counter()`, relógio monótono de alta resolução, para medir 1000 resoluções de cada puzzle e apresentar a média por resolução.
* **Isolamento:** O script consome as variáveis de conhecimento exportadas por `puzzle.py` sem interferir com os testes formais do validador `check50`.

## 3. Como Executar
```bash
python benchmark.py
```

## 4. Interpretação dos Resultados
* **Puzzle 0 (2 símbolos):** até $2^2 = 4$ modelos por consulta.
* **Puzzles 1 e 2 (4 símbolos):** até $2^4 = 16$ modelos por consulta.
* **Puzzle 3 (6 símbolos):** até $2^6 = 64$ modelos por consulta.

Os tempos dependem do computador e da carga do sistema; por isso, o script apresenta médias obtidas localmente, sem assumir valores fixos. Cada resolução verifica todos os símbolos do puzzle e, para cada símbolo, executa uma consulta a `model_check`.

## 5. Apoio de Ferramentas de IA
* **Ferramenta:** IA Generativa (LLM).
* **Função:** Apoio na estruturação do benchmark com `perf_counter` e elaboração da apresentação dos resultados no terminal.