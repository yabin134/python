#factorial of a number using reccursion
def down(a):
    
    if a==5:
        return a
    else:
        return a*down(a+1)
    
print(down(1))