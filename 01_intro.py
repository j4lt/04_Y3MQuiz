import random


def check_rounds():
    while True:
        response = input("How many rounds would you like to play ? ")
        round_error = "Please type an integer that is more than 0"
        # If infinite mode not chosen, check response
        # is an integer that is more than 0
        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue
        return response


def statement_generator(statement, decoration):

    sides = decoration * 3

    sides = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


def answer_checker(question, valid_list, error):
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

game_summary = []
mode = "regular"
rounds_played = 0
answer_list = ["true", "false"]
rounds_won = 0
rounds_lost = 0


rounds = check_rounds()

if rounds == "":
    mode = "infinite"
    rounds = 5

end_game = "no"
while end_game == "no" and rounds_played < rounds:

    print()

    if mode == "infinite":
        heading = "Continuous Mode: Round {}".format(rounds_played + 1)
        rounds += 1
    else:
        heading = "Round {} of {}".format(rounds_played + 1, rounds)

    print(heading)
    print()

    num_1 = random.randint(1, 12)
    num_2 = random.randint(1, 12)

    fake_ans = random.randint(2, 30)

    question_1 = "{} * {} == {} ".format(num_1, num_2, fake_ans)
    actual_ans = eval(question_1)

    if fake_ans == actual_ans:
        answer = "true"

    else:
        answer = "false"

    choose_error = "Please enter true or false "

    # Ask user for choice and check it's valid
    choose = answer_checker(question_1, answer_list, choose_error)
    print(question_1)

    if choose == "xxx" and rounds_played > 0:
        break
    elif choose == "xxx":
        print("You need to play at least one round ! ")
        continue

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

