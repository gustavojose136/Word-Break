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


# Exemplo 1: "applepenapple" pode ser segmentada em "apple" + "pen" + "apple"
s1 = "applepenapple"
word_dict1 = {"apple", "pen"}
print(f"Resultado para '{s1}':", word_break(s1, word_dict1))

# Exemplo 2: "catsandog" não pode ser segmentada corretamente com o dicionário dado
s2 = "catsandog"
word_dict2 = {"cats", "dog", "sand", "and", "cat"}
print(f"Resultado para '{s2}':", word_break(s2, word_dict2))

# Exemplo 3: "catsanddog" pode ser segmentada, por exemplo, em "cats" + "and" + "dog"
s3 = "catsanddog"
word_dict3 = {"cats", "cat", "and", "sand", "dog"}
print(f"Resultado para '{s3}':", word_break(s3, word_dict3))

# Exemplo 4: "pineapplepenapple" pode ser segmentada em "pineapple" + "pen" + "apple"
s4 = "pineapplepenapple"
word_dict4 = {"apple", "pen", "applepen", "pine", "pineapple"}
print(f"Resultado para '{s4}':", word_break(s4, word_dict4))

# Exemplo 5: String vazia deve retornar True (segmentação trivial)
s5 = ""
word_dict5 = {"a", "b"}
print(f"Resultado para string vazia:", word_break(s5, word_dict5))

# Exemplo 6: "abcd" pode ser segmentada em "a" + "b" + "cd"
s6 = "abcd"
word_dict6 = {"a", "abc", "b", "cd"}
print(f"Resultado para '{s6}':", word_break(s6, word_dict6))

# Exemplo 7: "leetcode" pode ser segmentada em "leet" + "code"
s7 = "leetcode"
word_dict7 = {"leet", "code", "le", "etc", "ode"}
print(f"Resultado para '{s7}':", word_break(s7, word_dict7))

# Exemplo 8: "leetcod" não pode ser segmentada completamente com o dicionário fornecido
s8 = "leetcod"
word_dict8 = {"leet", "code", "le", "etc", "ode"}
print(f"Resultado para '{s8}':", word_break(s8, word_dict8))
