import board_class as Board

print('Zacznijmy grę! :)')

def get_player_choice():
    player_choice = input('Wybierz drużynę, wpisz 1 jeżeli chcesz być "X", wpisz 2 jeżeli chcesz być "O": ')
    if player_choice == '1':
        return "X"
    if player_choice =='2':
        return "O"
    else:
        print('Zła liczba, wpisz odpowiednią liczbę :)')
 
player_choice = get_player_choice()

board = Board.Board(player_choice)

while (not board.check_if_win()) and (not board.check_if_draw()) :
    board.show_board()
    player_x_choice = int(input("Któro pole wybierasz, wpisz wartość pól poziomych (X): "))
    player_y_choice = int(input("Któro pole wybierasz, wpisz wartość pól pionowych (Y): "))
    board.put_to_board(player_x_choice,player_y_choice)


if board.check_if_win():
    board.show_board()
    winner = ''
    if board.player == 'X':
        winner = 'O'
    elif board.player == 'O':
        winner= 'X'
    print('-------')
    print(f'Gratulacje, gracz {winner} wygrał grę!')

if board.check_if_draw():
    board.show_board()
    print('-------')
    print('Remis!')