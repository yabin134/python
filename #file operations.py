#file operations

#to read contents of a file
with open('file test.txt','r') as f:
    a=f.read()
    print(a)



# to write contents to a file


# with open('file test.txt','w') as f:
#     f.write('This is a test file')

with open('file test.txt','a') as f:
    f.write('\n Test')