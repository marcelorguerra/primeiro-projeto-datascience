import pandas as pd

dados = {
    "nome": ["Ana", "Bruno", "Carlos", "Daniela"],
    "idade": [25, 31, 42, 29],
    "salario": [5000, 7500, 11000, 6800]
}

df = pd.DataFrame(dados)

print(df)
print("\nEstatísticas:")
print(df.describe())
print("\nSalário médio:")
print(df["salario"].mean())