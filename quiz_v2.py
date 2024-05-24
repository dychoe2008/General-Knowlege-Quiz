"""Program for a general knowledge quiz about NZ V2.

This version will include component 1, 2

By Daniel C
"""
# pylint: disable = c0103


def str_checker(string, question_01):
    """Check if the everything in the input is in the alpahbet."""
    invalid_str = "\n Sorry, you must enter a vaild input\n"
    while string.isalpha() is False:
        print(invalid_str)
        string = str(input(question_01))
    return string


def int_checker(question_02):
    """Check the input was a null or string repeats until receives a int."""
    invalid = "\n You must enter an integer that's from 5 to 11\n"
    num = ""
    while not num:
        try:
            num = int(input(question_02))
            return num
        except ValueError:
            print(invalid)


def welcome_screen():
    """Print a welcome statement."""
    print()
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("Welcome to the 'General Knowledge Quiz about NZ!'")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print()


def ask_name():
    """Asks what their name is."""
    invalid_length = "\nSorry please enter a valid name length\n"
    name = input("What is your name?: ").title()
    set_name = str_checker(name, "What is your name?: ").title()
    while len(set_name) < 3:
        print(invalid_length)
        name = input("What is your name?: ").title()
        set_name = str_checker(name, "What is your name?: ").title()
    return set_name
    # Return the name and use this to greet them


def ask_age():
    """Asks for their age."""
    invalid_age = "\n You must enter an whole number that's from 5 to 11\n"
    age = int_checker("What is your age?\n"
                      "(This will pick which Quiz you will be trying): ")
    while age > AGE_MAXIMUM or age < AGE_MINIMUM:
        print(invalid_age)
        age = int_checker("What is your age?\n"
                          "(This will pick which Quiz you will be trying): ")
    return age
    # Return their age and using this pick which Quiz they will do


AGE_MINIMUM = 5
AGE_MAXIMUM = 11

main_total_score = 0
# Use this variable for the total score for the quizzes

# Main Routine
welcome_screen()
main_set_name = ask_name()
main_age = ask_age()
print(f"\t\tHello {main_set_name}!!!")
