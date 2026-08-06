import random #random module to generate random number
winning_number = random.randint(1,100)
guess = 1
num = int(input("enter your guess: "))
game_over = False

while not game_over:
    if num == winning_number:
        print(f"you win and you guessed this number in {guess} times")
        game_over = True
    else:
        if num < winning_number:
            print("too low")
        else:
            print("too high")
        
        guess += 1
        num = int(input("guess again : "))



#DRY - don't repeat yourself
#use functions to avoid repetition and less line of code