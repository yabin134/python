#program to print all numbers which are divisible by m and n in the list
a=[]
m=int(input("enter a value for m:  "))
n=int(input("enter a value for n:  "))
for i in range(1,301):
    if i%m==0 and i%n==0:
        a.append(i)
print(a)