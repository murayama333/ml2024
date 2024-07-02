import random

num1 = random.randint(1, 10)
num2 = random.randint(1, 10)
correct_answer = num1 * num2

print(f"What is {num1} * {num2}?")
user_answer = int(input("Your answer: "))

if user_answer == correct_answer:
    print("Correct!")
else:
    print(f"Incorrect. The correct answer is {correct_answer}.")
