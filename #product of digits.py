#product of digits
prod=1
n=int(input('Enter a number:  '))
while n>0:
    
    digit=n%10
    prod=prod*digit
    n=n//10
print('The product of digits is ',prod)