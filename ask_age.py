"""Component 2, Ask for their age.

Ask for their age, check it with an integer checker, then check it's

in the range of 5-11

By Daniel C
"""


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


# Main Routine
main_age = ask_age()
print(main_age)
