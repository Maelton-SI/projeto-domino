from funcoes.cria_partida import cria_partida
from classes.Jogador import Jogador
from estruturas_de_dados.Noh import Noh

def test():
    maelton = Jogador("Maelton")

    maelton.pega_peca((0,0))
    maelton.imprime_pecas()

    maelton.pega_peca((1,1))
    maelton.imprime_pecas()

    print(f"tenho: {maelton.pecas.size} peças.")

    print("\njoguei")
    maelton.jogar(2,0)
    maelton.imprime_pecas()

    print(maelton.pecas.size)

def main():
    mesa = cria_partida()
    
    if mesa:
        mesa.distribui_pecas_jogadores()

        while True:
            rodada = mesa.rodada()

            if rodada == "EMPATE":
                print('EMPATE')
                break
            elif type(rodada) == "Jogador":
                break

if __name__ == "__main__":
    main()