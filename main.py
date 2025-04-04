def word_break(s, word_dict):
    # Cache para armazenar os resultados intermediários
    memo = {}

    def can_break(start):
        # Caso base: se atingirmos o final da string, a segmentação foi bem-sucedida
        if start == len(s):
            return True
        
        # Verifica se o resultado para a posição atual já está no cache
        if start in memo:
            return memo[start]
        
        # Tenta segmentar a string de 'start' até o final
        for end in range(start + 1, len(s) + 1):
            # Se a substring atual está no dicionário
            if s[start:end] in word_dict:
                # Chamada recursiva para o restante da string
                if can_break(end):
                    memo[start] = True
                    return True
        
        # Se não foi possível segmentar, armazena o resultado no cache e retorna False
        memo[start] = False
        return False

    return can_break(0)


# Exemplos de uso:

s1 = "applepenapple"
word_dict1 = {"apple", "pen"}
print(f"Resultado para '{s1}':", word_break(s1, word_dict1))

s2 = "catsandog"
word_dict2 = {"cats", "dog", "sand", "and", "cat"}
print(f"Resultado para '{s2}':", word_break(s2, word_dict2))
