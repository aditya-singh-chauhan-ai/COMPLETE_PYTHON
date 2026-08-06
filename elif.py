# show ticket Pending
# 1 to 3 (free)
# 3 to 10 (150)
# 10 to 60 (300)
# above 60 (500)
age= int(input("enter your age: "))
if 1<age<=3:
    print("your ticket is free : ")
elif 3<age<=10:
    print("your ticket is 150 : ")
elif 10<age<=60:
    print("your ticket is 300 : ")
else:
    print("your ticket is 500 : ")
    if age ==0 or age<0:
        print("your age is invalid : ")