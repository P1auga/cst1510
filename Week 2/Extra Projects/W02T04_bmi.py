weight = float(input("Enter weight in pounds: "))
height = float(input("Enter height in inches: "))

kg = weight * 0.45359237
meters = height * 0.0254
bmi = kg / (meters ** 2)

print(f"BMI is {bmi:.2f}")

if bmi < 18.5:
    print("Underweight")
elif bmi < 25.0:
    print("Normal")
elif bmi < 30.0:
    print("Overweight")
else:
    print("Obese")
