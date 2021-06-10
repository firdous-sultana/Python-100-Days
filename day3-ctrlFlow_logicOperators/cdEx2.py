# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = round(weight / (height * height))

if bmi < 18.5:
	print("Your bmi is " + str(bmi) + ", You are underweight.")
elif bmi < 25:
	print("Your bmi is " + str(bmi) + ", You are normal weight.")
elif bmi < 30:
	print("Your bmi is " + str(bmi) + ", You are slightly overweight.")
elif bmi < 35:
	print("Your bmi is " + str(bmi) + ", You are obese.")
else:
	print("Your bmi is " + str(bmi) + ", You are clinically obese.")
