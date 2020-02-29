print("This is my guessing number game")
import random
Random_number = random.randrange(1,5)
guess = int(input(" What could be the number? "))
correct = False
print(Random_number)

while not correct:
    if guess==Random_number:
        print("congrats your are guessing number is right")
        correct = True 
    elif guess>Random_number:
        print("sorry your number is high")
        break   
    elif guess<Random_number:
        print("sorry your number is low")
        break   
    else:
        print("Try something else") 
