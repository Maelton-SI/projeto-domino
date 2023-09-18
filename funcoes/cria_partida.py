from classes.Jogador import Jogador
from classes.Mesa import Mesa
from funcoes.menus import menu_inicial

def cria_partida():
    opcao_menu_inicial = menu_inicial()
    mesa = Mesa()

    if opcao_menu_inicial == 1:
        jogador_um = Jogador()
        jogador_dois = Jogador()

        print()
        nome_jogador_um = str(input("Digite o nome do primeiro jogador: "))
        nome_jogador_dois = str(input("Digite o nome do segundo jogador: "))

        jogador_um.set_nome(nome_jogador_um)
        jogador_dois.set_nome(nome_jogador_dois)

        mesa.add_jogador(jogador_um)
        mesa.add_jogador(jogador_dois)

        return mesa

    elif opcao_menu_inicial == 2:
        jogador_um = Jogador()
        jogador_dois = Jogador()
        jogador_tres = Jogador()

        print()
        nome_jogador_um = str(input("Digite o nome do primeiro jogador: "))
        nome_jogador_dois = str(input("Digite o nome do segundo jogador: "))
        nome_jogador_tres = str(input("Digite o nome do terceiro jogador: "))

        jogador_um.set_nome(nome_jogador_um)
        jogador_dois.set_nome(nome_jogador_dois)
        jogador_tres.set_nome(nome_jogador_tres)

        mesa.add_jogador(jogador_um)
        mesa.add_jogador(jogador_dois)
        mesa.add_jogador(jogador_tres)

        return mesa

    elif opcao_menu_inicial == 3:
        jogador_um = Jogador()
        jogador_dois = Jogador()
        jogador_tres = Jogador()
        jogador_quatro = Jogador()

        print()
        nome_jogador_um = str(input("Digite o nome do primeiro jogador: "))
        nome_jogador_dois = str(input("Digite o nome do segundo jogador: "))
        nome_jogador_tres = str(input("Digite o nome do terceiro jogador: "))
        nome_jogador_quatro = str(input("Digite o nome do quarto jogador: "))

        jogador_um.set_nome(nome_jogador_um)
        jogador_dois.set_nome(nome_jogador_dois)
        jogador_tres.set_nome(nome_jogador_tres)
        jogador_quatro.set_nome(nome_jogador_quatro)

        mesa.add_jogador(jogador_um)
        mesa.add_jogador(jogador_dois)
        mesa.add_jogador(jogador_tres)
        mesa.add_jogador(jogador_quatro)

        return mesa

    elif opcao_menu_inicial == 4:
        print("\nObrigado por jogar conosco, até a próxima!\n")
        
        return False
    
if __name__ == "__main__":
    pass