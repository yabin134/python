#program to print first 100 no in list even no list and odd no list
a=[]
b=[]
c=[]
for i in range(1,101):
    a.append(i)
    if i%2==0:
        b.append(i)
    else:
        c.append(i)    
# for j in range(1,100,2):
#     b.append(j)    
# for k in range(2,100,2):
#     c.append(k)
print('1 to 100 numbers',a)
print('ODD numbers list',b)    
print('EVEN numbers list',c)