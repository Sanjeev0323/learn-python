def gcd(a,b):
    while b:
        a,b=b,a%b
        #temp=b
        #b=a%b
        #temp=a
    return a
n=int(input("number 1: "))
m=int(input("number 2: "))
print(gcd(n,m)) 