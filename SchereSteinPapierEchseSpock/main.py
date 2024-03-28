import sys

import Game

if __name__ == "__main__":

    game = Game.Game()

    print("imput your name")
    user_name = input()
    while True:

        print("what do u wana do?")
        print("1. play game")
        print("2. show statistics")
        print("3. exit")
        user_choice = input()
        if user_choice == "1":
            game.play_game(user_name)
        elif user_choice == "2":
            print("show statistics")
            game.show_statistics(user_name)
        elif user_choice == "3":
            print("exit")
            sys.exit()

        print(game.counts_symboles)
        print(game.counts_results)
