# -------------------------------------------------------------------------
# 7. Fazer um procedimento que exiba os elementos cujos índices sejam pares

# ------------ VALORES
v = [34, 6, 57, 3, 45]

def vetorPar(vetor: list) -> None:
    for i in range(len(vetor)):
        if i % 2 == 0:
            print(f"vetor[{i}]")

vetorPar(v)