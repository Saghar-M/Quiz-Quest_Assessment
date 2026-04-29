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
        response = input(question).lower()

        # check for infinite mode / exit code
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
        if response.isalpha():
            return response

        else:
            print("Sorry- Your response can't be blank or numbers")



# Main routine starts here
# Initialize game variables
mode = "regular"
score= 0
history = []
user_answer =  ""
end_game = "no"

rounds_played = 0
feedback =""

print("🔼🔼🔼 Welcome to the Math Quiz🔻🔻🔻")
print()

# Get the username and welcome them
your_name = not_blank("What is your name? ")
print(f"Welcome to Math quiz {your_name}")

# ask the user if they want instructions(yes/ no)
want_instructions = yes_no("Do you want to see the instructions? ")

# Display the instructions if the user wants to see them...
if want_instructions == "yes":
    instructions()
# Ask for the number of questions

# Ask user for number of questions / infinite mode
question_numbers = num_check("Rounds <enter for infinite:",
                       low=1, high=100, exit_code="")
# checks if the user wants to quit

if question_numbers== "":
    mode ="infinite"
    question_numbers = 10

# ask user if they want to customise the number range
default_params = yes_no("Do you want to use the default game parameters? ")
if default_params== "yes":
    low_num= 0
    high_num = 100

# allow user to choose the high / low number
else:
    low_num = num_check("Low Number? ", exit_code="xxx")
    if low_num == "xxx":
        end_game ="yes"
        exit()
    high_num = num_check("High Number? ", low=low_num+1, exit_code="xxx")
    if high_num == "xxx":
        end_game = "yes"
        exit()

# calculate the maximum number of guesses bsed on the low and high number
numbers_allowed = (low_num, high_num)

# Game loop starts here

while rounds_played < question_numbers:

    rounds_played+=1

    # Rounds headings ( based on mode)
    if question_numbers == "infinite":
        rounds_heading = f"\n 💿💿💿 Round {rounds_played} (infinite Mode) 💿💿💿 "
    else:
        rounds_heading = f"\n 💿💿💿 Round {rounds_played } of {question_numbers} 💿💿💿 "

    print(rounds_heading)

    # Looping starts here

    num_one = random.randint(low_num, high_num)
    num_two = random.randint(low_num, high_num)
    operations = random.choice(["+", "-", "*","Area","Perimeter"])

    # Calculate the user answers based in the operations
    if operations == "+":
        correct_answer = num_one + num_two
    elif operations == "-":
        correct_answer = num_one - num_two
    elif operations == "*":
        correct_answer = num_one * num_two
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
                user_answer=int(input(f" Round {rounds_played}: Area of rectangle (height = {num_one} , width= {num_two}) " ))
            elif operations == "Perimeter":
                user_answer= int(input(f" Round {rounds_played}: Perimeter of rectangle (height ={num_one} and width= {num_two}) " ))
            else:
                user_answer = int(input(f"Round {rounds_played}: {num_one}  {operations} {num_two} "))
            break
        except ValueError:
            print("Please enter a number! ")


    # Check the answer and output the history
    if user_answer == correct_answer:
        print("✅✅✅ Correct! ✅✅✅")
        score+=1
        feedback = "Correct"
    else:
        print(f" ❌❌❌ Incorrect! ❌❌❌ The answer was {correct_answer}.")
        feedback = f" Incorrect "

    # Save the answers for history
    if operations == "Area":
        quiz_history = f"Round {rounds_played}: Area of rectangle (height = {num_one} , width= {num_two}) = {user_answer} "
    elif operations == "Perimeter":
        quiz_history = f"Round {rounds_played}: Perimeter of rectangle (height ={num_one} and width= {num_two}) =  {user_answer} "
    else:
        quiz_history = f"Round {rounds_played}: {num_one}  {operations} {num_two}  = {user_answer}"
    history.append(quiz_history)



# Loop ends here
if question_numbers > 0:
    percentage = (score / rounds_played) * 100
    print(f"percentage: {percentage:.1f}%")
else:
    print("You have to enter numbers!")

# Display the game history on request
see_history = yes_no("\nDo you want to see your game history? ")
if see_history == "yes":
    for item in history:
            print(rounds_played)







