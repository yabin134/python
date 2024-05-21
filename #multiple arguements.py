#multiple arguements *args

# def function(*args):
#     sum=0
#     a=list(args)
#     for i in a:
#         sum+=i
#     return sum

# print(function(3,5,6,4,2,4))

#keyword arguements
def main(**kwargs):
    z=''
    for i,j in kwargs.items():
        z=z+f'{i} name is {j}'
    print(z)
main(fname='yabin',sname='paul',lname='thomas')