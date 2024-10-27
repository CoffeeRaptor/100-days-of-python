def greet(name, location):
    print(f"Hai {name}\nHow are you {name}?\nLovely weather in {location} !!!!!\n")

greet(location="Somewhere in the universe", name="Rick Sanchez")

check1 = "true"
check2 = "love"


def calculate_love_score(name1, name2):
    score1 = 0
    score2 = 0
    for letter in name1:
        if letter in check1:
            score1 = score1 + 1
        if letter in check2:
            score1 = score1 + 1

    for letter in name2:
        if letter in check1:
            score2 = score2 + 1
        if letter in check2:
            score2 = score2 + 1

    print(f"{score1}{score2}")

calculate_love_score(name1="Rick Sanchez", name2="Diana")
