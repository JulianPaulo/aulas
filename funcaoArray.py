"""
EXERCÍCIOS:
1. Fazer uma Função que retorne o primeiro elemento do vetor
2. Fazer um procedimento que exiba somente os numeros negativos contidos no vetor
3. Fazer uma função que retorne a soma dos elementos do vetor
4. Fazer uma função que retorne a media dos elementos do vetos
5. Fazer um procedimento que exiba na tela os numeros ímpares contidos no vetor
6. fazer um procedimento que exiba na tela o primeiro e o ultimo elemento do vetor
7. Fazer um procedimento que exiba os elementos cujos índices sejam pares
8. Fazer uma função que retorne True caso um valor passado por parâmetro esita no vetor, senão False
9. Fazer uma função que ordene os elementos do vetor.
"""

#    0   1   2  3   4  5
v = [34, 6, 57, 3, 45]

# ------ SUBALGORITMOS
def exibe_vetor(vetor: list) -> None:
    for i in range(len(vetor)):
        print(f"v[{i}] = {vetor[i]}")


def ultimo_elemento(vetor: list) -> int:
    ultimo = len(vetor)
    return v[ultimo - 1]

# ------ PROGRAMA PRINCIPAL
exibe_vetor(v)
print(ultimo_elemento(v))
