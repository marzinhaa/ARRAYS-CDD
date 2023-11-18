login = [0,0,0,0,0]
senha = [0,0,0,0,0]

for x in range(5):
    login[x] = input(f"Qual o login do {1+x}° usuario: ")
    senha[x] = input(f"Qual a senha {1+x}° usuario: ")

cont = 0
while cont < 3:
    verificador_login = input("Login: ")
    for c in range(5):
        if login[c] == verificador_login:
            cont = 3
            print("O usuario está correto")
            for c in range(3):
                verificador_senha = input("Senha:")
                if verificador_senha == senha[c]:
                    print("Login realizado!")
                    break
                else:
                    print("Senha invalida")
    if cont < 3:
        print("Usuario invalido")
    cont += 1