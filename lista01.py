print("="*30)
print("      LISTA DE COMPRAS   ")
print("="*30)

lista_compras = []

QtItens = int(input("Quantos itens deseja adicionar na lista? "))

item = 0

while item != QtItens:
    produto = input(f"Digite o nome do {item + 1}º item: ")
    if produto in lista_compras:
        print(f"O item '{produto}' já está na lista de compras.")
    else:
        item += 1
        lista_compras.append(produto)
print("\nSua lista de compras é:")
for indice, produto in enumerate(lista_compras, start=1):
    print(f"{indice}. {produto}")

    
