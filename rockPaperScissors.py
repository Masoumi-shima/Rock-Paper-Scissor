from operator import truediv
import random


def play():
    user = input("'r' for Rock, 'p' for Paper and 's' for Scissors:")
    computer = random.choice(["r", "s", "p"])
    if user == computer:
        return "It's a tie!"

    if is_win(user, computer):
        return "You won!"

    return "You lost!"


def is_win(player, opponent):
    # return true if the player wins
    # r > s, s > p, p > r
    if (
        (player == "r" and opponent == "s")
        or (player == "s" and opponent == "p")
        or (play == "p" and opponent == "r")
    ):
        return True


print(play())
