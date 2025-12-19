import random

#Variaveis
resposta = True
respostaUsuario = ''
listaOpcoes = ['Validador de CPF', 'Gerador de CPF', 'Sair']
escolhaUsuario = ''
listaCPF = []
cpfGerado = 0
qtdCPF = 0
retornoValidadorCPF = True
retornoGeradorCPF = True



# Função de validação de CPF
def ValidadorDeCPF(cpfInput):
    checkFinal = 0
    


    if len(cpfInput) == 11 and cpfInput != (len(cpfInput)*cpfInput[0]):

        def validacaoCPF_PenultimoNumero(cpfInput):
            
                conjuntoNove = cpfInput[:9]
                iteracaoConjuntoNove = 10
                somaPrimeiraValidacao = 0
                
                    
                for numero in conjuntoNove:
                    somaPrimeiraValidacao += int(numero) * iteracaoConjuntoNove

                    iteracaoConjuntoNove -= 1

                resultadoPrimeiraValidacao = ((somaPrimeiraValidacao * 10) % 11)
                resultadoFinalPrimeiraValidacao = 0 if resultadoPrimeiraValidacao > 9 else resultadoPrimeiraValidacao

                return f'{resultadoFinalPrimeiraValidacao}'


        def validacaoCPF_UltimoNumero(cpfInput):
                conjuntoDez = cpfInput[:10]
                iteracaoConjuntoDez = 11
                somaSegundaValidacao = 0
                
                    
                for numero in conjuntoDez:
                    somaSegundaValidacao += int(numero) * iteracaoConjuntoDez

                    iteracaoConjuntoDez -= 1

                resultadoSegundaValidacao = ((somaSegundaValidacao * 10) % 11)
                resultadoFinalSegundaValidacao = 0 if resultadoSegundaValidacao > 9 else resultadoSegundaValidacao

                return f'{resultadoFinalSegundaValidacao}'
    
        penultimoNumero = validacaoCPF_PenultimoNumero(cpfInput)
        ultimoNumero = validacaoCPF_UltimoNumero(cpfInput)

        checkFinal = penultimoNumero + ultimoNumero

        if checkFinal == cpfInput[-2:]:
             print("CPF válido! 🟢\n")

        else:
            print("CPF inválido! 🔴\n")
             
        

    else:
        print("Insira um CPF válido! ❌\n")

# Função para Gerar CPF
def geradorDeCPF(qtdCPF):
    listaCPF = []

    for _ in range(int(qtdCPF)):
        noveDigitos = ''

        for _ in range(9):
            noveDigitos += str(random.randint(0, 9))    


        #Primeira validação

        iteracaoConjuntoNove = 10
        somaPrimeiraValidacao = 0

        for numero in noveDigitos:
            somaPrimeiraValidacao += int(numero) * iteracaoConjuntoNove
            iteracaoConjuntoNove -= 1

        resultadoPrimeiraValidacao = (somaPrimeiraValidacao * 10) % 11
        primeiroDV = 0 if resultadoPrimeiraValidacao > 9 else resultadoPrimeiraValidacao
        
        dezDigitos = noveDigitos + str(primeiroDV)

        #Segunda validação

        iteracaoConjuntoDez = 11
        somaSegundaValidacao = 0
            
                
        for numero in dezDigitos:
            somaSegundaValidacao += int(numero) * iteracaoConjuntoDez
            iteracaoConjuntoDez -= 1

        resultadoSegundaValidacao = (somaSegundaValidacao * 10) % 11
        segundoDV = 0 if resultadoSegundaValidacao > 9 else resultadoSegundaValidacao

        listaCPF.append(dezDigitos + str(segundoDV))

    return listaCPF

#Menu
while resposta:
    escolhaUsuario = ''
    retornoValidadorCPF = True
    retornoGeradorCPF = True




    print('🔍 Olá,seja bem-vindo!!\n')
    
    for index, opcoes in enumerate(listaOpcoes, start= 1):
         print(f'{index}){opcoes}')

    
    try:
        escolhaUsuario = int(input('\nEscolha uma opção do menu: '))


        if escolhaUsuario > 0 and escolhaUsuario <= 3:

            match escolhaUsuario:
                case 1:
                    while retornoValidadorCPF:  
                        cpfInput =''
                        
                        print("\nValidador de CPF 🕵️")
                        cpfInput = input("\nPor favor, insira o CPF que deseja validar: ").replace('.', '').replace('-', '')

                        ValidadorDeCPF(cpfInput)

                        respostaUsuario = input("Deseja voltar para o menu? 🤔 ").upper()

                        if respostaUsuario == 'SIM' or respostaUsuario == 'S':
                            retornoValidadorCPF = False
                
                case 2:
                    while retornoGeradorCPF:
                        
                        qtdCPF = input('🪪 Digite a quantidade de CPF que deseja gerar: ')

                        listaGerados = geradorDeCPF(qtdCPF)

                        for cpf in listaGerados:
                            print(cpf)


                        respostaUsuario = input("\nDeseja voltar para o menu? 🤔 ").upper()

                        if respostaUsuario == 'SIM' or respostaUsuario == 'S':
                            retornoGeradorCPF = False
                case _:
                    break
        else: 
            print("\nEscolha um número da lista...")

    except ValueError:
        print("\nOpção inválida. Insira um número! ❌ \n")

