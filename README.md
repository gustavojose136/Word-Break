# Solução para o Problema "Divisão de Palavras (Word Break)"
Utilizando recursividade, memorization

## Introdução
Neste documento, apresentamos uma solução para o problema de "Divisão de Palavras" que consiste em verificar se uma string pode ser segmentada em palavras válidas presentes em um dicionário. A abordagem utiliza:
- **Recursividade:** Para testar as diversas possibilidades de segmentação da string.
- **Memorization:** Para armazenar os resultados de subproblemas já calculados, evitando repetições desnecessárias.

## Descrição do Problema
O problema de **Divisão de Palavras (Word Break)** é clássico em desafios de programação e entrevistas. Ele consiste em determinar se uma dada string pode ser segmentada em palavras presentes em um dicionário. Essa escolha é interessante porque ilustra bem como a recursividade e a programação dinâmica podem ser aplicadas para evitar o reprocessamento de subproblemas já solucionados.

### Entrada
- Uma string s (sem espaços)
- Um dicionário wordDict contendo palavras válidas

### Saída
- True se a string puder ser segmentada em palavras do dicionário
- False caso contrário

## Estratégia de Resolução

### Recursividade:
- A função interna `can_break(start)` tenta segmentar a string a partir do índice `start`
- Para cada posição, ela testa todas as possíveis substrings e, caso a substring esteja no dicionário, realiza uma chamada recursiva para verificar se o restante da string pode ser segmentado

### Memorization:
- Para evitar a recomputação de subproblemas, os resultados já calculados são armazenados em um dicionário (`memo`)
- Antes de processar um índice, o algoritmo verifica se o resultado já foi calculado, o que otimiza a execução, especialmente em casos com muitas sobreposições

## Análise de Complexidade

### Tempo
- Sem memorization: O(2^n), onde n é o comprimento da string
- Com memorization: O(n^2), onde n é o comprimento da string

### Espaço
- O(n) para o dicionário de memorization
- O(n) para a pilha de recursão
- Total: O(n)

## Exemplos de Uso
```python
# Exemplo 1
s = "applepenapple"
wordDict = {"apple", "pen"}
# Retorna: True

# Exemplo 2
s = "catsandog"
wordDict = {"cats", "dog", "sand", "and", "cat"}
# Retorna: False

# Exemplo 3
s = "leetcode"
wordDict = {"leet", "code"}
# Retorna: True

# Exemplo 4
s = "aaaaaaa"
wordDict = {"aaaa", "aaa"}
# Retorna: True