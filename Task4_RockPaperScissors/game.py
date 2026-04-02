import random

choices = ["rock", "paper", "scissors","star"]
user_score = 0
computer_score = 0

print("----* ROCK PAPER SCISSORS GAME * ----")

while True:
    user = input("\nEnter rock, paper,  scissors or , star: ").lower()

    if user not in choices:
        print("Invalid choice! Try again.")
        continue

    computer = random.choice(choices)

    print("You chose:", user)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")

    #Oprations Game paly
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
          (user == "paper" and computer == "rock") or \
         (user == "star" and computer in [ "rock","scissors"]):
        print("You win! ")
        user_score += 1

    else:
        print("Computer wins! ")
        computer_score += 1

    print(f"Score -> You: {user_score} | Computer: {computer_score}")

    again = input("Play again? (yes/no): ").lower()
    if again != "yes":
        print("Game Over!")
        break
