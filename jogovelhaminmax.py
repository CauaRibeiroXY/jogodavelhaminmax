import platform
from random import choice
from os import system




def menu():

    continuar = 1
    while continuar:
        continuar = int(input("0. Sair \n" +
                              "1. Jogar\n"))
        if continuar == 1:
            game()
        else:
            print("Saindo...")
        


def game():
    rodada = 0
    jogada = 0

    while ganhou(board) == 0:
        print("\nJogador ", jogada % 2 + 1)
        exibe()
        if (jogada % 2+1) == 1:
            linha = int(input("\nLinha :"))
            coluna = int(input("Coluna:"))
        else:
            mova = iajoga()
            linha = mova[0]+1
            coluna = mova[1]+1
            print('jogada real', linha, coluna)
        if board[linha-1][coluna-1] == 0:
            if(jogada % 2+1) == 1:
                board[linha-1][coluna-1] = 1
            else:
                board[linha-1][coluna-1] = -1
        else:
            print("Nao esta vazio")
            jogada -= 1
            rodada -= 1
            

        if ganhou(board):
            print("Jogador ", jogada %
                  2 + 1, " ganhou apos ", jogada+1, " rodadas")
            exibe()

        jogada += 1
        rodada += 1
        if rodada == 9:
            print('velha')
            break
    


def ganhou(tabuleiro):
    # checa as linhas
    for i in range(3):
        soma = tabuleiro[i][0]+tabuleiro[i][1]+tabuleiro[i][2]
        if soma == 3 or soma == -3:
            return 1

     # checa as colunas
    for i in range(3):
        soma = tabuleiro[0][i]+tabuleiro[1][i]+tabuleiro[2][i]
        if soma == 3 or soma == -3:
            return 1

    # checa as diagonais
    diagonal1 = tabuleiro[0][0]+tabuleiro[1][1]+tabuleiro[2][2]
    diagonal2 = tabuleiro[0][2]+tabuleiro[1][1]+tabuleiro[2][0]
    if diagonal1 == 3 or diagonal1 == -3 or diagonal2 == 3 or diagonal2 == -3:
        return 1

    return 0


def exibe():
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                print(" _ ", end=' ')
            elif board[i][j] == 1:
                print(" X ", end=' ')
            elif board[i][j] == -1:
                print(" O ", end=' ')

        print()

def custo(tabuleiro):
    #checa as linhas
    for i in range(3):
        soma = tabuleiro[i][0]+tabuleiro[i][1]+tabuleiro[i][2]
        if soma == 3:
            return +1
        elif soma == -3:
            return -1

     # checa as colunas
    for i in range(3):
        soma = tabuleiro[0][i]+tabuleiro[1][i]+tabuleiro[2][i]
        if soma == 3:
            return +1
        elif soma == -3:
            return -1

    # checa as diagonais
    diagonal1 = tabuleiro[0][0]+tabuleiro[1][1]+tabuleiro[2][2]
    diagonal2 = tabuleiro[0][2]+tabuleiro[1][1]+tabuleiro[2][0]
    if diagonal1 == 3 or diagonal2 == 3:
        return +1
    elif diagonal1 == -3 or diagonal2 == -3:
        return -1

    return 0


def acoes(tabuleiro):

    acao = []

    for x, linha in enumerate(tabuleiro):
        for y, lugar in enumerate(linha):
            if lugar == 0:
                acao.append([x, y])

    return acao


def minimax(tabuleiro, rodada, jogador):
    if jogador == 1:
        melhor = [-1, -1, -1000]
    else:
        melhor = [-1, -1, +1000]

    if (rodada == 0 or ganhou(tabuleiro)):
        pontuacao = custo(tabuleiro)
        return [-1, -1, pontuacao]

    for acao in acoes(tabuleiro):
        x, y = acao[0], acao[1]

        tabuleiro[x][y] = jogador
        
        pontuacao = minimax(tabuleiro, rodada - 1, -jogador)
        
        tabuleiro[x][y] = 0
        pontuacao[0], pontuacao[1] = x, y

        if jogador == 1:
            if pontuacao[2] > melhor[2]:
                melhor = pontuacao
        else:
            if pontuacao[2] < melhor[2]:
                melhor = pontuacao
        

    return melhor


def iajoga():
    #qtd de acoes restantes
    rodada = len(acoes(board))
    
    if rodada == 0 or ganhou(board):
        return
    limpa()
    
    move = minimax(board, rodada, -1)
    x, y = move[0], move[1]
    print(move)
    return move




def limpa():

    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')


def limpa_tabuleiro(board):
    board = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    return board

board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
menu()
