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
                for i in range(1, qtd_jogadores):
                    proximo_jogador = jogador_atual.getProximo()
                    if vencedor == 'EMPATE':
                        print('entrou no if')
                        print(vencedor)
                        if jogador_atual.dados.get_somatorio_pecas() > proximo_jogador.dados.get_somatorio_pecas():
                            # vencedor = proximo_jogador.dados.get_nome()
                            vencedor = proximo_jogador
                        elif jogador_atual.dados.get_somatorio_pecas() < proximo_jogador.dados.get_somatorio_pecas():
                            # vencedor = jogador_atual.dados.get_nome()
                            vencedor = jogador_atual
                    else:
                        print('entrou no else')
                        print(vencedor.dados.get_nome())
                        if vencedor.dados.get_somatorio_pecas() > jogador_atual.dados.get_somatorio_pecas():
                            vencedor = jogador_atual
                        # elif jogador_atual.dados.get_somatorio_pecas() < proximo_jogador.dados.get_somatorio_pecas():
                        #     vencedor = jogador_atual.dados.get_nome()
                   
                    jogador_atual = proximo_jogador

                print(type(vencedor))
                if vencedor != 'EMPATE':
                    # print(f'Ganhador(a): {vencedor}')
                    print(f'Ganhador(a): {vencedor.dados.get_nome()}')
                else:
                    print('EMPATE')
                break
        
            elif type(rodada) == Jogador:
                break

if __name__ == "__main__":
    main()