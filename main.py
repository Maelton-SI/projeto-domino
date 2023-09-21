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

            if rodada == "EMPATE":
                print('EMPATE')
                break
            elif type(rodada) == "Jogador":
                break

if __name__ == "__main__":
    test2()