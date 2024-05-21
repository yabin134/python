#check if armstrong or not
sum=0
num=155
onum=num

while num>0:
    
    digit=num%10
    sum=sum+digit**3
    num=num//10
if onum==sum:
        print(f'{onum} is an armstrong number')
else:
      print(f'{onum} is not an armstrong number')    