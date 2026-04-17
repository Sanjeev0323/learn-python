def even(n):
    even_list=[]
    for x in n:
        if x % 2==0:
            even_list.append(x)
        return even_list
print(even([1,2,3,4,5,6]))
