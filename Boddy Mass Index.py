height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

BodyMassIndex=weight/height**2

BMI=round(BodyMassIndex)

print(f"Your BMI is {BMI}.")
