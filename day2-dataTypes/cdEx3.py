# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
years_left = 90 - int(age)

days = round(years_left * 365)
weeks = round(years_left * 52)
months = round(years_left * 12)

message = print(f'You have {days} days, {weeks} weeks and {months} months left.')

print(message)