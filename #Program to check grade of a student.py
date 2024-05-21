#Program to check grade of a student
maths=60
english=70
physics=30
biology=50
chem=65
marks=maths+english+physics+biology+chem
if marks>400:
    print('A grade')
elif marks>300:
    print('B grade')
elif marks>200:
    print('C grade')
else: 
    print('Fail')    