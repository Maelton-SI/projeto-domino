from classes.Domino import Domino
from funcoes.menus import *
from classes.Jogador import *
from estrutura_de_dados.Deque import * 

meu_domino = Domino()
opcao_menu_inicial = menu_inicial()

if opcao_menu_inicial == 1:
    jogador_um = Jogador()
    jogador_dois = Jogador()

    nome_jogador_um = str(input("Digite o nome do primeiro jogador: "))
    nome_jogador_dois = str(input("Digite o nome do segundo jogador: "))

    jogador_um.set_nome(nome_jogador_um)
    jogador_dois.set_nome(nome_jogador_dois)

    for _ in range(7):
         jogador_um.pega_peca(meu_domino.remove_proxima_peca())
         jogador_dois.pega_peca(meu_domino.remove_proxima_peca())

elif opcao_menu_inicial == 2:
    jogador_um = Jogador()
    jogador_dois = Jogador()
    jogador_tres = Jogador()

    nome_jogador_um = str(input("Digite o nome do primeiro jogador: "))
    nome_jogador_dois = str(input("Digite o nome do segundo jogador: "))
    nome_jogador_tres = str(input("Digite o nome do terceiro jogador: "))

    jogador_um.set_nome(nome_jogador_um)
    jogador_dois.set_nome(nome_jogador_dois)
    jogador_tres.set_nome(nome_jogador_tres)

    for _ in range(7):
         jogador_um.pega_peca(meu_domino.remove_proxima_peca())
         jogador_dois.pega_peca(meu_domino.remove_proxima_peca())
         jogador_tres.pega_peca(meu_domino.remove_proxima_peca())

elif opcao_menu_inicial == 3:
    jogador_um = Jogador()
    jogador_dois = Jogador()
    jogador_tres = Jogador()
    jogador_quatro = Jogador()

    nome_jogador_um = str(input("Digite o nome do primeiro jogador: "))
    nome_jogador_dois = str(input("Digite o nome do segundo jogador: "))
    nome_jogador_tres = str(input("Digite o nome do terceiro jogador: "))
    nome_jogador_quatro = str(input("Digite o nome do quarto jogador: "))

    jogador_um.set_nome(nome_jogador_um)
    jogador_dois.set_nome(nome_jogador_dois)
    jogador_tres.set_nome(nome_jogador_tres)
    jogador_quatro.set_nome(nome_jogador_quatro)

    for _ in range(7):
         jogador_um.pega_peca(meu_domino.remove_proxima_peca())
         jogador_dois.pega_peca(meu_domino.remove_proxima_peca())
         jogador_tres.pega_peca(meu_domino.remove_proxima_peca())
         jogador_quatro.pega_peca(meu_domino.remove_proxima_peca())

elif opcao_menu_inicial == 4:
    print("Obrigado por jogar conosco, até a próxima!")