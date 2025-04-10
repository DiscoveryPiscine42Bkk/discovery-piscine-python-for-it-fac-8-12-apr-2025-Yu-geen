
num1 = int(input("Enter the first number:\n"))
num2 = int(input("Enter the second number:\n"))

num = num1 * num2

print(f'{num1} x {num2} = {num}')

if num < 0:
	print("The result is negative.")
elif num == 0:
	print("The result is positive and negative.")
elif num > 0:
	print("The result is positive.")
