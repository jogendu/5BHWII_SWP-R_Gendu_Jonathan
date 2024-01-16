import random

def read_symbol_counts_from_file():
    try:
        with open("gewinner.txt", "r") as file:
            lines = file.readlines()
            if len(lines) >= 2:
                symbol_counts_line = lines[1].strip()  # Zeile 2 enthält die Symbolzählungen
                symbol_counts = {}
                parts = symbol_counts_line.split(", ")
                for p in parts:
                    symbol, count_str = p.split(": ")
                    count = int(count_str.split()[0])
                    symbol_counts[symbol] = count
                return symbol_counts
            else:
                return {}
    except FileNotFoundError:
        return {}
def load_scores():
    try:
        with open("gewinner.txt", "r") as file:
            user_wins, computer_wins = map(int, file.readline().strip().split(":"))
            return user_wins, computer_wins
    except FileNotFoundError:
        return 0, 0


def save_scores(user_wins, computer_wins, symbol_counts):
    with open("gewinner.txt", "w") as file:
        file.write(f"{user_wins}:{computer_wins}")
        file.write("\n")
        for symbol, count in symbol_counts.items():
            file.write(f"{symbol}: {count} Mal, ")


def get_user_choice():
    print("Schere, Stein, Papier, Echse oder Spock?")
    user_choice = input("Deine Wahl: ").strip().lower()
    while user_choice not in ["schere", "stein", "papier", "echse", "spock"]:
        print("Ungültige Eingabe. Bitte erneut eingeben.")
        user_choice = input("Deine Wahl: ").strip().lower()
    return user_choice


def get_computer_choice():
    choices = ["schere", "stein", "papier", "echse", "spock"]
    return random.choice(choices)


def menu():
    print("\ng - Runde spielen\ns - SpielStatistik")
    menu_input = input("Deine Wahl:").strip().lower()
    return menu_input


def determine_winner():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    symbol_counts = read_symbol_counts_from_file()
    print(symbol_counts)
    symbol_counts[user_choice] += 1
    symbol_counts[computer_choice] += 1

    print(f"Du hast {user_choice} gewählt.")
    print(f"Der Computer hat {computer_choice} gewählt.")
    win_conditions = {
        ("schere", "papier"): "Du gewinnst",
        ("schere", "echse"): "Du gewinnst",
        ("stein", "schere"): "Du gewinnst",
        ("stein", "echse"): "Du gewinnst",
        ("papier", "stein"): "Du gewinnst",
        ("papier", "spock"): "Du gewinnst",
        ("echse", "spock"): "Du gewinnst",
        ("echse", "papier"): "Du gewinnst",
        ("spock", "schere"): "Du gewinnst",
        ("spock", "stein"): "Du gewinnst",
        ("papier", "schere"): "Computer gewinnt",
        ("echse", "stein"): "Computer gewinnt",
        ("stein", "papier"): "Computer gewinnt",
        ("spock", "papier"): "Computer gewinnt",
        ("spock", "echse"): "Computer gewinnt",
        ("schere", "stein"): "Computer gewinnt"
    }
    user_wins, computer_wins = load_scores()
    if (user_choice, computer_choice) in win_conditions:
        if win_conditions[(user_choice, computer_choice)] == "Computer gewinnt":  # Übergebe als Tupel
            computer_wins += 1
            save_scores(user_wins, computer_wins, symbol_counts)
            return win_conditions[(user_choice, computer_choice)]
        elif win_conditions[(user_choice, computer_choice)] == "Du gewinnst":
            user_wins += 1
            save_scores(user_wins, computer_wins, symbol_counts)
            return win_conditions[(user_choice, computer_choice)]

    else:
        save_scores(user_wins, computer_wins, symbol_counts)
        return "Unentschieden"


if __name__ == "__main__":
    menu_input = menu()
    match menu_input:
        case "g":
            print(determine_winner())

            menu_input = menu()
        case "s":
            player, computer = load_scores()
            print("Spieler: " + str(player) + "  Computer: " + str(computer))
            symbol_counts = read_symbol_counts_from_file()
            for symbol, count in symbol_counts.items():
                print(f"{symbol}: {count} Mal")

            menu_input = menu()

        case _:
            print("Falsche Eingabe")
            menu_input = menu()
