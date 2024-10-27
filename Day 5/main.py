import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Crazy Password Maker!")
nr_letters = input("How many letters do you want in your password? (e.g., 4, 5, etc.)\n")
nr_symbols = input("Now, how many weird symbols do you want? (e.g., 2, 3, etc.)\n")
nr_numbers = input("Finally, how many numbers should I throw in there? (e.g., 1, 2, etc.)\n")

if not nr_letters.isdigit() or not nr_symbols.isdigit() or not nr_numbers.isdigit():
    print("What??? That wasn't a number. Try again with a number.")
else:
    password = []

    for _ in range(int(nr_letters)):
        password.append(random.choice(letters))

    for _ in range(int(nr_numbers)):
        password.append(random.choice(numbers))

    for _ in range(int(nr_symbols)):
        password.append(random.choice(symbols))

    random.shuffle(password)
    generated_password = ''.join(password)
    print(f"Here's your password: {generated_password}")

    if len(password) <= 6:
        print("*Sighs*, that's a bit short. Even my cat could crack this! Try at least 8 characters.")
    elif len(password) == 7:
        print("Not bad, but adding one more character might make it tougher for hackers (and my cat)")
    else:
        print("Now that's a strong password! Even a hacker would need coffee breaks to crack this one! Unless you store it in plain text and push it to Github")
