import random

num_1 = random.randint(1, 12)
num_2 = random.randint(1, 12)

question = "{} * {}".format(num_1, num_2)

# evaluate the answer
actual_ans = eval(question)
fake_ans = random.randint(2,30)

t_f_question = "{} * {} = {}".format(num_1, num_2, fake_ans)
t_f_question_2 = "{} * {} == {}".format(num_1, num_2, actual_ans)

# list containing two possible questions
question_chooser = [t_f_question, t_f_question_2]
to_ask = random.choice(question_chooser)

ask_it = input(to_ask)
