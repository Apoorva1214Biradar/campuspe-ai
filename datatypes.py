#String
#message="Hey Bro wassup"
#mname="Apoorvs"
poem="""
She sells sea shells on the sea shore
Roses are red
Violets are blue
Well so are you!"
"""

#string Operations
f_name="Apoorva"
l_name="Biradar"

#concatenate
full_name=f_name+" "+l_name
print(full_name)

#Repetitive Characters
line="*" * len(full_name)
print(line)

print(full_name[6])
print(full_name[-1])

#string Upper and lower case
print(f_name.upper())
print(f_name.lower())

#Integer
a=10
b=20

print("addition",a+b)
print("subtraction",a-b)
print("multiplication",a*b)
print("division",a/b)
print("integer division",a//b)
print("modulus",a%b)
print("exponentiation",a**b)

#floats
pi=3.14
price=20.99
total=price*1.5
print(total)
print(round(0.1+0.345, 2))


#Booleans
is_raining=False
is_holiday=False
 
age=20
is_adult=age>=18
print(is_adult)