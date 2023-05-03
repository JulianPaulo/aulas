# TESTE DO PANDAS
produtos = [
    {"Nome": "IPad", "Preco": 1200,"Quantidade": 500},
    {"Nome": "IPhone", "Preco": 8000, "Quantidade": 1000},
    {"Nome": "Airpod", "Preco": 3000, "Quantidade": 800},
    {"Nome": "Applewatch", "Preco": 4000, "Quantidade": 300},
    {"Nome": "Macbook", "Preco": 15000, "Quantidade": 300},
]

import pandas as pd

tabela = pd.DataFrame(produtos)
print(tabela)