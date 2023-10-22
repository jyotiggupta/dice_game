import random
# 1


def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

# 2


while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must enter between 2-4 players")
    else:
        print("Invalid! Try again.")

# print(players)

max_score = 50
players_score = [0 for _ in range(players)]
while max(players_score) < max_score:
    for player_idx in range(players):
        print("\nPlayer number ", player_idx + 1, " has just started!\n")
        print("Your total score is:", players_score[player_idx], "\n")
        current_score = 0
        while True:
            should_roll = input("Would you like to roll (y/n)? ")
            if should_roll.lower() != 'y':
                break

            value = roll()
            if value == 1:
                print("You rolled 1! TURN IS OVER! ")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a: ", value)

            print("Your score is:", current_score)

        players_score[player_idx] += current_score
        print("Your total score is : ", players_score[player_idx])

max_score = max(players_score)
winning_ind = players_score.index(max_score)
print("PLayer number", winning_ind + 1, "is the winner with score :", max_score)
