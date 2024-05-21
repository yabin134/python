#prime no within a limit (100 to 200)
number=11
count=0
if number>=100 and number<=200:

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
else:
    print('Number less than 100 or more than 200')