#reverse of a number using functions
def reverse(number):
    rev=0
    while number>0:
        a=number%10
        rev=rev*10+a
        number=number//10
    return rev
number=int(input("Enter a number to be reversed  :"))
print(reverse(number))

