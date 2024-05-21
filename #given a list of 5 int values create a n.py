#given a list of 5 int values create a new list with the sqaures of the first list
a=[2,4,5,7,5]
b=[]
for i in range(len(a)):
    num=a[i]
    num=num*num
    b.append(num)
print(b)

