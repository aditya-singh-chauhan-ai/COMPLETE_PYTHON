winning_number= 7
user_input= int(input("guesse the winning number : "))
if winning_number == user_input:
    print("you win")
else:
    if winning_number > user_input:
        print("too low")
    else:
        print("too high")
        # nested if else statement
        # like if we use if else statement in else statement then it is called nested if else statement
        #for cheching the equality of two numbers use ==
        #for cheching the inequality of two numbers use !=
        #for assign use single =