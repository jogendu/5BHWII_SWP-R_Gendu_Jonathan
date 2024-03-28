# make method start game
import sys
import random
import csv


class Game:
    def __init__(self):
        self.rules = {"Schere": ["Papier", "Echse"],
                      "Stein": ["Schere", "Echse"],
                      "Papier": ["Stein", "Spock"],
                      "Echse": ["Papier", "Spock"],
                      "Spock": ["Stein", "Schere"]}
        self.counts_symboles = {"Schere": 0,
                                "Stein": 0,
                                "Papier": 0,
                                "Echse": 0,
                                "Spock": 0}
        self.counts_results = {"draw": 0,
                               "win": 0,
                               "lose": 0}

    def play_game(self, user_name):
        entrys = []
        written_entry = False
        # let user make a choice
        print("choose one of the following options: ")
        print("Stein, Schere, Papier, Echse, Spock")
        user_choice = input()
        # if user choice is not in the list
        if user_choice not in ["Stein", "Schere", "Papier", "Echse", "Spock"]:
            print("Invalid input")
            sys.exit()

        else:
            # add 1 to the count of the user choice
            self.counts_symboles[user_choice] += 1
            possible_choices = ["Stein", "Schere", "Papier", "Echse", "Spock"]
            computer_choice = random.choice(possible_choices)
            self.counts_symboles[computer_choice] += 1
            if user_choice == computer_choice:
                result = f"There is a draw ({computer_choice})"
                self.counts_results["draw"] += 1
            # if user choice is not equal to computer choice
            else:
                if computer_choice in self.rules[user_choice]:
                    result = f"Well done. Computer chose {computer_choice} and lost"
                    self.counts_results["win"] += 1
                    # save score to file score.csv
                    score = 100
                    with open('score.csv', newline='') as csvfile:

                        reader = csv.DictReader(csvfile)

                        for row in reader:
                            entrys.append(row)

                    with open('score.csv', 'w', newline='') as csvfile:
                        fieldnames = ['user_name', 'score']
                        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                        writer.writeheader()
                        for row in entrys:
                            if row['user_name'] == user_name:
                                score = int(row['score']) + 100
                                writer.writerow({'user_name': user_name, 'score': score})
                                written_entry = True
                            else:
                                writer.writerow({'user_name': row['user_name'], 'score': row['score']})
                        if not written_entry:
                            writer.writerow({'user_name': user_name, 'score': score})



                else:
                    result = f"Sorry, but computer chose {computer_choice} and won"
                    self.counts_results["lose"] += 1
            print(result)

    def show_statistics(self, user_name):
        with open('score.csv', newline='') as csvfile:

            reader = csv.DictReader(csvfile)

            for row in reader:
                if row['user_name'] == user_name:
                    print(row['user_name'], row['score'])
                    break
            else:
                print("no score found")
