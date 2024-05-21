#sum of digits of numbers in list 
# a=[11,22,33,44,55] question
# b=[2,4,6,8,10]    output

a=[11,22,33,44,55]
b=[]
for i in range(len(a)):
    num=a[i]
    digit=num%10
    digit=digit+digit
    b.append(digit)
print(b)
    