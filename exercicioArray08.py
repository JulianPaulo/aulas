# ----------------------------------------------------------------------------------------------------
# 8. Fazer uma função que retorne True caso um valor passado por parâmetro exista no vetor, senão False

vetor = int(input("Valores contidos no vetor: "))
v = [1, 34, 6, 57, 3, 45]

def analiseVetorTrueFalse(vetor: int, v: list) -> int:
    num = 0
    for i in range(len(v)):
        num = num + 1
    if vetor == v[i]:
        return True
    elif vetor != v[i]:
        return False

analise = analiseVetorTrueFalse(vetor, v)
print(analise)
