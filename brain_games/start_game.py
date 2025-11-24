import argparse

from brain_games.user_interactive import welcome_user
from brain_games.games.even import start_even_game
from brain_games.games.calc import start_calc_game
from brain_games.games.nod import start_nod_game
from brain_games.games.progression import start_progression_game

def main():
    parser = create_parser()
    args_namespace = parser.parse_args() 
    user_name = welcome_user()
    match args_namespace.game_type:
        case "even":
            start_even_game(user_name, args_namespace.game_length)
        case "calc":
            start_calc_game(user_name, args_namespace.game_length)
        case "nod":
            start_nod_game(user_name, args_namespace.game_length)
        case "progression":
            start_progression_game(user_name, args_namespace.game_length)
        case _: 
            print(f'Sorry {user_name}. Unknown game')

if __name__ == "__main__":
    main()

def create_parser():
    parser = argparse.ArgumentParser(description="Start brain game.") 
    parser.add_argument('-t', '--game_type', type=str, help='Type of mind games.')
    parser.add_argument('-l', '--game_length', type=int, default=3, help='Count of rounds to win. Dedault value is 3.')
    return parser