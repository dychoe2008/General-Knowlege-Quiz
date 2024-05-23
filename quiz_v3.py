"""Program for a general knowledge quiz about NZ V3
This version will include component 1, 2, 3
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
    name = input("What is your name?: ")
    set_name = str_checker(name, "What is your name?: ")
    while len(set_name) < 3:
        print(invalid_length)
        name = input("What is your name?: ")
        set_name = str_checker(name, "What is your name?: ")
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


AGE_MINIMUM = 5
AGE_MAXIMUM = 11
YES_NO = ["Yes", "Y", "No", "N"]
YES = ["Yes", "Y"]
NO = ["No", "N"]

main_total_score = 0


#Main Routine
welcome_screen()
name_set = ask_name()
main_age = ask_age()
instructions()
