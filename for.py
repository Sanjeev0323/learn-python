c=0
a=int(input("enter a number: "))
b=int(input("enter a number: "))
for i in range(a,b):
    if i % 3 == 0 and i % 5 == 0:
       c=c+1
print(c)