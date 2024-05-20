"""Program for a general knowledge quiz about NZ V1
This version will include component 1
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

total_score = 0

#Main Routine
welcome_screen()
name_set = ask_name()
