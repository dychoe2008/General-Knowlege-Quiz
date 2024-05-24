"""Component 4 part 1, Quiz A.

Make Quiz a

By Daniel C
"""


def str_checker(string, question_01):
    """Check if the everything in the input is in the alpahbet."""
    invalid_str = "\n Sorry, you must enter a vaild input\n"
    while string.isalpha() is False:
        print(invalid_str)
        string = str(input(question_01))
    return string


def quiz_a():
    """Questions for quiz A."""
    total_score = 0
    print("\nWelcome to Quiz A!\n")
    print(">>First Question<<")
    print("What is the capital of New Zealand?:")
    print("\tA = Auckland\n\tB = Wellington\n\tC = Christchurch"
          "\n\tD = Hamilton")
    guess_for_question_1 = input_for_quiz()
    if guess_for_question_1 == RANGE_OF_ANSWERS[1]:
        print("Correct!\n")
        total_score += 1
    else:
        print(f"That was Incorrect! The Answer was {RANGE_OF_ANSWERS[1]}\n")
    print(">>Second Question<<")
    print("Which city is known as 'The Garden City?':")
    print("\tA = Wellington\n\tB = Christchurch\n\tC = Paeroa\n\tD = Auckland")
    guess_for_question_2 = input_for_quiz()
    if guess_for_question_2 == RANGE_OF_ANSWERS[1]:
        print("Correct!\n")
        total_score += 1
    else:
        print(f"That was Incorrect! The Answer was {RANGE_OF_ANSWERS[1]}\n")
    print(">>Third Question<<")
    print("Where did L&P soda originally come from?:")
    print("\tA = Putaruru\n\tB = Waihi\n\tC = Paeroa\n\tD = Auckland")
    guess_for_question_3 = input_for_quiz()
    if guess_for_question_3 == RANGE_OF_ANSWERS[2]:
        print("Correct!\n")
        total_score += 1
    else:
        print(f"That was Incorrect! The Answer was {RANGE_OF_ANSWERS[2]}\n")
    print(">>Foruth Question<<")
    print("In what month is Matariki celebrated?:")
    print("\tA = April\n\tB = May\n\tC = May, June, or July\n\tD = July")
    guess_for_question_4 = input_for_quiz()
    if guess_for_question_4 == RANGE_OF_ANSWERS[2]:
        print("Correct!\n")
        total_score += 1
    else:
        print(f"That was Incorrect! The Answer was {RANGE_OF_ANSWERS[2]}\n")
    print(">>Fifth Question<<")
    print("What colour is Kakariki?:")
    print("\tA = Green\n\tB = Blue\n\tC = Black\n\tD = Grey")
    guess_for_question_5 = input_for_quiz()
    if guess_for_question_5 == RANGE_OF_ANSWERS[0]:
        print("Correct!\n")
        total_score += 1
    else:
        print(f"That was Incorrect! The Answer was {RANGE_OF_ANSWERS[0]}\n")
    return total_score
    # Return your score from Quiz A


def input_for_quiz():
    """Funtion to ask which option they want to choose."""
    invalid_guess = "\n Sorry, you must enter a vaild guess\n"
    guess = input("Which of these options will you choose?: ").title()
    guess_confirmed = str_checker(guess, "Which of these options"
                                  " will you choose?: ").title()
    while guess_confirmed not in RANGE_OF_ANSWERS:
        print(invalid_guess)
        guess = input("Which of these options will you choose?: ").title()
        guess_confirmed = str_checker(guess, "Which of these options"
                                      " will you choose?: ").title()
    return guess_confirmed
    # Return your guess from the options A,B,C,D


RANGE_OF_ANSWERS = ["A", "B", "C", "D"]

# Main Routine
main_total_score = quiz_a()
print(main_total_score)
# Make sure to add text to this print statement not just the number
