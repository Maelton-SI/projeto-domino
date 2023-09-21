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

            if type(rodada) == tuple:
                print('JOGO TRANCADO!')
                vencedor = 'EMPATE'
                qtd_jogadores = rodada[1].size
                jogador_atual = rodada[1].head
                for i in range(0, qtd_jogadores):
                    if qtd_jogadores == 2 and i == 1:
                        break

                    proximo_jogador = jogador_atual.getProximo()
                    if vencedor == 'EMPATE':
                        if jogador_atual.dados.get_somatorio_pecas() > proximo_jogador.dados.get_somatorio_pecas():
                            vencedor = proximo_jogador
                        elif jogador_atual.dados.get_somatorio_pecas() < proximo_jogador.dados.get_somatorio_pecas():
                            vencedor = jogador_atual
                    else:
                        if vencedor.dados.get_somatorio_pecas() > jogador_atual.dados.get_somatorio_pecas():
                            vencedor = jogador_atual
                   
                    jogador_atual = proximo_jogador

                if vencedor != 'EMPATE':
                    print(f'{vencedor.dados.get_nome()} ganhou!')
                else:
                    print('EMPATE')
                break
        
            elif type(rodada) == Jogador:
                # mesa.imprime_pecas_jogadores()
                mesa.imprime_mesa()
                print()
                print(f'{rodada.get_nome()} ganhou!')
                break

if __name__ == "__main__":
    main()