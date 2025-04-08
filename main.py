import time

def word_break_with_memo(s, word_dict):
    memo = {}

    def can_break(start):
        if start == len(s):
            return True

        if start in memo:
            return memo[start]

        for end in range(start + 1, len(s) + 1):
            if s[start:end] in word_dict and can_break(end):
                memo[start] = True
                return True

        memo[start] = False
        return False

    return can_break(0)

def word_break_without_memo(s, word_dict):
    def can_break(start):
        if start == len(s):
            return True

        for end in range(start + 1, len(s) + 1):
            if s[start:end] in word_dict and can_break(end):
                return True

        return False

    return can_break(0)

def run_test_case(s, word_dict, num_runs=1000):
    total_time_memo = 0
    result_memo = None
    min_time_memo = float('inf')

    for _ in range(num_runs):
        start_time = time.perf_counter()
        result_memo = word_break_with_memo(s, word_dict)
        elapsed = time.perf_counter() - start_time
        total_time_memo += elapsed
        min_time_memo = min(min_time_memo, elapsed)

    avg_time_memo = (total_time_memo / num_runs) * 1000  

    total_time_no_memo = 0
    result_no_memo = None
    min_time_no_memo = float('inf')

    for _ in range(num_runs):
        start_time = time.perf_counter()
        result_no_memo = word_break_without_memo(s, word_dict)
        elapsed = time.perf_counter() - start_time
        total_time_no_memo += elapsed
        min_time_no_memo = min(min_time_no_memo, elapsed)

    avg_time_no_memo = (total_time_no_memo / num_runs) * 1000  # Convert to milliseconds

    return result_memo, avg_time_memo, result_no_memo, avg_time_no_memo, min_time_memo * 1000, min_time_no_memo * 1000

test_cases = [
    ("applepenapple", {"apple", "pen"}, "Caso 1: Concatenação simples"),
    ("catsandog", {"cats", "dog", "sand", "and", "cat"}, "Caso 2: Segmentação impossível"),
    ("pineapplepenapple", {"apple", "pen", "applepen", "pine", "pineapple"}, "Caso 3: Múltiplas segmentações possíveis"),
    ("", {"a", "b"}, "Caso 4: String vazia"),
    ("aaaaaaa", {"a", "aa", "aaa"}, "Caso 5: Caracteres repetidos"),
    ("leetcode", {"leet", "code"}, "Caso 6: Caso simples com duas palavras"),
    ("aaaaaaaaaaaaaaaaaaaab", {"a", "aa", "aaa", "aaaa"}, "Caso 7: String longa com backtracking"),
    ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", {"a", "aa", "aaa", "aaaa"}, "Caso 8: String muito longa"),
    ("abcdefghijklmnopqrstuvwxyz", {"abc", "def", "ghi", "jklmno", "pqrs", "tuv", "wxyz"}, "Caso 9: Palavras longas")
]

print("Comparação de Desempenho do Algoritmo Word Break\n")
print("Formato: (Resultado, Tempo médio em milissegundos)\n")

valid_speedups = []

for s, word_dict, description in test_cases:
    print(f"\n{description}")
    print(f"String de entrada: '{s}'")
    print(f"Dicionário: {word_dict}")

    result_memo, time_memo, result_no_memo, time_no_memo, min_time_memo, min_time_no_memo = run_test_case(s, word_dict)

    print(f"Com memoização:    ({result_memo}, {time_memo:.3f}ms)")
    print(f"Sem memoização:    ({result_no_memo}, {time_no_memo:.3f}ms)")

    if time_memo > 0.001:  
        speedup = time_no_memo / time_memo
        print(f"Fator de aceleração: {speedup:.2f}x")
        if speedup > 1: 
            valid_speedups.append(speedup)

if valid_speedups:
    avg_speedup = sum(valid_speedups) / len(valid_speedups)
    print(f"\nAceleração média nos casos significativos: {avg_speedup:.2f}x")
