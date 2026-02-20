count=0
#While condition:
# while count<=5:
#     print("count is",count)
#     count+=1
# print("loop entered")

# for count in range(0,5):
#     print("count is",count)
    
# for i in range(1,10):
#     for j in range(i):
#         print("*",end="")
#     print()

numbers=[1,2,3,4,5]
serach_for=6
for num in numbers:
    if num==serach_for:
        print("number found")
        break
else:
        print("not found")