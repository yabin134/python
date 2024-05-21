#lcm of 2 numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1>0 and num2>0:
    if num2 % num1 == 0:
        lcm=num1
    elif num1 % num2==0:
      lcm=num2
print("LCM of", num1, "and", num2, "is:", lcm)
