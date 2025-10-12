numero = input("Por favor, digite um numero inteiro: ")


try:
    inteiro = int(numero)
    if (inteiro%2) == 0:
        print("O número é par!")
    else:
        print("O número é ímpar!")
        
except:
    print("Você não digitou um número inteiro")