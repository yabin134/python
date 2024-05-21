#reccursion

def down(a):
    print(a)
    if a==0:
        return a
    else:
        return down(a-1)
    
down(10)