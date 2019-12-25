import random
winning_number = random.randint(1,100)
guess_number = int(input("guess any number bitween 1 and 100    :   "))
attempt = 1
game_over = False
while not game_over:
    if guess_number==winning_number:
        game_over = True
        continue
    elif guess_number < winning_number:
        print("too low..")
    else:
        print("to high...")
    guess_number= int(input("guess again    :   "))
    attempt+=1
print (f"YOU WIN!! and you guess number in {attempt} time.")