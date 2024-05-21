#concatinate the n string
concat=''
n=int(input('Enter the total number of words'))
for i in range(n):
    number=(input('enter the words 1 by 1 : '))
    concat=concat+number
print(f'The concatinated string is {concat}')