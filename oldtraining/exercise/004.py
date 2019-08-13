
import random
result_number, guess_number = random.randint(1, 10), 2
while result_number != guess_number:
    guess_number = int(input('Guess a number between 1 and 10 until you get it right : '))
print('Well guessed!')