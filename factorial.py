# Python Program for factorial of a number
def factorial(number):
  return 1 if number == 1 or number == 0 else number * factorial(number - 1)
number = eval(input("Enter your number: "))
print(f"Factorial of {number} is {factorial(number)}")
