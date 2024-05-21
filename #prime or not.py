#prime or not
number=11
count=0
for i in range(1,11):
    if number==1:
        print('Not Prime')
    else:
        i=2
    
    if number%i==0:
        count=count+1
        
if count>0:
    print('not prime')
else:

    print('prime')
