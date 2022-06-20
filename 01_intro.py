

def statement_generator(statement, decoration):

    sides = decoration * 3

    sides = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""

# Main routine

statement_generator("YEAR 6 MATH QUIZZ", "*" )
print()

rounds_lost = 0
rounds_won = 0
rounds_played = 0
game_summary = []
end_game = "no"

while rounds_played < rounds and end_game == "no":

    print("*** Round {} of {} ******".format(rounds_played + 1, rounds)) 

