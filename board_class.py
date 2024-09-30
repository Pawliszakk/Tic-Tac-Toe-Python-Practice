class Board:
    def __init__(self, player):
        self.board= [['.','.','.'],['.','.','.'],['.','.','.']]
        self.player = player
        self.win = False


    def show_board(self):
        print('  1 2 3')
        number_row = 1
        for row in self.board:
            print(number_row, end =' ')
            for element in row:
                print(element, end=' ')
            print()
            number_row += 1

    def check_if_win(self):
        for x in range(0,3):
            if self.board[x][0] == self.board[x][1] and self.board[x][1] == self.board[x][2] !='.' :
                self.win = True
                return True
        for y in range(0,3):
            if self.board[0][y] == self.board[1][y] and self.board[2][y] == self.board[2][y] != '.' :
                self.win = True
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '.':
            self.win = True
            return True
        
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '.':
            self.win = True
            return True
        return False


    def check_if_draw(self):
        if not self.check_if_win():
            for row in self.board:
                for element in row:
                    if element == '.':
                        return False
            return True
        else:
            return False

    def check_if_free_to_put(self,x,y):
        return self.board[x-1][y-1] == '.'

    def change_player(self):
        if self.player =='O':
            self.player = 'X'
        elif self.player =='X':
            self.player = 'O'
    

    def put_to_board(self,x,y):
        if self.check_if_free_to_put(x,y):
            self.board[x-1][y-1] = self.player
            self.change_player()
        else:
            print('Podane pole jest zajęte przez przeciwnika, spróboj inne pole.')
    

    def get_player(self):
        return self.player


