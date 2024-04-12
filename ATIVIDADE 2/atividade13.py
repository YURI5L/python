
lista_compras = [
    {"descricao": "Notebook", "preco": 2500.00},
    {"descricao": "Smartphone", "preco": 1500.00},
    {"descricao": "Fone de ouvido", "preco": 200.00},
    {"descricao": "Mouse", "preco": 80.00},
    {"descricao": "Teclado", "preco": 150.00}
]


print("Lista de Compras:")
for produto in lista_compras:
    print(f"Descrição: {produto['descricao']} - Preço: R${produto['preco']:.2f}")
