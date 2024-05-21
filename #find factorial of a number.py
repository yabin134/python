#find factorial of a number using function

def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    print(fact)

    
factorial(5)