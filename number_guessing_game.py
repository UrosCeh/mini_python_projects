import random

if __name__ == '__main__':
    num = int(input("Guess a number between 1 and 3\n:"))
    win_num = random.randint(1, 3)
    if num == win_num:
        print("You won!")
    else:
        print(f"You lost...\nThe number was {win_num}")
