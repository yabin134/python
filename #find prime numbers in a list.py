#find prime numbers in a list
number=8
count=0
if number==1:
    print('Not Prime')
else:
    i=2
    while i<number:
        if number%i==0:
            count=count+1
        i=i+1
if count>0:
    print('not prime')
else:

    print('prime')

