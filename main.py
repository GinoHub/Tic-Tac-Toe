import board
import os

def user_size_input():
    user_input = input("Board Size:\n -> ")
    return int(user_input)

def run():
    game_board = board.Board(user_size_input())
    turn = 0

    def display_board():
        os.system('cls' if os.name == 'nt' else 'clear')
        print(game_board)

    while(not game_board.check_win()):
        display_board()
        turn += 1
        game_board.make_move(turn % 2, int(input(f"where do you want to play Player {(turn % 2)}?\n -> ")))
    display_board()
    print(f"Game over! Player {((turn + 1) % 2) + 1} won in {turn} turns!")



if __name__ == "__main__":
    while True:
        run()
        if (input("Quit (Y/N)?\n -> ").lower() in ["y", "yes"]):
            break
    print("\nThanks for playing!")
