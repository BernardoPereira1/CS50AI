"""
Visualizador e Exportador de Tabelas de Verdade.
Apresenta uma vista compacta na consola e exporta a análise completa para HTML.
"""

import itertools
import puzzle


def evaluate_truth_table(title, knowledge, symbols):
    """Calcula todas as combinações e recolhe os modelos válidos."""
    headers = [str(s) for s in symbols]
    total_combinations = 2 ** len(symbols)
    valid_rows = []
    all_rows = []

    for combination in itertools.product([True, False], repeat=len(symbols)):
        model = {}
        for s, val in zip(symbols, combination):
            model[s] = val
            model[str(s)] = val

        is_true = knowledge.evaluate(model)
        row_data = (combination, is_true)
        all_rows.append(row_data)
        if is_true:
            valid_rows.append(row_data)

    return headers, total_combinations, valid_rows, all_rows


def print_cli_summary(title, headers, total_combinations, valid_rows):
    """Imprime uma tabela compacta focada apenas na resolução."""
    print("\n" + "=" * 60)
    print(f"  {title.upper()} (Vista Compacta)")
    print("=" * 60)

    # Nomes curtos para o cabeçalho (ex: AKnight -> A_Kt, AKnave -> A_Kn)
    short_headers = [
        h.replace(" is a Knight", "_Kt").replace(" is a Knave", "_Kn")
        for h in headers
    ]
    header_str = " | ".join(f"{h:^7}" for h in short_headers)
    print(f"{header_str} | KNOWLEDGE")
    print("-" * (len(header_str) + 12))

    for combination, is_true in valid_rows:
        row_str = " | ".join(
            f"{('V' if val else 'F'):^7}" for val in combination
        )
        print(f"{row_str} |  VERDADEIRO  <-- SOLUÇÃO")

    print("-" * (len(header_str) + 12))
    print(f"Combinações testadas: {total_combinations} | "
          f"Modelos consistentes: {len(valid_rows)}")


def generate_html_report(all_puzzle_data, filename="truth_tables.html"):
    """Gera um relatório HTML limpo para visualização no navegador."""
    html = [
        "<!DOCTYPE html>",
        "<html lang='pt'><head><meta charset='UTF-8'>",
        "<title>Tabelas de Verdade - Knights</title>",
        "<style>",
        "body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', "
        "Roboto, sans-serif; margin: 30px; background: #f8fafc; color: #1e293b; }",
        "h1 { color: #0f172a; }",
        "h2 { margin-top: 35px; color: #334155; }",
        "table { border-collapse: collapse; margin-bottom: 20px; "
        "background: #fff; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }",
        "th, td { border: 1px solid #cbd5e1; padding: 6px 12px; text-align: center; }",
        "th { background: #e2e8f0; font-weight: 600; }",
        ".valid { background: #dcfce7; font-weight: bold; color: #166534; }",
        ".meta { font-size: 0.9em; color: #64748b; margin-bottom: 10px; }",
        "</style></head><body>",
        "<h1>Relatório Formal: Análise por Tabelas de Verdade</h1>",
        "<p class='meta'>Inspeção exaustiva do espaço de estados para o projeto Knights.</p>"
    ]

    for title, headers, total_comb, valid_rows, all_rows in all_puzzle_data:
        html.append(f"<h2>{title}</h2>")
        html.append(
            f"<div class='meta'>Combinações: {total_comb} | "
            f"Modelos consistentes: {len(valid_rows)}</div>"
        )
        html.append("<table><thead><tr>")
        for h in headers:
            html.append(f"<th>{h}</th>")
        html.append("<th>Base de Conhecimento</th></tr></thead><tbody>")

        for combination, is_true in all_rows:
            row_class = " class='valid'" if is_true else ""
            html.append(f"<tr{row_class}>")
            for val in combination:
                html.append(f"<td>{'V' if val else 'F'}</td>")
            status = "VERDADEIRO (Solução)" if is_true else "FALSO"
            html.append(f"<td>{status}</td></tr>")

        html.append("</tbody></table>")

    html.append("</body></html>")

    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(html))


def main():
    puzzles = [
        ("Puzzle 0", puzzle.knowledge0, [puzzle.AKnight, puzzle.AKnave]),
        ("Puzzle 1", puzzle.knowledge1, [
            puzzle.AKnight, puzzle.AKnave,
            puzzle.BKnight, puzzle.BKnave
        ]),
        ("Puzzle 2", puzzle.knowledge2, [
            puzzle.AKnight, puzzle.AKnave,
            puzzle.BKnight, puzzle.BKnave
        ]),
        ("Puzzle 3", puzzle.knowledge3, [
            puzzle.AKnight, puzzle.AKnave,
            puzzle.BKnight, puzzle.BKnave,
            puzzle.CKnight, puzzle.CKnave
        ]),
    ]

    reports = []
    for name, knowledge, syms in puzzles:
        headers, total, valid, all_r = evaluate_truth_table(name, knowledge, syms)
        reports.append((name, headers, total, valid, all_r))
        print_cli_summary(name, headers, total, valid)

    generate_html_report(reports)
    print("\n[OK] Ficheiro 'truth_tables.html' gerado com sucesso!")


if __name__ == "__main__":
    main()