name_str=input("hi what is your name ")
age =int(input("hi "+name_str+", what is your age? "))
if age>= 18:
    print("You are eligible to vote")
else:
    print("you are baccha " +name_str+"Go and have icecream")

#IF ELSE If STATEMENT
# score=int(input("enter your score"))
# if score >=90:
#     grade="A"
# elif score >=80:
#     grade="B"
# elif score >=70:
#     grade="C"
# else:
#     grade="D"

# print("Your grade is:", grade)

#Nested if statement
# age=int(input("enter your age"))
# if age>=18:
#     print("you can vote")
#     if age>=21:
#         print("you are male and you are allowed to marry")
#     else:
#         print("you can also drive")
# else:
#     print("tou are not eligivble to vote")


## age=20
#has_ticket=False
# if age>=18 and has_ticket:
#     print("You can watch the movie")
#else:
#print("cannot enter")

#If else using or
#day="monday
# if day=="saturday" or day=="sunday":
#     print("it is a holiday")
#else:
#print("its a weekday")

#If else using NOT
#is_sunny=True
# if not is_sunny:
#     print("It's cloudy today")
# else:
#     print("It's sunny today")

#ternary operator
# age=21
# if age>=18:
#     status="adult"
# else:    status="minor"
status="adult" if age>=18 else "minor"
print(status)