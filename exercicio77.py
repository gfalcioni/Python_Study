perguntas = [
    {
        'Pergunta': "Quantos é 2+2?",
        'Opções': ['1','3','4','5'],
        'Resposta': '4',
    },

    {
        'Pergunta': 'Quantos é 5x5?',
        'Opções': ['25','55','10','51'],
        'Resposta': '25',
    },

    {
        'Pergunta': 'Quantos é 10/2?',
        'Opções': ['4','5','2','1'],
        'Resposta': '5',

    },
]


for item in perguntas:
    print(item['Pergunta'])

    #Opção que eu fiz sem consultar
    # for opcoes in enumerate(item['Opções'],start=1):
    #     print(f"{opcoes[0]}) {opcoes[1]}")

    #Logica que o professor fez
    for i, opcao in enumerate(item['Opções']):
        print(f"{i})", opcao)

    try:
        resposta = input("Escolha uma opção: ")
        convertido = int(resposta)-1

        
        if item['Opções'][int(convertido)] == item['Resposta']:
            print("Acertou!👍 ")
            print()

        else:
            print('Errou! ❌')
            print()

    except ValueError:
        print("Digite um número 🕵️")

    except IndexError:
        print("Opção inválida, escolha um dos itens da lista 🧐")


