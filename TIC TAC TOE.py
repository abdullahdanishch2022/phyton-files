import random
from colorama import fore, init, Style
init(autoreset=True)

def display_board(board):
    print()
    def colored(cell):
        if cell == 'x':
            return fore.RED +cell + Style.RESET_ALL
        elif cell =='o':
            return fore.BLUE + cell + Style.RESET_ALL
        else:
            return fore.YELLOW +cell + Style.RESET_ALL
    print('' + colored(board[0]) + '_' + colored(board[1])+  '_' + colored(board))
    print(fore.CYAN + ---+---+--- + Style.RESET_ALL)
    print('' + colored(board[3]) + '_' + colored(board[4]) + '_'+ colored(board[5]))
        