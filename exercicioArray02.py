# ---------------------------------------------------------------------------------
# 2. Fazer um procedimento que exiba somente os numeros negativos contidos no vetor

# ------------ VALORES
v = [34, -6, 57, 3, 45]

# ------------------------------- SUBALGORITMOS
def numerosNegativosArray(vetor: list) -> None:
    for i in range(len(vetor)):
        if v[i] < 0:
            print(v[i])

# -------------------------- PROGRAMA PRINCIPAL

numerosNegativosArray(v)