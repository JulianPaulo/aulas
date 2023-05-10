# -------------------------------------------------------------------------------
# 5. Fazer um procedimento que exiba na tela os numeros ímpares contidos no vetor

# ------------ VALORES
v = [34, 6, 57, 3, 45]

def imparVetor(vetor: list) -> None:
    for i in range(len(vetor)):
        if vetor[i] % 2 == 1:
            print(f"vetor[{i}] = {vetor[i]}")

imparVetor(v)