import random


def return_if_int(inputted):
    try:
        val = int(inputted)
        return val
    except ValueError:
        print("Number must be integer!")
        return None


def get_int(message):
    number = None
    while not number:
        print(message)
        number = return_if_int(input())
    else:
        return number


def guess_number(minim, maxim):
    number = get_int(f"Guess a number between {mn} and {mx}")
    while not minim <= number <= maxim:
        number = get_int(f"Guess a number between {mn} and {mx}")
    else:
        return number


if __name__ == '__main__':
    mn = get_int("Enter minimum guessing value:")
    mx = get_int("Enter maximum guessing value:")
    num = guess_number(mn, mx)
    # print(num)
    win_num = random.randint(mn, mx)
    if num == win_num:
        print("You won!")
    else:
        print(f"You lost...\nThe number was {win_num}")
