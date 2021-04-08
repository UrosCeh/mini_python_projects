def enter_a_term():
    guessing_term = input("Enter a term: ")
    sentence = guessing_term.split(" ")
    is_correct = True
    for wd in sentence:
        if not wd.isalpha():
            is_correct = False
            break
    if not is_correct:
        print("Term you enter can contain only words and spaces")
        enter_a_term()
    else:
        return guessing_term


def get_letters_from_the_term(guessing_term):
    return_letters = [ltr for ltr in guessing_term if ltr.isalpha()]
    print(set(return_letters))
    return set(return_letters)


def convert_a_term(hidden_term, exceptions):
    return_string = ""
    for char in hidden_term:
        if char in exceptions:
            return_string += char
        elif char.isalpha():
            return_string += '_'
        else:
            return_string += ' '
    return return_string


def guess_a_letter():
    ltr = input("Enter a letter: ")
    if not ltr.isalpha() or len(ltr) > 1:
        print("You can enter only one letter!")
        guess_a_letter()
    else:
        return ltr


def number_of_allowed_mistakes():
    inp = input("Enter number of allowed mistakes: ")
    try:
        i = int(inp)
    except:
        print("Enter a positive, integer number")
        number_of_allowed_mistakes()
    if i <= 0:
        print("Enter a positive, integer number")
        number_of_allowed_mistakes()
    else:
        return i


if __name__ == '__main__':
    term = enter_a_term()
    term_letters = get_letters_from_the_term(term)
    guessed_term = ""
    guessed_letters = []
    mistakes = 0
    allowed_mistakes = number_of_allowed_mistakes()

    # print("\tGuess:")
    # while not sorted(guessed_letters) == sorted(term_letters):
    while not all(ltr in guessed_letters for ltr in term_letters):
        if mistakes == allowed_mistakes:
            print("You lost!")
            break
        print("\t" + convert_a_term(term, guessed_letters))
        print("\tGuessed letters: " + ','.join(guessed_letters))
        print(f"\tNumber of mistakes left: {mistakes}")
        letter = guess_a_letter()
        guessed_letters.append(letter)
        if not letter in term_letters:
            mistakes += 1
    else:
        print("You won!")
