def menu_inicial():
    while True:
        print("==============================")
        print("ESCOLHA A QUANTIDADE DE JOGADORES")
        print()
        print("1 - Dois Jogadores")
        print("2 - Três Jogadores")
        print("3 - Quatro Jogadores")
        print("4 - Sair")
        print()
        print("==============================")

        escolha = int(input("> "))
        
        if escolha in [1,2,3,4]:
            return escolha
        else:
            print('Opção inválida, tente novamente!\n')

if __name__ == "__main__":
    pass