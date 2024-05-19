"""Component 3, Instructions
Make a Quiz a
By Daniel C
"""
def str_checker(string, question_01):
    """Checks if the everything in the input is in the alpahbet"""
    invaild = "\n Sorry, you must enter a vaild input\n"
    while string.isalpha() is False:
        print(invaild)
        string = str(input(question_01))
    return string

def quiz_a():
    """questions for quiz A"""
    print("\nWelcome to Quiz A!\n")
    print(">>First Question<<")
    print("\n\tWhat is the capital of New Zealand?:")


def input_for_quiz_a():
    """"""
    guess = input("Which of these options will you choose?: ")
    guess_confirmed = str(guess, "Which of these options will you choose?: ")
    while guess_confirmed not in RANGE_OF_ANSWERS:
        input_for_quiz_a
    return input_for_quiz_a


RANGE_OF_ANSWERS = ["A", "B", "C", "D"]

#Main Routine

