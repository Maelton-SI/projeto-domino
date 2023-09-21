# Projeto-domino
O projeto visa criar um joguinho de dominó para a disciplina de Estrutura de Dados

# Integrantes:
Ana Larissa dos Santos Gomes da Silva <br>
Emesson Horácio dos Santos <br>
Maelton Lima dos Santos <br>

# Relatório Técnico:

## Escolhas de implementação:

    1. Utilizamos listas encadeadas para as peças do dominó, assim como nas mãos 
    dos jogadores, tal como a atividade requer, além da mesa de jogo pois as 
    peças estão endereçadas umas as outras;
    2. Durante o embaralhamento foi utilizado a estrutura deque por permitir 
    a entrada de dados dos dois lados, aumentando a aleatoriedade das peças 
    armazenadas; 
    3. A mesa também foi implementada com um deque pelo mesmo motivo do 
    embaralhamento, por permitir inserir peças através das duas extremidades.

## Estruturas de Dados:

    1. Lista encadeada: a implementação da lista encadeada foi feita modificando 
    o head a cada novo nó, deixando a operação como O(1);
    2. Deque: o deque foi implementado para embaralhamento e para a mesa do jogo. 
    Para o embaralhamento foi utilizanda a função random para trocar a entradas 
    dos dados, caso seja 0 vai entrar no início e se for 1 vai ao fim, 
    embaralhando a ordem;

# Dificuldades:

    1. Implementação das estruturas (deque, lista encadeada);
    2. Acessar os dados na lista encadeada, utilizando ponteiros;
    3. Embaralhar as peças;

# Conclusões:

    1. Conseguimos realizar quase todas as funcionalidade do projeto, com 
    exceção da interação do jogador com o jogo. 
    2. Para a lista encadeada temos:
        2.1. Adicionar O(1) 
        2.2. Embaralhar O(n)
    3. O deque tem o seguinte desempenho: 
        3.1. Adicionar no final é O(1) por ter o tamanho sempre atualizado; 
        3.2. Adicionar no começo é O(n) pois ao adicionar no início as peças 
        seguintes devem ser empurradas para casa seguinte;
        3.3. Deletar o primeiro também é O(n), pois ao deletar o primeiro é
        necessário mover todas as peças uma casa a frente;
        3.4. E por fim deletar o último é O(n).


