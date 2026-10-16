# Feature: Visualizador e Inspetor de Tabelas de Verdade

## 1. Descrição e Enquadramento
O motor padrão de inferência indica se uma dada sentença é consequência lógica da base de conhecimento, omitindo a avaliação dos estados intermédios. 

Esta funcionalidade introduz o script `truth_table.py`, que inspeciona detalhadamente o espaço de estados de cada puzzle, identificando quais os mundos possíveis em que todas as premissas são simultaneamente satisfeitas ($M \models KB$).

## 2. Implementação Técnica
* **Ficheiro:** `truth_table.py`
* **Branch Git:** `feature/truth-table`
* **Álgebra Combinatória:** Emprego de `itertools.product` para geração sistemática das $2^n$ combinações de valores de verdade.
* **Avaliação de Modelos:** Invocação direta do método `knowledge.evaluate(model)` para cada linha da tabela.
* **Apresentação em Dois Níveis:**
  1. **Vista de Terminal (Compacta):** Filtragem seletiva que exibe apenas as linhas correspondentes a modelos consistentes (evitando poluição na consola com 64 linhas no Puzzle 3).
  2. **Exportação HTML (`truth_tables.html`):** Geração automática de documento estruturado com estilos CSS e realce a verde dos modelos válidos para consulta no navegador.

## 3. Como Executar
```bash
python truth_table.py
```

## 4. Apoio de Ferramentas de IA
* **Ferramenta:** IA Generativa (LLM).
* **Função:** Depuração do emparelhamento de tipos de dados nos dicionários de modelos e geração do template HTML de exportação.