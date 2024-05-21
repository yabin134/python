#find min and max from this list
a=[1,2,102,-9,10,3,2,5,6,7,5]
min=a[0]
max=a[0]
for num in a:
    if num<min:
        min=num
    elif num>max:
        max=num   
print(min)
print(max)



