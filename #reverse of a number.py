#reverse of a number

number = 235
rev = 0
while number > 0:
    a = number % 10
    rev = rev * 10 + a
    number = number // 10
print(rev)
