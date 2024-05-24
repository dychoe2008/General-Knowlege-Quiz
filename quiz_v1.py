"""Program for a general knowledge quiz about NZ V1
This version will include component 1
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
        name = input("What is your name?: ")
        set_name = str_checker(name, "What is your name?: ").title()
    return set_name
main_total_score = 0

#Main Routine
welcome_screen()
main_set_name = ask_name()
print(f"\t\tHello {main_set_name}!!!")
