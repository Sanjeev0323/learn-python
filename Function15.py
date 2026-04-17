def sum(n):
    t=0
    for digit in str(abs(n)):
        t+=int(digit)
    return t
num =int(input("enter a number: "))
print(sum(num))
