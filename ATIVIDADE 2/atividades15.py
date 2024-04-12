
pessoas = [
    {"nome": "João", "sobrenome": "Silva"},
    {"nome": "Maria", "sobrenome": "Santos"},
    {"nome": "Pedro", "sobrenome": "Souza"},
    {"nome": "Ana", "sobrenome": "Oliveira"},
    {"nome": "Carlos", "sobrenome": "Ferreira"}
]


print("Nomes das pessoas:")
for pessoa in pessoas:
    nome_completo = f"{pessoa['nome']} {pessoa['sobrenome']}"
    print(nome_completo)
