# #Lists
students=["dennis","Apoorva"]
numbers=[8,1,6,4,5]
# mixed=["dennis",3.14,True]
# print(mixed[1:4])
# print(students[::2])
# print(students[::-1])
# students[1]="arun"
# print(students)
# students.pop()
# print(students)
# Operations on lists:
# Length
print(len(numbers))
# sum,min,max,
print("sum fo numbers of list is ",sum(numbers))
print(min(numbers))
print(max(numbers))

# count,
print(numbers.count(4))
# find index,
print("index of 3 is ",numbers.index(1))
# sort,
students.sort()
print(students)
# reverse,
numbers.reverse()
print(numbers)
# Check membership
print("Apoorva" in students)
for name in students:
    print(name)
    
#print(range(len(students)))
#for i in range(0,4,2):
#    print(f"{i}:{students[i]}")
#print(enummerate(students))
#for k,v in enumerate(students):
#    print(f"{k}:{v}")


#squares=[]
#for i in range(1,11)
# squares.append(i**2)
#print(squares)


#List comprehension
squares=[x**2 for x in range(1,11)]
print(squares)


#Tuples
coordiantes=(10,20)
person=("Apoorva",23,"Chitradurga")
#print(person[2])
name,age,district=person
#print(f"I am {name},from {district}.I am {age} years old")


#dictionaries
mathclass={}
student={
    "name":"Apoorva",
    "age":23,
    "garde":"A",

}
#print(student["name"])
student["phone"]="67672879298"
print(student.get("phone","users phone doesnt exist"))

# student["age"]=26
# print(student)

# student.pop("name")
# print(student)


#Set

numbers=[1,2,3,1,3,4,3,6,7,888,9,2,4,5,5,5,5,5,5]
u_numbers=set(numbers)
print(u_numbers)
u_numbers.discard(999)
