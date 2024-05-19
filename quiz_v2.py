"""Program for a general knowledge quiz about NZ V2
This version will include component 1, 2
By Daniel C
"""
def str_checker(string, question_01):
    """Checks if the everything in the input is in the alpahbet"""
    invaild = "\n Sorry, you must enter a vaild input\n"
    while string.isalpha() is False:
        print(invaild)
        string = str(input(question_01))
    return string

def int_checker(question_02):
    """Checks the input was a null or string repeats until receives a int."""
    invaild = "\n You must enter an integer that's 15-18\n"
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


AGE_MINIMUM = 5
AGE_MAXIMUM = 11


#Main Routine
welcome_screen()
name_set = ask_name()
main_age = ask_age()
