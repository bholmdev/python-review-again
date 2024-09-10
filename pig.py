import random

def play_game():

    def start():
        while True:
            num_players = input("Enter the number of players (2 - 4):  ")

            if num_players.isdigit():
                num_players = int(num_players)
                if 2 <= num_players <= 4:
                    return num_players
                else:
                    print("Must be betweeen 2 - 4 players.")
            else:
                print("Invalid, try again.")

    num_players = start()
    max_score = 10
    player_scores = [0 for _ in range(num_players)]

    def roll():
        min_value = 1
        max_value = 6
        roll = random.randint(min_value, max_value)

        return roll
    
    def play_again():
        ask = input("Would you like to play again?  ")

        if ask.lower() != "y" and ask.lower() != "yes":
            return
        else:
            play_game()
        
    def game():
        while max(player_scores) < max_score:
            for player in range(num_players):
                print(f"\nPlayer {player + 1}'s turn!\n")
                current_score = 0

                while True:
                    should_roll = input("Would you like to roll?  (y/n)  ")

                    if should_roll.lower() != "y" and should_roll.lower() != "yes":
                        break
                    
                    value = roll()

                    if value == 1:
                        print("You rolled a 1! Next player start")
                        current_score = 0
                        break
                    else:
                        current_score += value
                        print("You rolled a:", value)
                    
                    print("Your score is:", current_score)

                player_scores[player] += current_score
                print("Your total score is:", player_scores[player])
        play_again()
        
    game()

play_game()