#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.


preco = float(input("Digite o preço do produto: "))
novo_preco = preco * 0.95

print(f"O valor do produto é R${preco:.2f}, mas com os 5% de desconto fica R${novo_preco:.2f}.")
