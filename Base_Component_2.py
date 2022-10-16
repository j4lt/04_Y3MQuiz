import random

# checks that user types in an integer more than zero
def check_rounds():
    while True:
        response = input("How many rounds would you like to play ? ")
        round_error = "Please type an integer that is more than 0"
        # If infinite mode not chosen, check response

        if response != "":
            try:
                response = int(response)

               # If response is too low, go back to
               # start of loop
                if response < 1:
                    print(round_error)
                    continue

                else:
                    return response

            except ValueError:
                print(round_error)
                continue


# decorates statements to make them stand out
def statement_generator(statement, decoration):

    sides = decoration * 3

    sides = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""

# checks user enters true / false
def answer_checker(question, answer_list, error):
    valid = False
    while not valid:

        response = input(question).lower()

        for item in answer_list:
            if response == item[0] or response == item:
                return item

        print(error)
        print()

statement_generator("YEAR 5 MATH QUIZ", "*" )
print()
print("This is a true or false math quiz for students in year 5 (10-11 years old)")
print("If you think the math equations are correct please enter 'true' ")
print("If you think the math equations are incorrect please enter 'false'   ")
print()

# Defines variables

game_summary = []
mode = "regular"
rounds_played = 0
answer_list = ["true", "false"]
rounds_won = 0
rounds_lost = 0


rounds = check_rounds()


end_game = "no"
while end_game == "no" and rounds_played < rounds:

    print()

    heading = "Round {} of {}".format(rounds_played + 1, rounds)

    print(heading)
    print()

    #Defines variables

    num_1 = random.randint(1, 12)
    num_2 = random.randint(1, 12)

    question = "{} * {}".format(num_1, num_2)

    fake_ans = random.randint(2, 30)
    actual_ans = eval(question)

    question_1 = "{} * {} == {} ".format(num_1, num_2, fake_ans)
    question_2 = "{} * {} == {} ".format(num_1, num_2, actual_ans)

    question_chooser = [question_1, question_2]
    to_ask = random.choice(question_chooser)


    if to_ask == question_1:
        answer = "false"

    else:
        answer = "true"

    choose_error = "Please enter true or false "

    # Ask user for choice and check it's valid
    choose = answer_checker(to_ask, answer_list, choose_error)
    # print(choose)

    if choose == answer:
        result = "Correct"
        rounds_won +=1

    else:
        result = "Incorrect"
        rounds_lost +=1

    if result == "Correct":
        feedback = "Correct"

    else:
        feedback = "Incorrect, answer = {}".format(actual_ans)

    print(feedback)

    rounds_played += 1

    if rounds_played == rounds:
        break



#End of Game Summary
print()
statement_generator("Quiz Results", "-")
print()
print("You got {} Correct and {} Incorrect".format(rounds_won, rounds_lost))
print()
statement_generator("Thanks For Playing My Quiz", "=")