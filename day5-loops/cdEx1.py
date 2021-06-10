# write a program that calculates the average student height from a List of heights

suma = 0
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  suma += student_heights[n]
# 🚨 Don't change the code above 👆
avg = round(suma / len(student_heights))
print(avg)

#Write your code below this row 👇
