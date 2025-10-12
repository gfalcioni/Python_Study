def multiplicador(*args):

    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))

    total = a * b

    printando = print(total)

    return printando




multiplicador()

resultado = multiplicador()


def imparPar(*args):
    mensagem = "O número é Par" if resultado % 2 == 0 else "O número é ímpar!"
    print(mensagem)

imparPar()