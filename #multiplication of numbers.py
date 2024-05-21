#multiplication of numbers
limit=int(input("enter the limit  :"))
b=[]
for i in range(limit):
    z=int(input("enter values  :"))
    b.append(z)
print(b)

def multiplication(num):
    num=1
    for j in num:
        num=num*i
        j=j+j
    return num

print(multiplication(b))
