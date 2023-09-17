def menu_inicial():
    # print("==============================")
    # print("ESCOLHA A QUANTIDADE DE JOGADORES")
    # print()
    # print("1 - 2 Jogadores")
    # print("2 - 3 Jogadores")
    # print("3 - 4 Jogadores")
    # print("4 - Sair")
    # print()
    # print("==============================")

    print("==============================")
    print("ESCOLHA A QUANTIDADE DE JOGADORES")
    print()
    print("2 Jogadores")
    print("3 Jogadores")
    print("4 Jogadores")
    print("5 - Sair")
    print()
    print("==============================")

    escolha = int(input("> "))

    return escolha

def nome_jogador(n_jogador):
    print('=============================')
    print(f'Jogador {n_jogador}: ')
    nome = input('Digite seu nome > ')
    print('=============================')
    return nome
