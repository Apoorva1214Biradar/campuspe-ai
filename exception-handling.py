# try:
#     number=int(input("enter a number:"))
#     result=100/number
#     print(result)
# except ValueError:
#     print("not a valid number")
# except ZeroDivisionError:
#     print("cannot be divide by zero")
# except exception as e:
#     print(f"an error")


def validate_age(age):
    if age<0:
        raise ValueError("age cannot be zero")
    if age>200:
        raise ValueError("not an error")
    
try:
    age=int(input("enter an age"))
    validate_age()
    print(age)
except :
    print(f"an error")