#regras do jogo da velha

# 1 - jogador 1 = bolinha e o jogador 2 = x
# 2 - cada jogador pode jogar uma vez por turno
# 3 - São 9 espaços no tabuleiro e não pode jogar em um espaço ja utilizado
# 4 - Ganha quem quem prencher 3 espaços consecutivos com bolinha ou x na horizontal, vertical ou diagonal

class NougAndCross:

    def __init__(self):
        self.board =  [[' ',' ',' '],
                       [' ',' ',' '],
                       [' ',' ',' ']]
    def showBoard(self):

        for item in self.board:
            print(' | '.join(item))
            print('-'*9)
    def play(self):
        turn = 0
        ox = 'OX'
        end = False
        while end == False:
            for item in ox:
                try:
                    line = int(input(f'"{item}" Escolha a linha [0,1 ou 2] '))
                    column = int(input(f'"{item}" Escolha a coluna [0, 1 ou 2] '))
                    while play.check(line, column):
                        try:
                            line = int(input(f'{item} Escolha a linha [0, 1 ou 2] '))
                            column = int(input(f'{item} Escolha a coluna [0, 1 ou 2] '))
                        except ValueError:
                            print('Valor inválido')
                        if not play.check(line, column):
                            break
                except ValueError:
                    print('Valor inválido')
                    break
                else:
                    self.board[line][column] = item
                    play.showBoard()
                    if play.victory():
                        print(item, 'ganhou')
                        end = True
                        break
                    turn += 1
                    if turn == 9:
                        print('Empate')
                        end = True
                        break

    def check(self, line, column):
        if line < 0 or line > 2 or column < 0 or column > 2:
            print('Insira um número natural de 0 a 2!')
            return True
        if self.board[line][column] != ' ':
            print('Este espaço já está ocupado!')
            return True

    def victory(self):
        lines = self.board
        columns = list(zip(*lines))
        diagonal1 = [lines[i][i] for i in range(min(len(lines), len(lines[0])))]
        diagonal2 = [lines[i][len(lines) -1 - i] for i in range(min(len(lines), len((lines[0]))))]
        for line in lines:
             if line == ['O','O','O'] or line == ['X','X', 'X']:
                 return True
        for column in columns:
            if column == ('O', 'O', 'O') or column == ('X', 'X', 'X'):
                return True
        if diagonal1 == ['O', 'O', 'O'] or diagonal1 == ['X', 'X', 'X']:
            return True
        if diagonal2 == ['O', 'O', 'O'] or diagonal2 == ['X', 'X', 'X']:
            return True


play = NougAndCross()
play.showBoard()
play.play()

"""
        start = True
        while start:
            self.linha = int(input('Entre com a linha '))
            self.coluna = int(input(('Entre com a coluna')))
            if linha == 0:
                self.linha[self.coluna] =
                start = False
            elif linha == 1:
                self.linha[coluna] = self.ox[0]
                start = False
            elif linha == 2:
                self.linha[coluna] = self.ox[0]
                start = False

            self.atualizar = (f' 0 {self.linha0}\n 1 {self.linha1}\n 2 {self.linha2}')
            print(self.atualizar)
            print('='*50)
            if self.vitoria():
                print('jogador 1 ganhou!')
    def jogadaX(self, linha, coluna):
        self.linha = linha
        self.coluna = coluna
        start = True
        while start:
            if linha == 0:
                self.linha0[coluna] = self.ox[1]
                start = False
            elif linha == 1:
                self.linha1[coluna] = self.ox[1]
                start = False
            if linha == 2:
                self.linha2[coluna] = self.ox[1]
                start = False
        self.atualizar = (f' 0 {self.linha0}\n 1 {self.linha1}\n 2 {self.linha2}')
        print(self.atualizar)
        print('='*50)
        if self.vitoria():
            print('Jogador 2 Ganhou')

    def jogadaCheck(self):
        l1 = self.linha0[self.coluna] == 'O' or self.linha0[self.coluna] == 'X'
        l2 = self.linha1[self.coluna] == 'O' or self.linha1[self.coluna] == 'X'
        l3 = self.linha2[self.coluna] == 'O' or self.linha2[self.coluna] == 'X'
        return l1 or l2 or l3

    def vitoria(self):
        for self.coluna in self.matriz:
            if self.coluna[0] + self.coluna[1] + self.coluna[2] == 'OOO' or\
                    self.coluna[0] + self.coluna[1] + self.coluna[2] == 'XXX':
                return True

        coluna0 = (self.linha0[0] == 'O' , self.linha1[0] == 'O' , self.linha2[0] == 'O')
        coluna1 = (self.linha0[1] == 'O' , self.linha1[1] == 'O' , self.linha2[1] == 'O')
        coluna2 = (self.linha0[2] == 'O', self.linha1[2] == 'O' , self.linha2[2] == 'O')
        coluna3 = (self.linha0[0] == 'X' , self.linha1[0] == 'X' , self.linha2[0] == 'X')
        coluna4 = (self.linha0[1] == 'X' , self.linha1[1] == 'X' , self.linha2[1] == 'X')
        coluna5 = (self.linha0[2] == 'X', self.linha1[2] == 'X' , self.linha2[2] == 'X')
        if all(coluna0) or all(coluna1) or all(coluna2) or all(coluna3) or all(coluna4) or all(coluna5):
            return True

        diagonal0 = ''.join(self.linha0[0] + self.linha1[1] + self.linha2[2] )
        diagonal1 = ''.join(self.linha0[2] + self.linha1[1] + self.linha2[0] )

        if diagonal0 == "XXX" or "OOO" or diagonal1 == "XXX" or "OOO":
            return True
"""






