height = float(input("Enter your height in centimeters: "))
weight = float(input("Enter your weight in kg: "))
height = height/100
bmi = weight/(height**2)
print("Your Body Mass Index: "+str(bmi))
if bmi>0:
    if bmi<=16:
        print("you are severely underweight.")
    elif bmi <= 18.5:
        print("your are underweight.")
    elif bmi <= 25:
        print("You are Healthy.")
    elif bmi <= 30:
        print("You are overweight.")
    else:
        print("You are severely overweight")
else:
    print("Enter valid details")