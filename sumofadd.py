def add(n):
    if n<=1:
        return 0
    return n + add(n-1)
m=int(input("enter a number: "))
print(add(m))