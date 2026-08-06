#MODIY NUMBER GUESSING GAME
winning_number = 49
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
            guess += 1
            num = int(input("enter your guess: "))
        else:
            print("too high")
            guess += 1
            num = int(input("enter your guess: "))