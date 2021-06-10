#Write your code below this line 👇
import math

def prime_checker(number):
	if(number <= 1):
		print("Not a prime number.")
	flag = 0

	for i in range(2, int(math.sqrt(number)) + 1):
		if number%i == 0:
			flag = 1
		break
	if flag == 1:
		print("Not a prime number.")
	else:
		print("prime number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)