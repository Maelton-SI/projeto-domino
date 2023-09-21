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

            '''Se houver empate a rodada vai trazer uma tupla com a lista de jogadores, e essa condição 
            irá comparar o somatório de peças de cada um dos jogadores para definir o vencedor'''

            if type(rodada) == tuple:
                vencedor = 'EMPATE'
                qtd_jogadores = rodada[1].size
                jogador_atual = rodada[1].head
                for i in range(0, qtd_jogadores):
                    proximo_jogador = jogador_atual.getProximo()
                    if jogador_atual.dados.get_somatorio_pecas() > proximo_jogador.dados.get_somatorio_pecas():
                        vencedor = proximo_jogador.dados.get_nome()
                    elif jogador_atual.dados.get_somatorio_pecas() < proximo_jogador.dados.get_somatorio_pecas():
                        vencedor = jogador_atual.dados.get_nome()
                # print(f'{jogador_atual.dados.get_somatorio_pecas()}, {proximo_jogador.dados.get_somatorio_pecas()}')
                if vencedor != 'EMPATE':
                    print(f'Ganhador(a): {vencedor}')
                else:
                    print('EMPATE')
                # print('EMPATE')
                break
            elif type(rodada) == "Jogador":
                break

if __name__ == "__main__":
    main()