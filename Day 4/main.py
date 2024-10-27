import random

# Print the rules of the game
print('''
Welcome to Elemental Battle!
The rules are simple:
- Water extinguishes Fire
- Fire burns Air
- Air blows away Water

Choose your element wisely to defeat your opponent!
''')

# Element visuals
water = '''
    🌊
     ~~~~~
  ~~~~~~~~~
~~~~~~~~~~~~~
 ~~~~~~~~~~~
'''

fire = '''
    🔥
     (    )
    (      )
   (        )
    (      )
     (    )
      ( )
'''

air = '''
    💨
      _______
     /       \\
    /         \\
   /           \\
  /             \\
 /_______________\\
'''

# User and computer choices
choice = input("Choose your element! Type 0 for Water, 1 for Fire, or 2 for Air\n0/1/2: ")
computer_choice = random.randint(0, 2)

if not choice.isdigit():
    print("Invalid input! Please choose a number between 0-2.")
else:
    choice = int(choice)
    if choice > 2:
        print("Invalid choice! Please pick a number between 0-2.")
    else:
        # Display player's choice
        if choice == 0:
            print(f"You chose: Water {water}")
        elif choice == 1:
            print(f"You chose: Fire {fire}")
        elif choice == 2:
            print(f"You chose: Air {air}")

        # Display computer's choice
        if computer_choice == 0:
            print(f"The computer chose: Water {water}")
        elif computer_choice == 1:
            print(f"The computer chose: Fire {fire}")
        elif computer_choice == 2:
            print(f"The computer chose: Air {air}")

        # Determine the outcome
        if choice == computer_choice:
            print("It's a draw! Both elements cancel each other out.")
        elif (choice == 0 and computer_choice == 1) or (choice == 1 and computer_choice == 2) or (choice == 2 and computer_choice == 0):
            print("You win! Your element overpowers the opponent!")
        else:
            print("You lose! The opponent's element overpowers yours.")
