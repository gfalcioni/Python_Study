nome = input("Digite seu primeiro nome: ")
tamanhonome = len(nome)


if tamanhonome > 1:    
    if tamanhonome > 6:
        print("Seu nome é muito grande!")

    elif tamanhonome >= 5:
        print("Seu nome é normal")

    else:
        print("Seu nome é curto...")
else:
    print("Digite pelo menos uma letra.")