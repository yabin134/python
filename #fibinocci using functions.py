# #fibinocci using functions
# def fibinocci(limit):
#     i=0
#     n1,n2=0,1
#     print(n1)
#     print(n2)
#     while i<limit:
#         n3=n1+n2
#         print(n3)
#         n1=n2
#         n2=n3
#         i=i+1
# limit=int(input("Enter a limit :"))
# fibinocci(limit)

name=input("enter your name: ")

age=int(input("enter your age: "))

address=input("enter your address: ")
def info(name,age,address):
    age=2024-age
    print("entered name is",name)
    print("entered age is",age)
    print("entered address is",address)
info(name,age,address)