from funcoes.cria_partida import cria_partida
from classes.Jogador import Jogador
from estruturas_de_dados.Noh import Noh
from classes.Mesa import Mesa
from estruturas_de_dados.ListaEncadeada import ListaEncadeada

def test():
    maelton = Jogador("Maelton")
    emesson = Jogador("Emesson")

    maelton.pega_peca((0,0))
    emesson.pega_peca((6,6))
    
    jogo = Mesa()
    jogo.add_jogador(maelton)
    jogo.add_jogador(emesson)

    peca = Noh((6,1))
    jogo.add_peca(peca)

    jogo.rodada()

def test2():
    my_list = ListaEncadeada()
    my_list.add("maelton")
    my_list.remove("maelton")

    print(my_list.remove("emesson"))

def main():
    mesa = cria_partida()
    
    if mesa:
        mesa.distribui_pecas_jogadores()

        while True:
            rodada = mesa.rodada()

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

                if vencedor != 'EMPATE':
                    print(f'Ganhador(a): {vencedor}')
                else:
                    print('EMPATE')
        
            elif type(rodada) == "Jogador":
                break

if __name__ == "__main__":
    test2()