import time
from logic import model_check
import puzzle


def benchmark_puzzle(name, knowledge, symbols):
    """Mede o tempo necessário para o model_check avaliar um puzzle."""
    start_time = time.perf_counter()

    # Executa a verificação para todos os símbolos (exatamente como o main() do puzzle.py)
    results = []
    for symbol in symbols:
        if model_check(knowledge, symbol):
            results.append(str(symbol))

    elapsed_time = time.perf_counter() - start_time
    return results, elapsed_time


def main():
    symbols = [
        puzzle.AKnight, puzzle.AKnave,
        puzzle.BKnight, puzzle.BKnave,
        puzzle.CKnight, puzzle.CKnave
    ]

    puzzles = [
        ("Puzzle 0", puzzle.knowledge0),
        ("Puzzle 1", puzzle.knowledge1),
        ("Puzzle 2", puzzle.knowledge2),
        ("Puzzle 3", puzzle.knowledge3)
    ]

    print("=" * 45)
    print("  BENCHMARK DE RESOLUÇÃO (MODEL CHECKING)")
    print("=" * 45)

    total_time = 0.0

    for name, knowledge in puzzles:
        results, duration = benchmark_puzzle(name, knowledge, symbols)
        total_time += duration

        print(f"\n{name}:")
        for res in results:
            print(f"  {res}")
        print(f"  --> Tempo de execução: {duration * 1000:.4f} ms")

    print("\n" + "-" * 45)
    print(f"Tempo total decorrido: {total_time * 1000:.4f} ms")
    print("=" * 45)


if __name__ == "__main__":
    main()