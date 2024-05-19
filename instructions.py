"""Component 3, Instructions
Greet them with their name, print the instructions, 
By Daniel C
"""
def str_checker(string, question_01):
    """Checks if the everything in the input is in the alpahbet"""
    invaild = "\n Sorry, you must enter a vaild input\n"
    while string.isalpha() is False:
        print(invaild)
        string = str(input(question_01))
    return string


def instructions():
    """Print a list of instructions"""
    invaild_answer = "\n Sorry, you must enter a vaild option\n"
    list_rules = input("(***Highly Recommended***) "
                       "\n\tWould you like a list of the Rules?" 
                       "'Y' or 'N': ").title()
    final_list_rules = str_checker(list_rules, "(***Highly Recommended***) "
                                   "\n\tWould you like a list of the Rules?" 
                                   "'Y' or 'N': ").title()
    if final_list_rules in YES:
        print("\nThe Rules of this game are as follows:")
        print("\tYou will type in the answer from a multi-choice list that "
              "ranges from A to D for all questions.\n\tThere are 2 quizzes.")
        print("\tEach quiz contains 5 questions.\n\t"
              "Quiz A will be for 7 and under, "
              "whereas Quiz B will be for older than 7\n")
        print("\t\t***Of course NO CHEATING in any way!***")
        print("\t\t\t\tEnjoy!! •ᴗ•\n")
    elif final_list_rules in NO:
        print("\t\t\t\tEnjoy!! •ᴗ•\n")
    else:
        print(invaild_answer)
        instructions()


YES_NO = ["Yes", "Y", "No", "N"]
YES = ["Yes", "Y"]
NO = ["No", "N"]

#Main Routine
instructions()
