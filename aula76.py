import random

#Variable for iterable
attempts = 0

#List to discover
words = ["casa", "carro", "arvore", "sol", "lua", "rio"]

choicerandom = random.choice(words)

letter_hit = ''


print(f"Olá, vamos jogar um advinha de palavras? \n"
      f"Temos as seguintes palavras na lista para você descobrir: {','.join(words)}\n")


#loop while for the game
while True:

    

    shot = input('\nTente acertar uma letra da palavra: ')


    #logic for discover the word and processing of input erros 
    if len(shot) > 1:
        print("\nDigite apenas uma letra.")
        continue

    elif shot in choicerandom:
        print("\nParabêns, você acertou uma letra da palavra!")
        letter_hit += shot 

    else:
        print("\nErrooou, não existe essa letra na palavra...")


    for secret_letter in choicerandom:
        if secret_letter in letter_hit:
            print(secret_letter)
        else:
            print("*")



    attempts += 1
    print(f"\nJá foram {attempts} tentativas.")

    #Attempt to discover the word and ending the game.
    shotWord = input("\nDeseja tentar chutar a palavra? [S]im ou [N]ão \n").upper().startswith('S')

    if shotWord is True:
        attemptWord = input("\nFaça sua tentativa: ").lower()

        if attemptWord == choicerandom:
            print("\nParabêns, você acertou a palavra, uhuuuul!")
            print(f"Foram {attempts} tentativas. Até a próxima.")
            break

        else:
            print("\nQue pena, não foi dessa vez, tente novamente!")
            continue