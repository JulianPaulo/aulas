# ----------------------------------------------------------------------------------
# 6. fazer um procedimento que exiba na tela o primeiro e o ultimo elemento do vetor


# ------------- VALORES
v = [34, 6, 57, 3, 45]

def primeiroEUltimo(vetor: list) -> None:
    ultimo = len(vetor)
    print(f"Primeiro : {v[0]}")
    print(f"Ultimo : {v[ultimo - 1]}")

primeiroEUltimo(v)