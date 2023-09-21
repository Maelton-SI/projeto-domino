from funcoes.cria_partida import cria_partida
from classes.Jogador import Jogador
from estruturas_de_dados.Noh import Noh
from classes.Mesa import Mesa
from estruturas_de_dados.ListaEncadeada import ListaEncadeada

def main():
    mesa = cria_partida()
    
    if mesa:
        mesa.distribui_pecas_jogadores()

        while True:
            rodada = mesa.rodada()

            if rodada == "EMPATE":
                print("Empate!")
                break
            elif type(rodada) == "Jogador":
                break

if __name__ == "__main__":
    main()