#sum of digits
sum=0
n=int(input('Enter a number:  '))
for i in range(n):
    digit=n%10
    sum=sum+digit
    n=n//10
print(sum)