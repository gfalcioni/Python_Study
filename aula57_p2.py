print("Olá, pode me dizer que horas são?")
horas = input("Digite às horas: ")
minutos = input("Digite os minutos: ")


try:
    convertHours = int(horas)
    
    if convertHours >= 18:
        print(f"Boa noite, agora são {horas}:{minutos}")

    elif convertHours >= 12:
        print(f"Boa tarde, agora são {horas}:{minutos}")
        
    elif convertHours >= 00 or 0:
        print(f"Bom dia, agora são {horas}:{minutos}")

except:
    print("Horas incompativeis.")