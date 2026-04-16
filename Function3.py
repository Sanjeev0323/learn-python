def largest(a,b):
    if a>b:
        return a
    else:        
        return b
x=int(input("enter a number: "))
y=int(input("enter a number: "))
r=largest(x,y)
print("largest number is :",r)