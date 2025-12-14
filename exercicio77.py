retorno = True

while retorno:

    somaDoCPF = 0
    contagemSomaCPF = 10
    resultadoFinal = 0

    cpfInput = input("\nOlá, bem-vindo. \nInsira o CPF para validação: ")

    #tratamento do cpf
    if len(cpfInput) <= 11: 
        try:
            cpfTratado = cpfInput.replace('-','').replace('.','')

            noveDigitos = cpfTratado[:9]

            for numero in noveDigitos:
                somaDoCPF += int(numero) * (contagemSomaCPF)
                contagemSomaCPF -= 1
            
            resultadoPenultimoDigito = (somaDoCPF*10) % 11

            if resultadoPenultimoDigito <= 9:
                print(f"\nO penultimo digito do seu CPF é {resultadoPenultimoDigito}")
            else:
                print("\nO penultimo número do seu cpf é 0")
                resultadoPenultimoDigito = 0

            somaDoCPF = 0
            contagemSomaCPF = 11

            dezDigitos = cpfTratado[:10]

            for numero in dezDigitos:
                somaDoCPF += int(numero) * (contagemSomaCPF)
                contagemSomaCPF -= 1
            
            resultadoUltimoDigito = (somaDoCPF*10) % 11

            if resultadoUltimoDigito <= 9:
                print(f"O ultimo digito do seu CPF é {resultadoUltimoDigito}")
            else:
                print("O ultimo número do seu cpf é 0")

            validacaoFinal = str(resultadoPenultimoDigito)+str(resultadoUltimoDigito)

            if validacaoFinal == cpfTratado[9:11]:
                print("\nCPF válido! 🟢")

            else:
                print("\nCPF inválido! 🔴")


            decisao = input("\nDeseja consultar outro CPF? ")

            if decisao.upper() == 'NAO' or decisao.upper() == 'N':
                retorno = False
                

        except ValueError:
            print("Digite um CPF válido! ❌")
        
    else:
        print("\nO CPF contem mais de 11 digitos‼️")
