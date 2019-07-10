import json

answers = []

questions = {
            "name": "What's your name?",
            "birthday": "What's your date of birth? (MM/DD/YYYY)",
            "age": "How old are you?",
            "home": "Where do you call home? (City, State, Country)",
            "# of residents": "How many people live in your home more than 50% of the time?",
            "hrs/week on phone": "How many hours each week do you spend on your phone?",
            "favorite app": "Name the app/program/site you use most often"
            }

def get_answer(q, survey):
    survey[q] = input(f"{questions[q]}: ")

def append_answer(survey):
    answers.append(survey)

def show_quit_prompt():
    print("Would you like to take another survey? Press 'n' to quit.")

def quit_survey():
    return input() == 'n'

while True:
    survey = {}
    for q in questions:
        get_answer(q, survey)
    append_answer(survey)
    show_quit_prompt()
    if quit_survey():
        break
print(answers)

with open("survey_answers.json", "w") as f:
    f.write('[\n')
    index = 0
    for a in answers:
        json.dump(a, f)
        if (index < len(answers)-1):
            f.write(',\n')
        else:
            f.write('\n')
        index += 1
    f.write(']')
