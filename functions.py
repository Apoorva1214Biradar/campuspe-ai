def groot():
 print('I am groot')
for i in range(5):
    groot()

#function with arguments/parameters and return types
#function with no arguments/parameters and only return types
#function with arguments/parameters and  no return types
#function with no arguments&parameters and  no return types
# name=input("enter your name:")
# def greet(name):
#    print(f"hello {name}")
#    print(
# "welcome to python programming"
#    )
# greet(name)
a=int(input("enter first number:"))
b=int(input("enter second number:"))
def sum(a,b):
   return a+b
  
print(f"sum of {a}+{b}=",sum(a,b))
help(sum)

def display_info(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
display_info(name="john",age=30, married=True)