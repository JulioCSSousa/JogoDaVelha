#regras do jogo da velha

# 1 - jogador 1 = bolinha e o jogador 2 = x
# 2 - cada jogador pode jogar uma vez por turno
# 3 - São 9 espaços no tabuleiro e não pode jogar em um espaço ja utilizado
# 4 - Ganha quem quem prencher 3 espaços consecutivos com bolinha ou x na horizontal, vertical ou diagonal

class JogoDaVelha:
    ox = ['O', 'X']
    pontos_jogador1 = 0
    pontos_jogador2 = 0
    ganhou = False

    def __init__(self):
        self.linha0 = ['*', '*', '*']
        self.linha1 = ['*', '*', '*']
        self.linha2 = ['*', '*', '*']

        self.matriz = [self.linha0, self.linha1, self.linha2]

        print(f' 0 {self.linha0}\n 1 {self.linha1}\n 2 {self.linha2}')
        print('=' * 50)

    def jogador1(self, escolha_x_o):
        self.escolha_x_o = escolha_x_o
        if self.escolha_x_o == 0:
            self.escolha1 = '0'

        elif self.escolha_x_o == 1:
            self.bolinha_ou_x_escolha = 'X'
        else:
            print('Escolha entre 0 ou 1')

    def jogador2(self):
        if self.escolha_x_o == 0:
            self.escolha2 = 'X'
        elif self.escolha1 == 1:
            self.escolha2 = 'O'

    def atualiza_tabuleiro(self):
        print(self.atualizar)


    def jogadaO(self, linha, coluna):
        self.linha = linha
        self.coluna = coluna
        start = True
        while start:
            if linha == 0:
                self.linha0[coluna] = self.ox[0]
                start = False
            elif linha == 1:
                self.linha1[coluna] = self.ox[0]
                start = False
            elif linha == 2:
                self.linha2[coluna] = self.ox[0]
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



jogo = JogoDaVelha()





jogo.vitoria()







