from funcoes.cria_partida import cria_partida
from classes.Jogador import Jogador

def main():
    mesa = cria_partida()
    mesa.distribui_pecas_jogadores()
    mesa.imprime_pecas_jogadores()

if __name__ == "__main__":
    main()