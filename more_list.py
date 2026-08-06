#INSERT METHOD- TO PRINT IN ANY POSITION IN LIST
#JOINT - TO CONCETENATE TWO LIST
#EXTEND - TO ADD MULTIPLE ELEMENTS IN A LIST USE FOR ADD LIST 2 IN LIST 1
fruits1 = ['apple', 'banana']
fruits2 = ['banana' , ' mango']
fruits2.insert(0, 'cherry')     #insert
print(fruits2)  
fruits = fruits1 + fruits2      #joint  
print(fruits)
fruits1.extend(fruits2)         #extend
print(fruits1)