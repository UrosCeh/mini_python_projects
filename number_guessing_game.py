import random


def return_if_int(inputted):
    try:
        val = int(inputted)
        return val
    except ValueError:
        print("\tNumber must be integer!")
        return None


def get_int(message):
    number = None
    while not number:
        number = return_if_int(input(message))
    else:
        return number


def guess_number(minim, maxim):
    number = get_int(f"Guess a number between {minim} and {maxim}: ")
    while not minim <= number <= maxim:
        number = get_int(f"\tNumber out of bounds!\nGuess a number between {minim} and {maxim}: ")
    else:
        return number


def get_number_of_tries():
    number_of_tries = get_int("Enter number of tries: ")
    while not number_of_tries > 0:
        number_of_tries = get_int("Enter number of tries: ")
    else:
        return number_of_tries


if __name__ == '__main__':
    tries = get_number_of_tries()
    mn = get_int("Enter minimum guessing value: ")
    mx = get_int("Enter maximum guessing value: ")
    win_num = random.randint(mn, mx)
    while tries > 0:
        num = guess_number(mn, mx)
        if num == win_num:
            print("You won!")
            break
        else:
            print("\tWrong! Try again")
            tries -= 1
    else:
        print(f"You lost...\nThe number was {win_num}")
