#Calculadora infinita

choice = True

while choice:
    firstnumber = input("Please, insert the first number: ")
    secondnumber = input("Please, insert the second number: ")
    operator = input("Please, choose the desired operator [+ , - , * , / or : , % , **]: ")

    if firstnumber.replace('.','',1).isdigit() and secondnumber.replace('.','',1).isdigit():
        firstnumberconvert = float(firstnumber)
        secondnumberconvert = float(secondnumber)


        match operator:

            case '+':
                print(firstnumberconvert + secondnumberconvert)
            
            
            case '-':
                print(firstnumberconvert - secondnumberconvert)           
            
            case '*':
                print(firstnumberconvert * secondnumberconvert)
            
            
            case '/' | ':':
                print(firstnumberconvert / secondnumberconvert)
            
            case '%':
                print(firstnumberconvert % secondnumberconvert)
            
            
            case '**':
                print(firstnumberconvert ** secondnumberconvert)
                
            case _:
                print("Esse não é um operador válido!")

    else:
        print("Você não digitou números validos.")

    option = input("Deseja sair? [S/N]").upper().startswith('S')
    
    if option is True:
        break




