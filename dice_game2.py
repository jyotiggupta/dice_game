import random

''' SOME UNICODE CHARACTERS
print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
          ●      ┌      ─       ┐      │     └       ┘
'''

# dictionary = {key: value}
dice_fig = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),

    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),

    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),

    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),

    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),

    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

# Random numbers
dice = []
total = 0
num_of_dice = int(input("Enter number of dice : "))
for die in range(num_of_dice):
    dice.append(random.randint(1, 6))

# print dice vertically
for die in range(num_of_dice):
    for line in dice_fig.get(dice[die]):
        print(line)

# print dice horizontally
for line in range(5):
    for die in dice:
        print(dice_fig.get(die)[line], end="")
    print()

# calculate total
for die in dice:
    total += die
print(f"Total is : {total}")
