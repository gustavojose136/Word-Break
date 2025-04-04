# Solução para o Problema "Divisão de Palavras (Word Break)"  
Utilizando recursividade, memorization e logs

## Introdução

Neste documento, apresentamos uma solução para o problema de "Divisão de Palavras" que consiste em verificar se uma string pode ser segmentada em palavras válidas presentes em um dicionário. A abordagem utiliza:
- **Recursividade:** Para testar as diversas possibilidades de segmentação da string.
- **memorization:** Para armazenar os resultados de subproblemas já calculados, evitando repetições desnecessárias.

# Explicação da Solução

## 1. Escolha do Problema
O problema de **Divisão de Palavras (Word Break)** é clássico em desafios de programação e entrevistas. Ele consiste em determinar se uma dada string pode ser segmentada em palavras presentes em um dicionário. Essa escolha é interessante porque ilustra bem como a recursividade e a programação dinâmica podem ser aplicadas para evitar o reprocessamento de subproblemas já solucionados.

## 2. Estratégia de Resolução

### Recursividade:
- A função interna `can_break(start)` tenta segmentar a string a partir do índice `start`.
- Para cada posição, ela testa todas as possíveis substrings e, caso a substring esteja no dicionário, realiza uma chamada recursiva para verificar se o restante da string pode ser segmentado.

### memorization:
- Para evitar a recomputação de subproblemas, os resultados já calculados são armazenados em um dicionário (`memo`).
- Antes de processar um índice, o algoritmo verifica se o resultado já foi calculado, o que otimiza a execução, especialmente em casos com muitas sobreposições.

## 3. Implementação do Cache
- O cache é implementado usando um dicionário Python (`dict`), onde:
  - **Chave:** Posição inicial (`start`) da string.
  - **Valor:** Booleano que indica se a string a partir daquela posição pode ser segmentada.
- Essa estrutura permite acesso em tempo O(1), tornando o algoritmo mais eficiente ao evitar recomputações desnecessárias.

## Exemplos de Uso
No código são apresentados quatro exemplos:
- **"applepenapple"** com dicionário `{"apple", "pen"}` – retorna **True**.
- **"catsandog"** com dicionário `{"cats", "dog", "sand", "and", "cat"}` – retorna **False**.
- **"leetcode"** com dicionário `{"leet", "code"}` – retorna **True**.
- **"aaaaaaa"** com dicionário `{"aaaa", "aaa"}` – retorna **True**.