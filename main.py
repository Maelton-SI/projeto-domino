from classes.Domino import Domino
from funcoes.menus import *
from classes.Jogador import *

d = Domino()
d.imprime_domino()
global qtd_jogadores
while True:
    qtd_jogadores = menu_inicial()
    peca_atual = d.pecas.head.getDados()
    if qtd_jogadores == 2:
        jogador1 = Jogador()
        jogador1.nome = nome_jogador(1)
        jogador2 = Jogador()
        jogador2.nome = nome_jogador(2)
        for i in range(0, 7):
            if i == 0:
                jogador1.pecas.add(peca_atual)
                peca_atual = d.pecas.head.getProximo()
                jogador2.pecas.add(peca_atual.getDados())
            else:
                peca_atual = peca_atual.getProximo()
                jogador1.pecas.add(peca_atual.getDados())
                peca_atual = peca_atual.getProximo()
                jogador2.pecas.add(peca_atual.getDados())
        break
    elif qtd_jogadores == 3:
        jogador1 = Jogador()
        jogador1.nome = nome_jogador(1)
        jogador2 = Jogador()
        jogador2.nome = nome_jogador(2)
        jogador3 = Jogador()
        jogador3.nome = nome_jogador(3)
        for i in range(0, 7):
            if i == 0:
                jogador1.pecas.add(peca_atual)
                peca_atual = d.pecas.head.getProximo()
                jogador2.pecas.add(peca_atual.getDados())
                peca_atual = peca_atual.getProximo()
                jogador3.pecas.add(peca_atual.getDados())
            else:
                peca_atual = peca_atual.getProximo()
                jogador1.pecas.add(peca_atual.getDados())
                peca_atual = peca_atual.getProximo()
                jogador2.pecas.add(peca_atual.getDados())
                peca_atual = peca_atual.getProximo()
                jogador3.pecas.add(peca_atual.getDados())
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
        for i in range(0, 7):
            if i == 0:
                jogador1.pecas.add(peca_atual)
                peca_atual = d.pecas.head.getProximo()
                jogador2.pecas.add(peca_atual.getDados())
                peca_atual = peca_atual.getProximo()
                jogador3.pecas.add(peca_atual.getDados())
                peca_atual = peca_atual.getProximo()
                jogador4.pecas.add(peca_atual.getDados())
            else:
                peca_atual = peca_atual.getProximo()
                jogador1.pecas.add(peca_atual.getDados())
                peca_atual = peca_atual.getProximo()
                jogador2.pecas.add(peca_atual.getDados())
                peca_atual = peca_atual.getProximo()
                jogador3.pecas.add(peca_atual.getDados())
                peca_atual = peca_atual.getProximo()
                jogador4.pecas.add(peca_atual.getDados())
        break
    else:
        print('Opção inválida')

if qtd_jogadores == 2:
    print(jogador1.nome)
    jogador1.imprime_pecas()
    print(jogador2.nome)
    jogador2.imprime_pecas()
elif qtd_jogadores == 3:
    print(jogador1.nome)
    jogador1.imprime_pecas()
    print(jogador2.nome)
    jogador2.imprime_pecas()
    print(jogador3.nome)
    jogador3.imprime_pecas()
elif qtd_jogadores == 4:
    print(jogador1.nome)
    jogador1.imprime_pecas()
    print(jogador2.nome)
    jogador2.imprime_pecas()
    print(jogador3.nome)
    jogador3.imprime_pecas()
    print(jogador4.nome)
    jogador4.imprime_pecas()