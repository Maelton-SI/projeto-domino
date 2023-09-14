from classes.Domino import Domino
from funcoes.menus import *
from classes.Jogador import *

d = Domino()

while True:
    qtd_jogadores = menu_inicial()
    if qtd_jogadores == 2:
        jogador1 = Jogador()
        jogador1.nome = nome_jogador(1)
        jogador2 = Jogador()
        jogador2.nome = nome_jogador(2)
        break
    elif qtd_jogadores == 3:
        jogador1 = Jogador()
        jogador1.nome = nome_jogador(1)
        jogador2 = Jogador()
        jogador2.nome = nome_jogador(2)
        jogador3 = Jogador()
        jogador3.nome = nome_jogador(3)
        break
    elif qtd_jogadores == 4:
        jogador1 = Jogador()
        jogador1.nome = nome_jogador(1)
        jogador2 = Jogador()
        jogador2.nome = nome_jogador(2)
        jogador3 = Jogador()
        jogador3.nome = nome_jogador(3)
        jogador4 = Jogador()
        jogador4.nome = nome_jogador(4)
        break
    else:
        print('Opção inválida')

print(jogador1.nome)
print(jogador2.nome)
# d.imprime_domino()