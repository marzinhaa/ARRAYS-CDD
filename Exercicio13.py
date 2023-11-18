num = [0] * 30
qtd_pares = 0
soma = 0

for x in range(30):
    num[x] = int(input('Digite um número: '))

maior = num[0]
menor = num[0]
for c in range(30):
    if num[c] % 2 == 0:
        qtd_pares += 1

    soma += num[c]

    if num[c] > maior:
        maior = num[c]
    if num[c] < menor:
        menor = num[c]

media = soma / 30
qtd_media = 0

pares = [0] * qtd_pares
for v in range(30):
    indice_pares = 0
    if num[v] % 2 == 0:
        pares[indice_pares] = num[v]
        indice_pares += 1

    if num[v] > media:
        qtd_media += 1

print(f"Pares: {pares}")
print(f"O maior é {maior} e o menor é {menor}")
print(f"Acima da media: {qtd_media}")