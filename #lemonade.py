#lemonade
a=[5,5,5,10,20]
balance=0
for i in range(len(a)):
    bills=a[i]
    if bills==5:
        balance=balance+bills
    elif bills==10:
        balances=bills-5
    elif bills==20:
        balance=bills-15

if bills>balance:
    print('false')
    print(balance)
    
else:
    print('true')
    
