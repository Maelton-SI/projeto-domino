from funcoes.cria_partida import cria_partida

def main():
    mesa = cria_partida()
    
    if mesa:
        mesa.distribui_pecas_jogadores()
        mesa.imprime_mesa()

        mesa.comecar_partida()
        mesa.imprime_mesa()

if __name__ == "__main__":
    main()