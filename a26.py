def order(i,q,p=0):
 t=q*p
 print(f"order summary: {q} * {i}")
 print(f"total price is: {t}")
 print("positional argument is:")
 return t
print("keyword argument is:")
order(q=3,p=10,i="food")
print("default argument is:")
order(4,"burger")