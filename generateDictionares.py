#!/usr/bin/env python3
def generate_partitions(word):
    """
    Gera todas as possíveis divisões de uma palavra.
    
    Cada divisão corresponde a uma forma de inserir espaços entre os caracteres da palavra.
    Por exemplo, para a palavra "abc", as divisões são:
      - "a b c"
      - "a bc"
      - "ab c"
      - "abc"
    """
    partitions = []
    
    def backtrack(start, current):
        # Caso base: se atingimos o final da palavra, junta as partes e armazena a divisão
        if start == len(word):
            partitions.append(" ".join(current))
            return
        # Tenta todas as possíveis divisões a partir do índice 'start'
        for end in range(start + 1, len(word) + 1):
            current.append(word[start:end])
            backtrack(end, current)
            current.pop()
    
    backtrack(0, [])
    return partitions


def run_examples():
    # Limite para impressão: se o número de divisões for alto, mostra apenas os primeiros N.
    max_to_print = 20

    # Lista de exemplos, incluindo alguns exemplos mais complexos
    examples = [
        "a",          # Palavra com 1 caractere
        "ab",         # 2^(2-1) = 2 divisões: "a b" e "ab"
        "abc",        # 2^(3-1) = 4 divisões
        "dog",        # 4 divisões
        "cat",        # 4 divisões
        "hi",         # 2 divisões
        "py",         # 2 divisões
        "sun",        # 4 divisões
        "fun",        # 4 divisões
        "code",       # 2^(4-1) = 8 divisões
        "complex",    # 2^(7-1) = 64 divisões
        "algorithm",  # 2^(9-1) = 256 divisões
        "recursion",  # 2^(9-1) = 256 divisões
        "dynamic",    # 2^(7-1) = 64 divisões
        "programming", # 2^(11-1) = 1024 divisões
        "AlexandreDeMoraes", # 2^(17-1) = 65536 divisões
        "XandaoAmaEllonMusk", # 2^(17-1) = 65536 divisões
        "supercalifragilisticexpialidocious", # 2^(34-1) = 17179869184 divisões
    ]
    
    for word in examples:
        partitions = generate_partitions(word)
        total = len(partitions)
        print(f"Palavra: '{word}'")
        print(f"Número total de divisões: {total}")
        print("Divisões:")
        # Se houver muitas divisões, mostra apenas os primeiros max_to_print
        if total > max_to_print:
            for part in partitions[:max_to_print]:
                print(f"  - {part}")
            print(f"... mostrando apenas os primeiros {max_to_print} de {total} divisões.")
        else:
            for part in partitions:
                print(f"  - {part}")
        print("-" * 50)


if __name__ == "__main__":
    run_examples()
