import random

answer = random.randint(1, 10)
guess_count = 0
guess = 0
print("Guess a number from 1-10")
while guess_count < 3:
    life_count = 3 - guess_count
    print(f"You've got {life_count} lives")
    try:
        guess = int(input("Enter a guess: "))
    except ValueError:
        print("Invalid input! Please try again.")
        continue
    if guess == answer:
        print("Good job! You win the game.")
        break
    elif guess < answer:
        print(f"The answer is higher than {guess}")
    elif guess > answer:
        print(f"The answer is lower than {guess}")
    else:
        print("Something went wrong.")
    guess_count += 1
else:
    print("Sorry! You are out of lives.")
