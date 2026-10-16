import time
from logic import model_check
import puzzle

ITERATIONS = 1000


def benchmark_puzzle(knowledge, symbols, iterations):
    """Mede o tempo médio de várias resoluções de um puzzle."""
    start_time = time.perf_counter()

    results = []
    for _ in range(iterations):
        results = [
            str(symbol)
            for symbol in symbols
            if model_check(knowledge, symbol)
        ]

    average_time = (time.perf_counter() - start_time) / iterations
    return results, average_time


def main():
    puzzles = [
        ("Puzzle 0", puzzle.knowledge0, [puzzle.AKnight, puzzle.AKnave]),
        ("Puzzle 1", puzzle.knowledge1, [
            puzzle.AKnight, puzzle.AKnave, puzzle.BKnight, puzzle.BKnave
        ]),
        ("Puzzle 2", puzzle.knowledge2, [
            puzzle.AKnight, puzzle.AKnave, puzzle.BKnight, puzzle.BKnave
        ]),
        ("Puzzle 3", puzzle.knowledge3, [
            puzzle.AKnight, puzzle.AKnave, puzzle.BKnight, puzzle.BKnave,
            puzzle.CKnight, puzzle.CKnave
        ])
    ]

    print("=" * 45)
    print("  BENCHMARK DE RESOLUÇÃO (MODEL CHECKING)")
    print(f"  Média de {ITERATIONS} execuções por puzzle")
    print("=" * 45)

    total_time = 0.0

    for name, knowledge, symbols in puzzles:
        results, duration = benchmark_puzzle(
            knowledge, symbols, ITERATIONS
        )
        total_time += duration

        print(f"\n{name}:")
        print(f"  Símbolos: {len(symbols)}")
        print(f"  Modelos avaliados por consulta: {2 ** len(symbols)}")
        for res in results:
            print(f"  {res}")
        print(f"  --> Tempo médio por resolução: {duration * 1000:.4f} ms")

    print("\n" + "-" * 45)
    print("Soma das médias por puzzle: "
          f"{total_time * 1000:.4f} ms")
    print("=" * 45)


if __name__ == "__main__":
    main()