#rock paper scisor game
# def choice():
#     ch=['ROCK','PAPER','SCISOR']
#     a=random.choice(ch)
#     b=print(a)
#     return(b)
# import random
# ch1=['rock','paper','scisor']
# c=None
# while c not in ch1:
#     inp=input("Enter a choice ROCK,PAPER,SCISOR  :")
#     if inp=='rock':
#         val=1
#         choice()
#     elif inp=='paper':
#         val=2
#         choice()
#     elif inp=='scisor':
#         val=3
#         choice()
#     else:
#         print("invalid input")


    
import random
ch=['rock','paper','scisor']
comp=random.choice(ch)
user=None

while user not in ch:
    user=input("Enter a choice ROCK,PAPER,SCISOR  :")

print('USERS choice  :',user)
print('COMPUTERS choice  :',comp)
if comp==user:
    print("draw")

if user=='rock':
    if comp=='paper':
        print('comp wins')
    else:
        print("user wins")

if user=='paper':
    if comp=='scisor':
        print('comp wins')
    else:
        print("user wins")


if user=='scisor':
    if comp=='rock':
        print('comp wins')
    else:
        print("user wins")