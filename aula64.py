entrada = input("Digite seu nome: ")
tamanhonome = len(entrada)

iteravel = 0
nome = ''

# for indice in entrada:
#     nome += (f"{entrada[iteravel]}*")

#     iteravel +=1

#     if nome == ' *':
#         continue

while iteravel < tamanhonome:
    print(entrada[iteravel])
    nome += (f"{entrada[iteravel]}*")

    iteravel += 1

    if nome == " *":
        continue
    
    



print(nome)


