"""Program for a general knowledge quiz about NZ V4
This version will include component 1, 2, 3, 4
By Daniel C
"""
# pylint: disable = c0103
def str_checker(string, question_01):
    """Checks if the everything in the input is in the alpahbet"""
    invaild_str = "\n Sorry, you must enter a vaild input\n"
    while string.isalpha() is False:
        print(invaild_str)
        string = str(input(question_01))
    return string

def int_checker(question_02):
    """Checks the input was a null or string repeats until receives a int."""
    invaild = "\n You must enter an integer that's from 5 to 11\n"
    num = ""
    while not num:
        try:
            num = int(input(question_02))
            return num
        except ValueError:
            print(invaild)

def welcome_screen():
    """Prints a welcome statement"""
    print()
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("Welcome to the 'General Knowledge Quiz about NZ!'")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print()

def ask_name():
    """Asks what their name is"""
    name = input("What is your name?: ")
    name_set_ = str_checker(name, "What is your name?: ")
    return name_set_

def ask_age():
    """Asks for their age"""
    invaild_age = "\n You must enter an whole number that's from 5 to 11\n"
    age = int_checker("What is your age?\n"
                      "(This will pick which Quiz you will be trying): ")
    while age > AGE_MAXIMUM or age < AGE_MINIMUM:
        print(invaild_age)
        age = int_checker("What is your age?\n"
                          "(This will pick which Quiz you will be trying): ")
    return age

def instructions():
    """Print a list of instructions"""
    invaild_answer = "\n Sorry, you must enter a vaild option\n"
    list_rules = input("(***Highly Recommended***) "
                       "\n\tWould you like a list of the Rules? " 
                       "'Y' or 'N': ").title()
    final_list_rules = str_checker(list_rules, "(***Highly Recommended***) "
                                   "\n\tWould you like a list of the Rules? " 
                                   "'Y' or 'N': ").title()
    if final_list_rules in YES:
        print("\nThe Rules of this game are as follows:")
        print("\tYou will type in the answer from a multi-choice list that "
              "ranges from A to D for all questions. There are 2 quizzes.")
        print("\tEach quiz contains 5 questions. "
              "Quiz A will be for 7 and under, "
              "whereas Quiz B will be for older than 7\n")
        print("\t\t***Of course NO CHEATING in any way!***")
        print("\t\t\t\tEnjoy!! •ᴗ•\n")
    elif final_list_rules in NO:
        print("\t\t\t\tEnjoy!! •ᴗ•\n")
    else:
        print(invaild_answer)
        instructions()

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


AGE_MINIMUM = 5
AGE_MAXIMUM = 11
YES_NO = ["Yes", "Y", "No", "N"]
YES = ["Yes", "Y"]
NO = ["No", "N"]
RANGE_OF_ANSWERS = ["A", "B", "C", "D"]

total_score = 0


#Main Routine
welcome_screen()
name_set = ask_name()
main_age = ask_age()
instructions()
total_score = quiz_a()
print(total_score)
