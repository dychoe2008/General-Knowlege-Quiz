"""Component 1, the weclome screen
Make a welcome screen, make a string checker, ask for their name
By Daniel C
"""
# pylint: disable = c0103
def str_checker(string, question_01):
    """Checks if the everything in the input is in the alpahbet"""
    invaild_str = "\n Sorry, you must enter a vaild name\n"
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
    set_name = str_checker(name, "What is your name?: ")
    return set_name

total_score = 0

#Main Routine
welcome_screen()
main_set_name = ask_name()
print(main_set_name)
