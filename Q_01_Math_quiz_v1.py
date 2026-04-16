# function go here
import random


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
at the end if you want you can see your
quiz history. 
    """)



# Checks users enter an int / float that is
# more than a minimum (default minimum is zero)
# Allows an 'exir' code
def num_check(question, num_type=int, low=1, high= 100, exit_code = "xxx"):

    error = f"Please enter an integer between {low} and {high}."

    while True:
        # Ask user question and return response if
        # exit code is entered
        response = input(question)
        if response == exit_code:
            return response
        # check response is more than minimum
        try:
            response = num_type(response)

            if response < low:
                print(f"Too low {error}")
            elif response > high:
                print(f"Too high{error}")
            else:
                return response

        # Show error if response is invalid
        except ValueError:
            print(error)


def not_blank(question):
    """ Make sure that the input is not empty """
    while True:
        # ask user the question
        response = input(question)

        # return their response if it is not blank
        if response != "":
            return response
        elif response:
            print("Please enter only letters")
        else:
            print("sorry - your response can't be blank")



# Main routine starts here

# Get the username and welcome them
your_name = not_blank("What is your name? ")
print(f"Welcome to Math quiz {your_name}")

# ask the user if they want instructions(yes/ no)
want_instructions = yes_no("Do you want to see the instructions? ")

# Display the instructions if the user wants to see them...
if want_instructions == "yes":
    instructions()
# Ask for the number of questions
print()
question_numbers= num_check("How many questions do you want? ")
if question_numbers == "xxx":
    print("Have a good day")
else:
    print(f"You chose {question_numbers} questions")





    # Initialize game variables
    score= 0
    history = []
    user_answer =  ""

    # Looping starts here
    for item in range (int(question_numbers)):
        num_one = random.randint(1, 100)
        num_two = random.randint(1, 100)
        operations = random.choice(["+", "-", "*","/","Area","Perimeter"])

        # Calculate the user answers based in the operations
        if operations == "+":
            correct_answer = num_one + num_two
        elif operations == "-":
            correct_answer = num_one - num_two
        elif operations == "*":
            correct_answer = num_one * num_two
        elif operations == "/":
            correct_answer = num_one // num_two
        elif operations == "Area":
            correct_answer = num_one * num_two
            ask_question = f" Area of rectangle {num_one} x {num_two}  "
        else:
            correct_answer = 2 * (num_one + num_two)
            ask_question = f" perimeter of rectangle {num_one} x {num_two}  "


    # Get Valid answer from the user

        while True:
            try:
                if operations == "Area":
                    user_answer=int(input(f"{item+1}: Area of rectangle (height = {num_one} , width= {num_two}) " ))
                elif operations == "Perimeter":
                    user_answer= int(input(f"{item+1}: Perimeter of rectangle (height ={num_one} and width= {num_two}) " ))
                else:
                    user_answer = int(input(f"{item+1}: {num_one}  {operations} {num_two} "))
                break
            except ValueError:
                print("Please enter a number! ")


        # Check the answer of the user
        if user_answer == correct_answer:
            print("Correct!")
            score +=1

        else:
            print (f"Incorrect! The answer was {correct_answer}.")

        # Add results to game history
        if operations== "Area":
            quiz_history = f"{item+1}: Area of rectangle (height = {num_one} , width= {num_two}) = {user_answer} "
        elif operations== "Perimeter":
            quiz_history = f"{item+1}: Perimeter of rectangle (height ={num_one} and width= {num_two}) =  {user_answer} "
        else:
            quiz_history = f"{item+1}: {num_one}  {operations} {num_two}  = {user_answer}"
        history.append(quiz_history)

# Loop ends here
    if question_numbers > 0:
        percentage = (score / question_numbers) * 100
        print(f"percentage: {percentage:.1f}%")
    else:
        print("You have to enter numbers!")




# Display the game history on request
    see_history = yes_no("\nDo you want to see your game history? ")
    if see_history == "yes":
        for item in history:
                print(item)







