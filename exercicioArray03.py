# -------------------------------------------------------------
# 3. Fazer uma função que retorne a soma dos elementos do vetor

# ------------- VALORES
v = [34, 6, 57, 3, 45]

def somaVetores(vetor: int) -> int:
    somavalores = 0
    for i in range(len(vetor)):
        somavalores = somavalores + vetor[i]
    return somavalores

print(somaVetores(v))
