height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

BodyMassIndex=weight/height**2

BMI=round(BodyMassIndex)

if BMI<18.5:
    print(f"Your BMI is {BMI} and you're underweight")
elif BMI<25:
    print(f"Your BMI is {BMI} and you're normal weight")
elif BMI<30:
    print(f"Your BMI is {BMI} and you're slightly weight")
elif BMI<35:
    print(f"Your BMI is {BMI} and you're obese")
else:
    print(f"Your BMI is {BMI} and you're clinically obese")
