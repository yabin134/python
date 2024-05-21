#functions
# def hello():
#     print('Hello')
# def addition():
#     a=5
#     b=10
#     print(a+b)
# hello()

# addition()

def hello():
    #name='python'#global scope
    #print(name)
    def bye():
        name='yabin'#enclosing scope
        print(name)
        return name
        
print(hello())
 

