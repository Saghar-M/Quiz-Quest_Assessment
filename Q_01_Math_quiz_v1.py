# function go here
import random
from unittest import result


def yes_no(question):
    """checks user response to a question is yes / no (y/n), returns 'yes' or 'no' """

    while True:
        response = input(question).lower()

        # check the user says yes / no / y/ n
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes / no")


def instructions():
    """Prints instructions"""

    print("""
### Instructions ###
You will be asked simple math questions, 
you will get feedback after each question. 
please try to enter only numbers, and 
at the emd if you want you can see your
quiz history. 
    """)



def int_check(question):
    """cheks users enter an integer more than /equal to 1 """
    error =  "Please enter an integer more than/equal to 1."

    while True:
        try:
            response = int(input(question))

            if response <1:
                print(error)
            else:
                return response


        except ValueError:
            print(error)


# Main routine starts here

# ask the user if they want instructions(yes/ no)
want_instructions = yes_no("Do you want to see the instructions? ")

# Display the instructions if the user wants to see them...
if want_instructions == "yes":
    instructions()

print()
question_numbers= int_check("How many questions do you want? ")
print(question_numbers)


# Initialise game variables
score= 0


# Looping starts here
for item in range ( question_numbers):
    num_one = random.randint(1, 100)
    num_two = random.randint(1, 100)
    operations = random.choice(["+", "-", "*"])

    # Calculate the answers in here
    if operations == "+":
        correct_answer = num_one + num_two
    elif operations == "-":
        correct_answer = num_one - num_two
    else:
        correct_answer = num_one * num_two



# Get Valid answer from the user

    while True:
        try:
            user_answer = int(input(f"Question{item+1}: {num_one}  {operations} {num_two} "))
            break
        except ValueError:
            print("Please enter a number! ")

    # Check the answer of the user
    if user_answer == correct_answer:
        print("Correct!")
        score +=1

    else:
        print (f"Incorrect! The answer was {correct_answer}.")






