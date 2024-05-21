#list 
# a=[4,5,7,1,2,[10,80,5,['y','a','b','i','n'],5,5,6],5,1,2]
# print(a[5])
# print(a[5][3])
# print(a[5][3][2])


# b=['1','2','3','4',[1,2,['python','ml','django',['ha',['hari']],'ai','datascience'],4,5],'6','7','8','9']
# print(b[4][2][3][1][0])

# c=[1,2,3,4,5,6,7,8,9]  #list is mutable it shrinks and grows when we add elements
#c[0:5]=1,4
# c[1:4]=3,3,6,7,8,5,1
# print(c)

# d='python django' #string is not mutable
# d[1:3]='fdsf'
# print(d)


#find neg,pos and 0 in a list
# a=[1,-2,0,-10,3]
# for i in range(len(a)):
#     if a[i]>0:
#         print(a[i],"psoitive")
#     elif a[i]==0:
#         print(a[i],"value is 0")
#     else:
#         print(a[i],"negative")    
# a=[1,2,3,4,5,6,6]
#a.append(12) adds 12 to end of list
#a.extend('yabin') adds each eleemnt of string to the list
#a.insert(2,'yabin') adds the string the index position
#a.remove(2) removes an element from the list
#a.pop(1) removes an element from the 1 index
# a.pop() #removes the last element
# print(a) 

# a=[1,2,102,-9,10,3,2,5,6,7,5]
# a.reverse()
# print(a)

# a='this is may python batch'
# b=a.split('a')
# print(b)

# a='this is may python batch'
# b=a.split()
# print(b)

# a=['my', 'name', 'is', 'yabin']
# b=" ".join(a)
# print(b)

# a=['my', 'name', 'is', 'yabin']
# b='+'.join(a)
# print(b)

#split the list from the middle

# a=[1,23,65,23,65,87]
# b=[]
# c=[]
# split=int(len(a)/2)
# for i in range(split):

#     if i<split:
#         b.append(a[i])
#     else:
#         c.append(a[i])
# print(b)
# print(c)        


# a=['my', 'name', 'is', 'yabin']
# b=[]
# c=[]
# split=len(a)/2
# for i in range(len(a)):
#     if i<split:
#         b.append(a[i])
#     else:
#         c.append(a[i])
# print(b)
# print(c)


#a='this is may python batch' convert string to list
a='this is may python batch'
b=[]
s=''

for i in a:
    s=s+i
    if i==' ':
        continue
b.append(s)
print(b)
   

