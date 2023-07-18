import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
choices = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper, or 2 for scissors\n"))

if user_choice >= 3 or user_choice < 0:
    print("You entered an invalid number.")
else:
    print("You chose:\n" + choices[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:\n" + choices[computer_choice])

    if choices[user_choice] == choices[computer_choice]:
        print("It's a draw!")
    elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
        print("You win!")
    else:
        print("You lose!")
