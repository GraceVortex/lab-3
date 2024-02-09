import random

rand = random.randomint(1,20)

name = input("Hello , what is your name? \n")

t = 0
while True:
    if t == 0:
        guess_num = int(input(f'''Well, {name}, I am thinking of a number between 1 and 20. 
        Take a guess.'''))
    else:
        guess_num = int(input("Take a guess again: "))
    t+=1
    if guess_num == rand:
        print(f"Good job, {name}! You guessed my number in {t} guesses!")
        break
    elif guess_num > rand:
        print("Your guess is too high.")
    else:
        print("Your guess is too low.")
    

            
