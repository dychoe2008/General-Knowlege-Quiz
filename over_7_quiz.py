"""Component 4 part 2, Quiz B.

Make Quiz b

By Daniel C
"""


def str_checker(string, question_01):
    """Check if the everything in the input is in the alpahbet."""
    invalid_str = "\n Sorry, you must enter a vaild input\n"
    while string.isalpha() is False:
        print(invalid_str)
        string = str(input(question_01))
    return string


def quiz_b():
    """Questions for quiz B."""
    total_score = 0
    print("\nWelcome to Quiz B!\n")
    print(">>First Question<<")
    print("What is the name of the stretch of water that separates"
          " the North and South Islands?:")
    print("\tA = Wellington Strait\n\tB = Tasman Channel\n\tC = Cook Strait"
          "\n\tD = Kaikoura Strait")
    guess_for_question_1 = input_for_quiz()
    if guess_for_question_1 == RANGE_OF_ANSWERS[2]:
        print("Correct!\n")
        total_score += 1
    else:
        print(f"That was Incorrect! The Answer was {RANGE_OF_ANSWERS[2]}\n")
    print(">>Second Question<<")
    print("Which New Zealand city houses the Beehive?:")
    print("\tA = Wellington\n\tB = Christchurch\n\tC = Paeroa\n\tD = Auckland")
    guess_for_question_2 = input_for_quiz()
    if guess_for_question_2 == RANGE_OF_ANSWERS[0]:
        print("Correct!\n")
        total_score += 1
    else:
        print(f"That was Incorrect! The Answer was {RANGE_OF_ANSWERS[0]}\n")
    print(">>Third Question<<")
    print("Which town has a giant carrot as a landmark?:")
    print("\tA = Taihape\n\tB = Waihi\n\tC = Paeroa\n\tD = Ohakune")
    guess_for_question_3 = input_for_quiz()
    if guess_for_question_3 == RANGE_OF_ANSWERS[3]:
        print("Correct!\n")
        total_score += 1
    else:
        print(f"That was Incorrect! The Answer was {RANGE_OF_ANSWERS[3]}\n")
    print(">>Foruth Question<<")
    print("Where is 90 mile beach?:")
    print("\tA = Top of the North Island\n\tB = Bottom of the South Island"
          "\n\tC = Bottom of the North Island\n\tD = Top of the South Island")
    guess_for_question_4 = input_for_quiz()
    if guess_for_question_4 == RANGE_OF_ANSWERS[0]:
        print("Correct!\n")
        total_score += 1
    else:
        print(f"That was Incorrect! The Answer was {RANGE_OF_ANSWERS[0]}\n")
    print(">>Fifth Question<<")
    print("When was the Treaty of Waitangi signed?:")
    print("\tA = 1815\n\tB = 1840\n\tC = 1855\n\tD = 1875")
    guess_for_question_5 = input_for_quiz()
    if guess_for_question_5 == RANGE_OF_ANSWERS[1]:
        print("Correct!\n")
        total_score += 1
    else:
        print(f"That was Incorrect! The Answer was {RANGE_OF_ANSWERS[1]}\n")
    return total_score
    # Return your score for Quiz B


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
main_total_score = quiz_b()
print(main_total_score)
# Make sure to add text to this print statement not just the number
