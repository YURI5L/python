
lista_compras = [
    {"descricao": "Notebook", "preco": 2500.00},
    {"descricao": "Smartphone", "preco": 1500.00},
    {"descricao": "Fone de ouvido", "preco": 200.00},
    {"descricao": "Mouse", "preco": 80.00},
    {"descricao": "Teclado", "preco": 150.00}
]


produto_mais_caro = max(lista_compras, key=lambda x: x["preco"])
produto_mais_barato = min(lista_compras, key=lambda x: x["preco"])


print("Produto mais caro:")
print(f"Descrição: {produto_mais_caro['descricao']} - Preço: R${produto_mais_caro['preco']:.2f}")

print("\nProduto mais barato:")
print(f"Descrição: {produto_mais_barato['descricao']} - Preço: R${produto_mais_barato['preco']:.2f}")
