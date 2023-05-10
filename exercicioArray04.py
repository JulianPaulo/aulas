# 4. Fazer uma função que retorne a media dos elementos do vetor

v = [34, 6, 57, 3, 45]

def somaVetores(vetor: list) -> list:
    somaValores = 0
    for i in range(len(vetor)):
        somaValores = somaValores + vetor[i]
    media = somaValores / (i + 1)
    return media

print(somaVetores(v))
