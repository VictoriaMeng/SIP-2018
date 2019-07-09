import json

with open('survey_answers.json', 'r') as f:
    filedata = json.load(f)

def average_age():
    ages = [int(survey["age"]) for survey in filedata]
    return sum(ages) / len(ages)

def unique_answers():
    answers = [survey["name"] for survey in filedata]
    return len(list(set(answers)))

def mar_or_dec(date):
    month = date.split("/")[0]
    return month == "03" or month == "12"

def mar_dec_birthdays():
    birthdays = [survey["birthday"] for survey in filedata if mar_or_dec(survey["birthday"])]
    return len(birthdays)

print(f"Average age of respondents: {average_age()}")
print(f"Unique answers: {unique_answers()}")
print(f"Mar/Dec birthdays: {mar_dec_birthdays()}")
