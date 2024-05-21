#first sum of 10 numbers using reccursion
def down(a):
    
    if a==0:
        return a
    else:
        return a+down(a-1)
    
print(down(10))