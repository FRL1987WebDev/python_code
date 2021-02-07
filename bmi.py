height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = weight / (height * height)
bmi = round(bmi)

if bmi <= 18:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 22:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 28:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 33:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")