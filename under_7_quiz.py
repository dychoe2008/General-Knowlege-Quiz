"""Component 3, Instructions
Make Quiz a
By Daniel C
"""
def str_checker(string, question_01):
    """Checks if the everything in the input is in the alpahbet"""
    invaild = "\n Sorry, you must enter a vaild input\n"
    while string.isalpha() is False:
        print(invaild)
        string = str(input(question_01))
    return string

def quiz_a():
    """questions for quiz A"""
    total_score_quiz_a = 0
    print("\nWelcome to Quiz A!\n")
    print(">>First Question<<")
    print("\nWhat is the capital of New Zealand?:")
    print("\tA = Auckland\n\tB = Wellington\n\tC = Christchurch"
          "\n\tD = Hamilton")
    guess_for_question_1 = input_for_quiz_a()
    print(guess_for_question_1)
    if guess_for_question_1 == RANGE_OF_ANSWERS[1]:
        print("Correct!")
        total_score_quiz_a += 1
    else:
        print(f"That was Incorrect! The Answer was {RANGE_OF_ANSWERS[1]}")
    print(">>Second Question<<")
    print("\nWhich city is known as 'The Garden City?':")
    print("\tA = Wellington\n\tB = Christchurch\n\tC = Paeroa"
          "\n\tD = Auckland")
    guess_for_question_2 = input_for_quiz_a()
    print(guess_for_question_2)
    if guess_for_question_2 == RANGE_OF_ANSWERS[1]:
        print("Correct!")
        total_score_quiz_a += 1
    else:
        print(f"That was Incorrect! The Answer was {RANGE_OF_ANSWERS[1]}")
    print(">>Third Question<<")
    print("\nWhere did L&P soda originally come from?:")
    print("\tA = Putaruru\n\tB = Waihi\n\tC = Paeroa"
          "\n\tD = Auckland")
    guess_for_question_3 = input_for_quiz_a()
    print(guess_for_question_3)
    if guess_for_question_3 == RANGE_OF_ANSWERS[2]:
        print("Correct!")
        total_score_quiz_a += 1
    else:
        print(f"That was Incorrect! The Answer was {RANGE_OF_ANSWERS[2]}")
    print(">>Foruth Question<<")
    print("\nIn what month is Matariki celebrated?:")
    print("\tA = April\n\tB = May\n\tC = May, June, or July"
          "\n\tD = July")
    guess_for_question_4 = input_for_quiz_a()
    print(guess_for_question_4)
    if guess_for_question_4 == RANGE_OF_ANSWERS[2]:
        print("Correct!")
        total_score_quiz_a += 1
    else:
        print(f"That was Incorrect! The Answer was {RANGE_OF_ANSWERS[2]}")
    print(">>Fifth Question<<")
    print("\nWhat colour is Kakariki?:")
    print("\tA = Green\n\tB = Blue\n\tC = Black"
          "\n\tD = Grey")
    guess_for_question_5 = input_for_quiz_a()
    print(guess_for_question_5)
    if guess_for_question_5 == RANGE_OF_ANSWERS[0]:
        print("Correct!")
        total_score_quiz_a += 1
    else:
        print(f"That was Incorrect! The Answer was {RANGE_OF_ANSWERS[0]}")
    return total_score_quiz_a

def input_for_quiz_a():
    """funtion to ask which option they want to choose"""
    invaild_guess = "\n Sorry, you must enter a vaild guess\n"
    guess = input("Which of these options will you choose?: ").title()
    guess_confirmed = str_checker(guess, "Which of these options"
                                  " will you choose?: ").title()
    while guess_confirmed not in RANGE_OF_ANSWERS:
        print(invaild_guess)
        guess = input("Which of these options will you choose?: ").title()
        guess_confirmed = str_checker(guess, "Which of these options"
                                      " will you choose?: ").title()
    return guess_confirmed


RANGE_OF_ANSWERS = ["A", "B", "C", "D"]

#Main Routine
total_score = quiz_a()
print(total_score)
