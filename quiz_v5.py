"""Program for a general knowledge quiz about NZ V5
This version will include component 1, 2, 3, 4 part 1 and part 2, 5
By Daniel C
"""
# pylint: disable = c0103
def str_checker(string, question_01):
    """Checks if the everything in the input is in the alpahbet"""
    invalid_str = "\n Sorry, you must enter a vaild input\n"
    while string.isalpha() is False:
        print(invalid_str)
        string = str(input(question_01))
    return string
def int_checker(question_02):
    """Checks the input was a null or string repeats until receives a int."""
    invalid = "\n You must enter an integer that's from 5 to 11\n"
    num = ""
    while not num:
        try:
            num = int(input(question_02))
            return num
        except ValueError:
            print(invalid)
def welcome_screen():
    """Prints a welcome statement"""
    print()
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("Welcome to the 'General Knowledge Quiz about NZ!'")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print()
def ask_name():
    """Asks what their name is"""
    invalid_length = "\nSorry please enter a valid name length\n"
    name = input("What is your name?: ").title()
    set_name = str_checker(name, "What is your name?: ").title()
    while len(set_name) < 3:
        print(invalid_length)
        name = input("What is your name?: ").title()
        set_name = str_checker(name, "What is your name?: ").title()
    return set_name
def ask_age():
    """Asks for their age"""
    invalid_age = "\n You must enter an whole number that's from 5 to 11\n"
    age = int_checker("What is your age?\n"
                      "(This will pick which Quiz you will be trying): ")
    while age > AGE_MAXIMUM or age < AGE_MINIMUM:
        print(invalid_age)
        age = int_checker("What is your age?\n"
                          "(This will pick which Quiz you will be trying): ")
    return age
def instructions():
    """Print a list of instructions"""
    invalid_answer = "\n Sorry, you must enter a vaild option\n"
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
        print("\t\t\t\tEnjoy!! •ᴗ•")
    elif final_list_rules in NO:
        print("\t\t\t\tEnjoy!! •ᴗ•")
    else:
        print(invalid_answer)
        instructions()
def quiz_a():
    """questions for quiz A"""
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
def quiz_b():
    """questions for quiz B"""
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
    print("Whrn was the Treaty of Waitangi signted?:")
    print("\tA = 1815\n\tB = 1840\n\tC = 1855\n\tD = 1875")
    guess_for_question_5 = input_for_quiz()
    if guess_for_question_5 == RANGE_OF_ANSWERS[1]:
        print("Correct!\n")
        total_score += 1
    else:
        print(f"That was Incorrect! The Answer was {RANGE_OF_ANSWERS[1]}\n")
    return total_score
def input_for_quiz():
    """funtion to ask which option they want to choose"""
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
def play_again():
    """funtion to play the quiz again"""
    invalid = "\n Sorry, you must enter a valid option\n"
    ask_play = input("Would you like to play again?: ").title()
    play_again_confirmed = str_checker(ask_play, "Would you like to"
                                       " play again?: ").title()
    while play_again_confirmed not in YES_NO:
        print(invalid)
        ask_play = input("Would you like to play again?: ").title()
        play_again_confirmed = str_checker(ask_play, "Would you like to"
                                           " play again?: ").title()
    if play_again_confirmed in YES:
        play_again_confirmed = True
        return play_again_confirmed
    else:
        play_again_confirmed = False
        return play_again_confirmed
AGE_MINIMUM = 5
AGE_MAXIMUM = 11
YES_NO = ["Yes", "Y", "No", "N"]
YES = ["Yes", "Y"]
NO = ["No", "N"]
RANGE_OF_ANSWERS = ["A", "B", "C", "D"]
main_total_score = 0
#Main Routine
play = True
while play:
    welcome_screen()
    main_set_name = ask_name()
    main_age = ask_age()
    print(f"\t\tHello {main_set_name}!!!")
    instructions()
    if main_age <= 7:
        main_total_score = quiz_a()
    else:
        main_total_score = quiz_b()
    print(f"\tYour score was {main_total_score} out of 5!!!\n")
    play = play_again()
print("Thanks for playing!!!")
