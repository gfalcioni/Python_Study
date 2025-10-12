"""Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista
Não permite que o programe quebre com eros de indices inexistentes na lista"""

import os , time

listaOpcoes = (
    "Exibir lista de Compras", 
    "Inserir um item na lista de compras", 
    "Deletar um item na lista de Compras",
    "Sair"
)

listaDeCompras = [
    "Arroz",
    "Feijão",
    "Tomate",
    "Alface",
    "Frango",
    "Leite",
    "Pão",
    "Ovos",
    "Café",
    "Sabonete"
]

entradaUsuario = ''

print("\nOlá, seja bem-vindo a sua lista de compras!\n")

while True:


    print("\nPor favor, selecione as seguintes opções:")





    for iteravelListaOpcoes in tuple(enumerate(listaOpcoes,start= 1)):
        indiceItemOpcoes, itemOpcoes = iteravelListaOpcoes
        print(indiceItemOpcoes, itemOpcoes, sep = " - ")

    entradaUsuario = input("\nOpção:")

    print("\n-------------------------------------------\n")
    




    try:

        if entradaUsuario.isdigit() is True and len(entradaUsuario) <= 1 :

            match entradaUsuario:
                
                case '1':
                    for iteravelListaCompras in list(enumerate(listaDeCompras, start= 1)):
                        indiceItemListaCompras , itemListaCompras = iteravelListaCompras
                        print(indiceItemListaCompras,itemListaCompras, sep = ' - ')

                case '2':
                    insertListaDeCompras = input("Digite o item que deseja inserir na lista: \n")
                    listaDeCompras.append(insertListaDeCompras)
                    print(f"Item {insertListaDeCompras} adicionado com sucesso!")
                    print("\n-------------------------------------------\n")

                case '3':
                    entradaDeleteUsuario = input("Insira o número do item da lista: \n")
                    intEntradaUsuario = int(entradaDeleteUsuario) - 1
                    del listaDeCompras[intEntradaUsuario]
                    print(f"Item excluido!")

                case '4':
                    print("Saindo do programa...")
                    time.sleep(5)
                    break
            time.sleep(3)




    except IndexError:
        print("\nPor favor, insira um item que esteja na lista!\n")
        time.sleep(5)
        os.system("clear")