def count(n):
    if n == 0:
        return
    print(n)
    count(n-1)
num=int(input("enter a number: "))
print(count(num))