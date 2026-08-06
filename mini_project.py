# GUESS A NUMBER



import random

target = random.randint(1,1100)

while True:
    userinput = (input('guess the target or Quit (Q)'))
    if (userinput == 'Q'):
          break
    
    userinput = int(userinput)
    
    if (userinput == target):
        print('you win')
        break
    elif(userinput > target):
            print('guess lesser')
    else:
            print('guess high')
        
print('.....game over.....')



