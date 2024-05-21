#find sum and avg of n numbers5
sum=0
n=int(input('Enter the total numbers'))
for i in range(n):
    number=int(input('enter the number 1 by 1 : '))
    sum=number+sum
    avg=number/n
print(f'sum of the numbers entered is {sum}')
print(f'avg of the numbers entered is {avg}')
