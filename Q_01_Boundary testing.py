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

# Main routine starts here

# Ask for the number of questions
print()
question_numbers= num_check("How many questions do you want? ")
if question_numbers == "xxx":
    print("Have a good day")
else:
    print(f"You chose {question_numbers} questions")