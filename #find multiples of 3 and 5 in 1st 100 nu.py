#find multiples of 3 and 5 in 1st 100 numbers
i=0
while i<=100:
    if i%5==0 and i%3==0:
        print(i,'Multiple')
    i=i+1
