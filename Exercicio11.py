numeros = [0] * 30
for x in range(30):
    numeros[x] = int(input("Digite um número: "))

qntd = 0
num = int(input("Digite o número a ser pesquisado: "))
for c in range(30):
    if num == numeros[c]:
        qntd += 1

print(f"{num} aparece {qntd} vezes na lista")
