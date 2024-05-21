#calculate bmi using functons

# bmi=weight/h*h
weight=int(input("Enter your weight in kg  :"))
height=int(input("Enter your height in meters  :"))
def bmi(weight,height):
    bmi=weight/height*height
    return bmi
print(bmi(weight,height))