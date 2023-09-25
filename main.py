from funcoes.cria_partida import cria_partida
from classes.Jogador import Jogador
from estruturas_de_dados.Noh import Noh

def main():
    mesa = cria_partida()
    
    if mesa:
        mesa.distribui_pecas_jogadores()
        # roda o jogo
        while True:
            rodada = mesa.rodada()
            # caso seja empate verifica a soma das peças dos jogadores
            if type(rodada) == tuple:
                print('JOGO TRANCADO!')
                vencedor = 'EMPATE'
                qtd_jogadores = rodada[1].size
                jogador_atual = rodada[1].head
                for i in range(0, qtd_jogadores-1):
                    if qtd_jogadores == 2 and i == 1:
                        break

                    proximo_jogador = jogador_atual.getProximo()
                    if i == 0:
                        if jogador_atual.dados.get_somatorio_pecas() > proximo_jogador.dados.get_somatorio_pecas():
                            vencedor = proximo_jogador
                        elif jogador_atual.dados.get_somatorio_pecas() < proximo_jogador.dados.get_somatorio_pecas():
                            vencedor = jogador_atual
                        
                        
                    elif vencedor == 'EMPATE':
                        if jogador_atual.dados.get_somatorio_pecas() > proximo_jogador.dados.get_somatorio_pecas():
                            vencedor = proximo_jogador
                        
                    else:
                        if vencedor.dados.get_somatorio_pecas() > proximo_jogador.dados.get_somatorio_pecas():
                            vencedor = proximo_jogador
                        elif vencedor.dados.get_somatorio_pecas() == proximo_jogador.dados.get_somatorio_pecas():
                            vencedor = 'EMPATE'
                        
                   
                    jogador_atual = proximo_jogador

                if vencedor != 'EMPATE':
                    print(f'{vencedor.dados.get_nome()} ganhou!')
                else:
                    print('EMPATE')
                break
            
            # verifica se a rodada tem ganhador
            elif type(rodada) == Jogador:
                mesa.imprime_mesa()
                print()
                print(f'{rodada.get_nome()} ganhou!')
                break

if __name__ == "__main__":
    main()