"""Component 2, Ask for their age
Ask for their age, check it with an integer checker, then check it's 
in the range of 5-11
By Daniel C
"""

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
main_age = ask_age()
print(main_age)
