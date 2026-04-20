def num(n):
    if n<=0:
        return
    num(n-1)
    print(n)
m=int(input("enter a number: "))
print(num(m))